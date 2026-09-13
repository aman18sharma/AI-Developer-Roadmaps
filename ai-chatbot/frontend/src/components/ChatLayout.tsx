import { useEffect, useState } from "react";

import ChatSidebar from "./ChatSidebar";
import ChatWindow from "./ChatWindow";

import { getConversations, getCurrentUser } from "../services/api";

import type { Conversation } from "../types/chat";
import UserMenu from "./UserMenu";

export default function ChatLayout() {
  const [conversations, setConversations] =
    useState<Conversation[]>([]);

  const [currentUser, setCurrentUser] = useState<CurrentUser | null>(null);

  const [activeConversationId, setActiveConversationId] =
    useState<string | undefined>(undefined);

  // Forces ChatWindow to completely reset
  const [chatInstance, setChatInstance] = useState(0);

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

  useEffect(() => {
    async function loadUser() {
      try {
        const user = await getCurrentUser();
        setCurrentUser(user);
      } catch (error) {
        console.error(
          "Failed to load current user",
          error
        );
      }
    }

    void loadUser();
  }, []);

  function handleNewChat() {
    // Clear selected conversation
    setActiveConversationId(undefined);

    // Force a completely fresh ChatWindow
    setChatInstance((value) => value + 1);
  }

  function handleSelectConversation(id: string) {
    setActiveConversationId(id);
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
          activeConversationId={activeConversationId}
          onSelect={handleSelectConversation}
          onNewChat={handleNewChat}
        />
      )}

      <main className="main-panel">

        <header className="topbar">

          <button
            type="button"
            className="icon-button mobile-menu"
            onClick={() =>
              setSidebarOpen((value) => !value)
            }
          >
            ☰
          </button>

          <div className="brand">
            <div className="brand-mark">
              B & W
            </div>

            <span>Black &amp; White</span>
          </div>

          <div className="topbar-actions">
            {currentUser ? (
              <UserMenu user={currentUser} />
            ) : '?'}
          </div>

        </header>

        <ChatWindow
          key={`${chatInstance}-${activeConversationId ?? "new"}`}
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