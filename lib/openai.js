const ASK_SYSTEM = [
  "Bạn là chatbox của các note phía trên.",
  "Nguồn duy nhất: nguyên văn note đã lưu, và ngữ cảnh AI đã viết kèm note.",
  "Hãy trả lời ngắn bằng tiếng Việt khi câu hỏi nói về ý đã có trong hai nguồn đó, kể cả khi người học diễn đạt khác đi.",
  "Ví dụ: note nói tester không được nghe nhóm pitch option, thì câu hỏi 'vì sao không được giới thiệu giải pháp?' phải được trả lời từ note, không được từ chối.",
  "Không thêm dữ kiện mới ngoài note và ngữ cảnh đã viết.",
  "Chỉ từ chối khi chủ đề không liên quan tới các note, và khi đó dùng đúng câu:",
  "'Trong các note và ngữ cảnh đã lưu chưa có phần này.'",
].join(" ");

const CONTEXT_SYSTEM = [
  "Bạn là Smart AI Note trong một bài giảng.",
  "Người học vừa chọn một đoạn và gắn màu để lưu.",
  "Giải thích đoạn đó trong đúng ngữ cảnh bài giảng, bằng tiếng Việt, trong 2 đến 3 câu.",
  "Chỉ dùng đoạn trích và phần xung quanh được cung cấp.",
  "Không bịa số liệu. Không chào hỏi. Không nhắc lại yêu cầu.",
].join(" ");

function clip(value, max) {
  return String(value || "").slice(0, max);
}

function contextMessages(payload) {
  const title = clip(payload.title, 200);
  const heading = clip(payload.heading, 200);
  const excerpt = clip(payload.excerpt, 2000);
  const around = clip(payload.around, 4000);
  return [
    { role: "system", content: CONTEXT_SYSTEM },
    {
      role: "user",
      content: `Tiêu đề bài: ${title}\nMục: ${heading}\nĐoạn người học vừa lưu:\n${excerpt}\n\nNgữ cảnh xung quanh trong bài:\n${around}`,
    },
  ];
}

function askMessages(payload) {
  const question = clip(payload.question, 2000);
  const notes = Array.isArray(payload.notes) ? payload.notes : [];
  const history = Array.isArray(payload.history) ? payload.history : [];
  const blocks = [];
  for (const note of notes.slice(0, 12)) {
    if (!note || typeof note !== "object") continue;
    const kind = clip(note.kind || "text", 40);
    const heading = clip(note.heading, 200);
    const text = clip(note.text, 2500);
    const context = clip(note.context, 800);
    blocks.push(`[${kind}] ${heading}\n${text}`);
    if (context) blocks.push(`Nhận định AI đã ghi cho phần này:\n${context}`);
  }
  const packed = blocks.join("\n\n").slice(0, 12000) || "(chưa có đoạn nào được lưu)";
  const messages = [
    { role: "system", content: ASK_SYSTEM },
    { role: "user", content: `Note đã lưu và ngữ cảnh AI đã viết:\n${packed}` },
  ];
  for (const turn of history.slice(-8)) {
    if (!turn || (turn.role !== "user" && turn.role !== "assistant")) continue;
    messages.push({ role: turn.role, content: clip(turn.content, 2000) });
  }
  messages.push({ role: "user", content: question });
  return messages;
}

async function callModel(messages) {
  const key = process.env.OPENAI_API_KEY || "";
  const model = process.env.OPENAI_MODEL || "gpt-4o-mini";
  const base = (process.env.OPENAI_BASE_URL || "https://api.openai.com/v1").replace(/\/$/, "");
  if (!key) {
    const error = new Error("Chưa có OPENAI_API_KEY trên Vercel.");
    error.status = 500;
    throw error;
  }
  const response = await fetch(`${base}/chat/completions`, {
    method: "POST",
    headers: {
      Authorization: `Bearer ${key}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ model, temperature: 0.2, messages }),
  });
  const data = await response.json().catch(() => ({}));
  if (!response.ok) {
    const error = new Error(data.error?.message || "OpenAI từ chối yêu cầu.");
    error.status = 502;
    throw error;
  }
  const text = data.choices?.[0]?.message?.content?.trim();
  if (!text) {
    const error = new Error("Không nhận được câu trả lời từ GPT-4o mini.");
    error.status = 502;
    throw error;
  }
  return text;
}

module.exports = { contextMessages, askMessages, callModel };
