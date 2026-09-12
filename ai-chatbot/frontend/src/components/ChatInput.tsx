import { useState } from "react";

interface Props {
  onSend: (
    message: string
  ) => Promise<void>;

  disabled?: boolean;
}

export default function ChatInput({
  onSend,
  disabled = false,
}: Props) {
  const [input, setInput] =
    useState("");

  async function handleSend() {
    const message =
      input.trim();

    if (!message || disabled) {
      return;
    }

    setInput("");

    await onSend(message);
  }

  return (
    <div className="composer">

      <textarea
        value={input}
        disabled={disabled}
        rows={1}
        placeholder="Ask anything..."
        onChange={(event) =>
          setInput(event.target.value)
        }
        onKeyDown={(event) => {
          if (
            event.key === "Enter" &&
            !event.shiftKey
          ) {
            event.preventDefault();
            void handleSend();
          }
        }}
      />

      <button
        className="send-button"
        disabled={
          disabled ||
          !input.trim()
        }
        onClick={() =>
          void handleSend()
        }
      >
        ↑
      </button>

    </div>
  );
}