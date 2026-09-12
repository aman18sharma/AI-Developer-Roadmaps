import { useEffect, useState } from "react";

import ChatSidebar from "./ChatSidebar";
import ChatWindow from "./ChatWindow";

import { getConversations } from "../services/api";

import type { Conversation } from "../types/chat";

export default function ChatLayout() {
  const [conversations, setConversations] =
    useState<Conversation[]>([]);

  const [activeConversationId, setActiveConversationId] =
    useState<string | undefined>();

  const [sidebarOpen, setSidebarOpen] = useState(true);

  async function loadConversations() {
    try {
      const data = await getConversations();
      setConversations(data);
    } catch (error) {
      console.error(
        "Failed to load conversations",
        error
      );
    }
  }

  useEffect(() => {
    void loadConversations();
  }, []);

  function handleNewChat() {
    setActiveConversationId(undefined);
  }

  function handleConversationCreated(id: string) {
    setActiveConversationId(id);
    void loadConversations();
  }

  function handleConversationUpdated() {
    void loadConversations();
  }

  return (
    <div className="app-shell">

      {sidebarOpen && (
        <ChatSidebar
          conversations={conversations}
          activeConversationId={
            activeConversationId
          }
          onSelect={setActiveConversationId}
          onNewChat={handleNewChat}
        />
      )}

      <main className="main-panel">

        <header className="topbar">

          <button
            className="icon-button mobile-menu"
            onClick={() =>
              setSidebarOpen((value) => !value)
            }
          >
            ☰
          </button>

          <div className="brand">
            <div className="brand-mark">✦</div>
            <span>Black & White</span>
          </div>

          <div className="topbar-actions">
            <button className="icon-button">
              ?
            </button>

            <button className="avatar">
              A
            </button>
          </div>
        </header>

        <ChatWindow
          conversationId={activeConversationId}
          onConversationCreated={
            handleConversationCreated
          }
          onConversationUpdated={
            handleConversationUpdated
          }
        />

      </main>
    </div>
  );
}