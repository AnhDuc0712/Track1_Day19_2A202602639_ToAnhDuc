"""Local server for the lecture demo.

Serves index.html and proxies Smart AI Note calls to GPT-4o mini.
The API key stays in the repo-root .env file and is never sent to the browser.
"""

import json
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent
ENV_PATH = ROOT.parent / ".env"
HOST = "127.0.0.1"
PORT = 8765


def load_env(path):
    values = {}
    if not path.exists():
        return values
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or "=" not in stripped:
            continue
        key, value = stripped.split("=", 1)
        values[key.strip()] = value.strip().strip('"').strip("'")
    return values


def context_messages(payload):
    title = str(payload.get("title") or "")[:200]
    heading = str(payload.get("heading") or "")[:200]
    excerpt = str(payload.get("excerpt") or "")[:2000]
    around = str(payload.get("around") or "")[:4000]
    return [
        {
            "role": "system",
            "content": (
                "Bạn là Smart AI Note trong một bài giảng. "
                "Người học vừa bôi đen hoặc copy một đoạn. "
                "Giải thích đoạn đó trong đúng ngữ cảnh bài giảng, bằng tiếng Việt, trong 2 đến 3 câu. "
                "Chỉ dùng đoạn trích và phần xung quanh được cung cấp. "
                "Không bịa số liệu. Không chào hỏi. Không nhắc lại yêu cầu."
            ),
        },
        {
            "role": "user",
            "content": (
                f"Tiêu đề bài: {title}\n"
                f"Mục: {heading}\n"
                f"Đoạn người học vừa lưu:\n{excerpt}\n\n"
                f"Ngữ cảnh xung quanh trong bài:\n{around}"
            ),
        },
    ]


def ask_messages(payload):
    question = str(payload.get("question") or "")[:2000]
    notes = payload.get("notes") or []
    history = payload.get("history") or []
    blocks = []
    for note in notes[:12]:
        if not isinstance(note, dict):
            continue
        kind = str(note.get("kind") or "text")[:40]
        heading = str(note.get("heading") or "")[:200]
        text = str(note.get("text") or "")[:2500]
        context = str(note.get("context") or "")[:800]
        blocks.append(f"[{kind}] {heading}\n{text}")
        if context:
            blocks.append(f"Nhận định AI đã ghi cho phần này:\n{context}")
    packed = "\n\n".join(blocks)[:12000] or "(chưa có đoạn nào được lưu)"
    messages = [
        {
            "role": "system",
            "content": (
                "Bạn là chatbox của các note phía trên. "
                "Nguồn duy nhất: nguyên văn note đã lưu, và ngữ cảnh AI đã viết kèm note. "
                "Hãy trả lời ngắn bằng tiếng Việt khi câu hỏi nói về ý đã có trong hai nguồn đó, kể cả khi người học diễn đạt khác đi. "
                "Ví dụ: note nói tester không được nghe nhóm pitch option, thì câu hỏi 'vì sao không được giới thiệu giải pháp?' phải được trả lời từ note, không được từ chối. "
                "Không thêm dữ kiện mới ngoài note và ngữ cảnh đã viết. "
                "Chỉ từ chối khi chủ đề không liên quan tới các note, và khi đó dùng đúng câu: "
                "'Trong các note và ngữ cảnh đã lưu chưa có phần này.'"
            ),
        },
        {"role": "user", "content": f"Note đã lưu và ngữ cảnh AI đã viết:\n{packed}"},
    ]
    for turn in history[-8:]:
        if not isinstance(turn, dict):
            continue
        role = turn.get("role")
        if role not in ("user", "assistant"):
            continue
        messages.append({"role": role, "content": str(turn.get("content") or "")[:2000]})
    messages.append({"role": "user", "content": question})
    return messages


def call_model(base, key, model, messages):
    body = json.dumps(
        {"model": model, "temperature": 0.2, "messages": messages},
        ensure_ascii=False,
    ).encode("utf-8")
    request = Request(
        base.rstrip("/") + "/chat/completions",
        data=body,
        headers={
            "Authorization": "Bearer " + key,
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with urlopen(request, timeout=45) as response:
        data = json.loads(response.read().decode("utf-8"))
    return data["choices"][0]["message"]["content"].strip()


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def do_POST(self):
        path = self.path.split("?", 1)[0]
        if path not in ("/api/context", "/api/ask"):
            self.send_error(404)
            return
        length = int(self.headers.get("Content-Length", "0") or 0)
        raw = self.rfile.read(length) if length else b"{}"
        try:
            payload = json.loads(raw.decode("utf-8"))
        except json.JSONDecodeError:
            self.reply(400, {"error": "JSON không hợp lệ."})
            return
        env = load_env(ENV_PATH)
        key = env.get("OPENAI_API_KEY", "")
        model = env.get("OPENAI_MODEL") or "gpt-4o-mini"
        base = env.get("OPENAI_BASE_URL") or "https://api.openai.com/v1"
        if not key:
            self.reply(500, {"error": "Chưa có OPENAI_API_KEY trong file .env."})
            return
        try:
            messages = context_messages(payload) if path == "/api/context" else ask_messages(payload)
            text = call_model(base, key, model, messages)
        except HTTPError as error:
            message = "OpenAI từ chối yêu cầu."
            try:
                detail = json.loads(error.read().decode("utf-8", "replace"))
                message = detail.get("error", {}).get("message") or message
            except (json.JSONDecodeError, AttributeError):
                pass
            self.reply(502, {"error": message})
            return
        except (URLError, KeyError, IndexError, TimeoutError):
            self.reply(502, {"error": "Không kết nối được tới GPT-4o mini."})
            return
        self.reply(200, {"text": text})

    def reply(self, status, body):
        data = json.dumps(body, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)


if __name__ == "__main__":
    server = ThreadingHTTPServer((HOST, PORT), Handler)
    print(f"Smart AI Note at http://{HOST}:{PORT}/", flush=True)
    server.serve_forever()
