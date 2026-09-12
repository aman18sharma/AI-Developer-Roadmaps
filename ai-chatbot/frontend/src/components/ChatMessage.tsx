import ReactMarkdown from "react-markdown";
import remarkGfm from "remark-gfm";

import type {
  Message,
} from "../types/chat";


interface Props {
  message: Message;
}


export default function ChatMessage({
  message,
}: Props) {

  const isUser =
    message.role === "user";

  return (
    <div
      className={`message-row ${isUser
        ? "user-row"
        : "assistant-row"
        }`}
    >

      <div
        className={`message-bubble ${isUser
          ? "user-message"
          : "assistant-message"
          }`}
      >

        <div className="message-role">
          {isUser
            ? "You"
            : "AI Assistant"}
        </div>

        {isUser ? (
          <div className="message-content">
            {message.content}
          </div>
        ) : (
          <div className="message-content">
            <ReactMarkdown
              remarkPlugins={[
                remarkGfm,
              ]}
            >
              {message.content}
            </ReactMarkdown>
          </div>
        )}

      </div>

    </div>
  );
}