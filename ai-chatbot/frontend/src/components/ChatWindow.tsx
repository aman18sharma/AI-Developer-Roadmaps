import {
  useEffect,
  useRef,
  useState,
} from "react";

import ChatMessage from "./ChatMessage";
import ChatInput from "./ChatInput";

import {
  getConversation,
  sendMessage,
} from "../services/api";

import type { Message } from "../types/chat";

interface Props {
  conversationId?: string;
  onConversationCreated: (id: string) => void;
  onConversationUpdated: () => void;
}

export default function ChatWindow({
  conversationId,
  onConversationCreated,
  onConversationUpdated,
}: Props) {
  const [messages, setMessages] =
    useState<Message[]>([]);

  const [loading, setLoading] =
    useState(false);

  const messagesEndRef =
    useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    async function loadConversation() {
      if (!conversationId) {
        setMessages([]);
        return;
      }

      try {
        setLoading(true);

        const conversation =
          await getConversation(
            conversationId
          );

        setMessages(
          conversation.messages
        );
      } catch (error) {
        console.error(
          "Failed to load conversation",
          error
        );
      } finally {
        setLoading(false);
      }
    }

    void loadConversation();
  }, [conversationId]);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({
      behavior: "smooth",
    });
  }, [messages, loading]);

  async function handleSend(
    message: string
  ) {
    setMessages((previous) => [
      ...previous,
      {
        role: "user",
        content: message,
      },
    ]);

    setLoading(true);

    try {
      const result = await sendMessage(
        message,
        conversationId
      );

      setMessages((previous) => [
        ...previous,
        {
          role: "assistant",
          content: result.response,
        },
      ]);

      if (!conversationId) {
        onConversationCreated(
          result.conversation_id
        );
      }

      onConversationUpdated();
    } catch (error) {
      console.error(error);

      setMessages((previous) => [
        ...previous,
        {
          role: "assistant",
          content:
            "Something went wrong. Please try again.",
        },
      ]);
    } finally {
      setLoading(false);
    }
  }

  const isEmpty =
    messages.length === 0 &&
    !conversationId;

  return (
    <div className="chat-window">

      <div className="messages-container">

        {isEmpty ? (
          <div className="welcome-screen">

            <div className="welcome-symbol">
              ✦
            </div>

            <h1>
              What can I help
              <br />
              you build today?
            </h1>

            <p>
              Ask a question, explore an idea,
              or start building something.
            </p>

            <div className="suggestions">

              <button
                onClick={() =>
                  handleSend(
                    "Help me design a FastAPI project"
                  )
                }
              >
                <span>⌘</span>
                Build a FastAPI project
              </button>

              <button
                onClick={() =>
                  handleSend(
                    "Explain RAG architecture"
                  )
                }
              >
                <span>◈</span>
                Explain RAG architecture
              </button>

              <button
                onClick={() =>
                  handleSend(
                    "Help me build an AI agent"
                  )
                }
              >
                <span>✦</span>
                Build an AI agent
              </button>

              <button
                onClick={() =>
                  handleSend(
                    "Review my code"
                  )
                }
              >
                <span>⌘</span>
                Review my code
              </button>

            </div>

          </div>
        ) : (
          <>
            {messages.map(
              (message, index) => (
                <ChatMessage
                  key={
                    message.id ?? index
                  }
                  message={message}
                />
              )
            )}

            {loading && (
              <div className="thinking">
                <span className="thinking-dot" />
                AI is thinking...
              </div>
            )}
          </>
        )}

        <div ref={messagesEndRef} />
      </div>

      <div
        className={`composer-area ${isEmpty
          ? "composer-centered"
          : ""
          }`}
      >
        <ChatInput
          onSend={handleSend}
          disabled={loading}
        />

        <div className="composer-footer">
          AI can make mistakes. Check important information.
        </div>

      </div>
    </div>
  );
}