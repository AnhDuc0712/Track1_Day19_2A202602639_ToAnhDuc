const { contextMessages, callModel } = require("../lib/openai");

module.exports = async function handler(req, res) {
  if (req.method !== "POST") {
    res.status(405).json({ error: "Chỉ nhận POST." });
    return;
  }
  try {
    const text = await callModel(contextMessages(req.body || {}));
    res.status(200).json({ text });
  } catch (error) {
    res.status(error.status || 502).json({ error: error.message || "Không gọi được AI." });
  }
};
