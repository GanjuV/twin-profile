"""Styling constants for the digital twin Gradio app."""

INDIGO = "#6366f1"
VIOLET = "#8b5cf6"
PINK = "#ec4899"

EXAMPLES = [
    "Tell me about your background and experience.",
    "What kinds of projects are you working on now?",
    "What are your strongest technical skills?",
    "How can I get in touch with you?",
]

CSS = """
:root {
  --twin-accent-1: #6366f1;
  --twin-accent-2: #8b5cf6;
  --twin-accent-3: #ec4899;
  --twin-accent-gradient: linear-gradient(135deg, var(--twin-accent-1), var(--twin-accent-2));
  --twin-bg: #0b0c10;
  --twin-surface: #16171f;
  --twin-surface-2: #1e1f29;
  --twin-bubble-assistant: #1e1f29;
  --twin-border: rgba(255, 255, 255, 0.08);
  --twin-border-strong: rgba(255, 255, 255, 0.16);
  --twin-text: #edeef2;
  --twin-muted: #8c8d9a;
  --twin-shadow: rgba(0, 0, 0, 0.45);
}

/* Light mode: Gradio adds `.dark` to <body> when dark; absence = light.
   Accent gradient stays identical, only the neutral palette flips. */
body:not(.dark) {
  --twin-bg: #eef0f6;
  --twin-surface: #ffffff;
  --twin-surface-2: #f4f5f9;
  --twin-bubble-assistant: #f0f1f6;
  --twin-border: rgba(15, 15, 25, 0.08);
  --twin-border-strong: rgba(15, 15, 25, 0.14);
  --twin-text: #17181f;
  --twin-muted: #6b6c78;
  --twin-shadow: rgba(30, 30, 60, 0.12);
}

footer, .built-with, .show-api, .api-docs { display: none !important; }

html, gradio-app { background: var(--twin-bg) !important; }

body {
  background: radial-gradient(circle at 15% -10%, rgba(99, 102, 241, 0.22), transparent 50%),
              radial-gradient(circle at 100% 0%, rgba(236, 72, 153, 0.14), transparent 45%),
              var(--twin-bg) !important;
  background-repeat: no-repeat !important;
  background-attachment: fixed !important;
  min-height: 100vh !important;
}

/* ---------- Stable layout ---------- */
.gradio-container {
  background: transparent !important;
  color: var(--twin-text) !important;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
  width: 100% !important;
  max-width: 820px !important;
  min-width: 0 !important;
  margin: 0 auto !important;
  padding: 36px 20px 40px !important;
}
.gradio-container .main, .gradio-container .contain, .gradio-container .wrap {
  width: 100% !important;
  max-width: 100% !important;
  min-width: 0 !important;
}
.gradio-container * { min-width: 0; }

/* ---------- Title ---------- */
.gradio-container h1 {
  display: flex !important;
  align-items: center !important;
  gap: 10px !important;
  color: var(--twin-text) !important;
  font-size: 24px !important;
  font-weight: 700 !important;
  letter-spacing: -0.02em !important;
  margin: 4px 5px !important;
  text-align: left !important;
}
.gradio-container h1::before {
  content: "";
  display: inline-block;
  flex: none;
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: var(--twin-accent-gradient);
  box-shadow: 0 0 6px 3px rgba(99, 102, 241, 0.35);
  overflow: visible;
}

/* ---------- Rounded, soft surfaces everywhere ---------- */
.chatbot, .chatbot *, .block, .form,
button, input, textarea,
.examples button {
  border-radius: 16px !important;
}

/* ---------- Block surfaces ---------- */
.block, .form { background: transparent !important; box-shadow: none !important; }

/* ---------- Hide the Chatbot label / header strip ---------- */
.chatbot > .block-label,
.chatbot > label,
.chatbot .label-wrap,
.chatbot .block-label,
.chatbot > .label-container {
  display: none !important;
}

/* ---------- Chatbot frame: elevated card with soft glow ---------- */
.chatbot, .chatbot.block {
  background: var(--twin-surface) !important;
  border: 1px solid var(--twin-border) !important;
  border-radius: 24px !important;
  min-height: 480px !important;
  box-shadow: 0 24px 60px -20px var(--twin-shadow), 0 1px 0 rgba(255, 255, 255, 0.03) inset !important;
  padding: 6px !important;
  overflow: hidden !important;
}
.chatbot .placeholder, .chatbot .placeholder * { color: var(--twin-muted) !important; }

/* ---------- Floating toolbar (share / clear / copy) ----------
   Clipped by the card's own rounded corner via overflow:hidden above;
   styled here so it reads as a pill instead of a stray rectangle. */
.top-panel {
  background: var(--twin-surface-2) !important;
  border: 1px solid var(--twin-border) !important;
  border-radius: 12px !important;
  box-shadow: 0 4px 10px -4px var(--twin-shadow) !important;
  margin: 6px !important;
  overflow: hidden !important;
}

/* ---------- Message rows: strip parent backgrounds ---------- */
.message-row,
.message-row > div,
.message-row .role,
.message-wrap, .bubble-wrap {
  background: transparent !important;
  border: 0 !important;
  box-shadow: none !important;
}

.message-row {
  animation: twin-fade-in 0.25s ease-out both;
}
@keyframes twin-fade-in {
  from { opacity: 0; transform: translateY(6px); }
  to { opacity: 1; transform: translateY(0); }
}

/* ---------- Reset borders on every bubble variant first ---------- */
.message-row .message,
.message-row .message-bubble,
.message-row .bubble {
  border: 0 !important;
  box-shadow: 0 1px 2px var(--twin-shadow) !important;
  padding: 10px 14px !important;
}

/* ---------- Bubble shapes: chat-app tail effect ---------- */
.message-row.user-row .message,
.message-row.user-row .message-bubble,
.message-row.user-row .bubble,
.message-row[data-role="user"] .message,
.message-row[data-role="user"] .message-bubble {
  background: var(--twin-accent-gradient) !important;
  color: #ffffff !important;
  border-radius: 18px 18px 4px 18px !important;
}

.message-row.bot-row .message,
.message-row.bot-row .message-bubble,
.message-row.bot-row .bubble,
.message-row[data-role="assistant"] .message,
.message-row[data-role="assistant"] .message-bubble {
  background: var(--twin-bubble-assistant) !important;
  color: var(--twin-text) !important;
  border: 1px solid var(--twin-border) !important;
  border-radius: 18px 18px 18px 4px !important;
}

/* Suppress radius/shadow doubling on nested bubble elements */
.message-row .message .message,
.message-row .message .bubble,
.message-row .message .message-bubble,
.message-row .bubble .message,
.message-row .bubble .bubble,
.message-row .bubble .message-bubble,
.message-row .message-bubble .message,
.message-row .message-bubble .bubble,
.message-row .message-bubble .message-bubble {
  border-radius: 0 !important;
  box-shadow: none !important;
  border: 0 !important;
  padding: 0 !important;
}

/* ---------- Uniform font size in bubbles ---------- */
.message-row .message,
.message-row .message-bubble,
.message-row .bubble {
  font-size: 14.5px !important;
  line-height: 1.6 !important;
}
.message-row .message p,
.message-row .message-bubble p,
.message-row .bubble p,
.message-row .prose p {
  font-size: 14.5px !important;
  line-height: 1.6 !important;
  margin: 0 0 8px !important;
  color: inherit !important;
}
.message-row .message p:last-child,
.message-row .message-bubble p:last-child,
.message-row .bubble p:last-child,
.message-row .prose p:last-child { margin-bottom: 0 !important; }

/* Strip stray internal borders/backgrounds from anything inside a bubble */
.message-row .message *,
.message-row .message-bubble *,
.message-row .bubble * {
  background: transparent !important;
  border-color: transparent !important;
  box-shadow: none !important;
  color: inherit !important;
}
.message-row .message a,
.message-row .message-bubble a {
  color: inherit !important;
  text-decoration: underline;
  text-decoration-color: currentColor;
  opacity: 0.9;
}

/* ---------- Tables inside bubbles ----------
   Tight columns were forcing mid-word breaks ("Perio" / "d"). Keep words
   whole and let wide tables scroll horizontally instead of crushing text.
   Broad selector because we don't know which wrapper class (.prose vs
   .message vs .bubble) actually holds the <table> in the running Gradio. */
.message-row .message:has(table),
.message-row .message-bubble:has(table),
.message-row .bubble:has(table),
.message-row .prose:has(table) {
  max-width: 100% !important;
  overflow-x: auto !important;
  -webkit-overflow-scrolling: touch !important;
  display: block !important;
}
.message-row table {
  width: max-content !important;
  min-width: 100% !important;
  border-collapse: collapse !important;
}
.message-row .message th, .message-row .message td,
.message-row .message-bubble th, .message-row .message-bubble td,
.message-row .bubble th, .message-row .bubble td {
  word-break: normal !important;
  overflow-wrap: normal !important;
  white-space: normal !important;
  text-align: left !important;
  vertical-align: top !important;
  padding: 8px 12px !important;
  border: 1px solid var(--twin-border) !important;
}

/* Safety net: nothing on the page should ever force horizontal scroll
   of the whole viewport, no matter how wide a table renders. */
html, body, .gradio-container { overflow-x: hidden !important; }

/* ---------- Input row alignment ---------- */
.input-row,
.gr-input-row,
.chat-input-row,
form[class*="input"] {
  align-items: center !important;
  gap: 8px !important;
  background: var(--twin-surface) !important;
  border: 1px solid var(--twin-border) !important;
  border-radius: 28px !important;
  padding: 6px !important;
  margin-top: 16px !important;
  box-shadow: 0 12px 30px -18px var(--twin-shadow) !important;
}

textarea, input[type="text"] {
  background: transparent !important;
  border: 0 !important;
  border-radius: 22px !important;
  color: var(--twin-text) !important;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
  font-size: 14.5px !important;
  padding: 12px 16px !important;
  line-height: 1.4 !important;
  min-height: 44px !important;
}
textarea:focus, input[type="text"]:focus {
  outline: none !important;
  box-shadow: none !important;
}
textarea::placeholder, input::placeholder { color: var(--twin-muted) !important; }

/* ---------- Buttons ---------- */
button {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
  letter-spacing: 0 !important;
  text-transform: none !important;
  font-size: 13px !important;
  font-weight: 600 !important;
  border: 1px solid var(--twin-border) !important;
  border-radius: 14px !important;
  background: var(--twin-surface-2) !important;
  color: var(--twin-text) !important;
  padding: 0 16px !important;
  min-height: 44px !important;
  align-self: stretch !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  cursor: pointer;
  transition: transform 0.12s ease, box-shadow 0.12s ease, border-color 0.12s ease, background 0.12s ease;
}
button:hover { border-color: var(--twin-border-strong) !important; transform: translateY(-1px); }

button.primary,
button[variant="primary"],
button.submit,
button.submit-button,
.submit-button,
button.lg.primary {
  background: var(--twin-accent-gradient) !important;
  border: 0 !important;
  color: #ffffff !important;
  min-height: 44px !important;
  width: 44px !important;
  align-self: center !important;
  border-radius: 50% !important;
  padding: 0 !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  box-shadow: 0 8px 20px -8px rgba(99, 102, 241, 0.6) !important;
}
button.primary:hover,
button.submit:hover,
.submit-button:hover,
button.lg.primary:hover {
  transform: translateY(-1px) scale(1.04);
  box-shadow: 0 10px 24px -6px rgba(99, 102, 241, 0.7) !important;
}

/* ---------- Submit-button icon: center and size correctly ---------- */
button.submit svg,
button.submit-button svg,
.submit-button svg,
button.primary svg,
button[variant="primary"] svg {
  width: 18px !important;
  height: 18px !important;
  margin: 0 auto !important;
  display: block !important;
  align-self: center !important;
  color: #ffffff !important;
  fill: currentColor !important;
  stroke: currentColor !important;
}

/* ---------- Examples: pill chips ---------- */
.examples, .examples-holder, [data-testid="examples"] {
  background: transparent !important;
  padding: 0 !important;
  margin-top: 16px !important;
}
.examples table, .examples-table { background: transparent !important; border: 0 !important; }
.examples button, .example, .examples td button, [data-testid="examples"] button {
  background: var(--twin-surface) !important;
  border: 1px solid var(--twin-border) !important;
  color: var(--twin-text) !important;
  border-radius: 999px !important;
  text-transform: none !important;
  letter-spacing: 0 !important;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
  font-size: 13px !important;
  font-weight: 500 !important;
  padding: 10px 16px !important;
  text-align: left !important;
  min-height: 0 !important;
  align-self: auto !important;
  display: inline-block !important;
  transition: border-color 0.12s ease, transform 0.12s ease;
}
.examples button:hover, .example:hover, [data-testid="examples"] button:hover {
  border-color: var(--twin-accent-1) !important;
  color: var(--twin-accent-1) !important;
  background: var(--twin-surface) !important;
  transform: translateY(-1px);
}

/* ---------- Icon buttons (clear, retry, copy) ---------- */
.icon-button, .chatbot .icon-button {
  color: var(--twin-muted) !important;
  background: transparent !important;
  border: 0 !important;
  border-radius: 10px !important;
  min-height: 0 !important;
  align-self: auto !important;
  padding: 4px !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
}
.icon-button:hover, .chatbot .icon-button:hover {
  color: var(--twin-accent-1) !important;
  background: var(--twin-surface-2) !important;
}

/* ---------- Scroll-to-bottom affordance ----------
   Was floating bare over the last message line; give it a solid disc,
   shadow, and breathing room so it reads as a control, not clipped text. */
.scroll-down-button-container {
  bottom: 14px !important;
  background: transparent !important;
}
.scroll-down-button-container button {
  background: var(--twin-surface) !important;
  border: 1px solid var(--twin-border) !important;
  border-radius: 50% !important;
  width: 36px !important;
  min-height: 36px !important;
  box-shadow: 0 6px 16px -6px var(--twin-shadow) !important;
  color: var(--twin-muted) !important;
}
.scroll-down-button-container button:hover {
  color: var(--twin-accent-1) !important;
  border-color: var(--twin-accent-1) !important;
}

/* ---------- Scrollbar ---------- */
::-webkit-scrollbar { width: 8px; height: 8px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: var(--twin-border-strong); border-radius: 999px; }
::-webkit-scrollbar-thumb:hover { background: var(--twin-accent-2); }

/* ---------- Selection ---------- */
::selection { background: var(--twin-accent-2); color: #ffffff; }

/* ---------- Mobile ---------- */
@media (max-width: 640px) {
  .gradio-container { padding: 24px 12px 32px !important; }
  .gradio-container h1 { font-size: 20px !important; }
  .chatbot, .chatbot.block { border-radius: 18px !important; }
  .input-row, .gr-input-row, .chat-input-row, form[class*="input"] { border-radius: 22px !important; }
}
"""

JS = """
() => {
  document.title = 'Digital Twin';

  const focusInput = () => {
    const areas = document.querySelectorAll('textarea');
    if (areas.length) areas[areas.length - 1].focus();
  };
  setTimeout(focusInput, 300);

  // Re-focus the message field whenever Gradio re-enables it
  // (i.e. after the assistant finishes responding).
  const watchTextarea = (area) => {
    if (area.dataset.twinWatched) return;
    area.dataset.twinWatched = '1';
    let wasDisabled = area.disabled || area.readOnly;
    new MutationObserver(() => {
      const isDisabled = area.disabled || area.readOnly;
      if (wasDisabled && !isDisabled) area.focus();
      wasDisabled = isDisabled;
    }).observe(area, { attributes: true, attributeFilter: ['disabled', 'readonly'] });
  };

  const scan = () => document.querySelectorAll('textarea').forEach(watchTextarea);
  setTimeout(scan, 500);
  new MutationObserver(scan).observe(document.body, { childList: true, subtree: true });
}
"""
