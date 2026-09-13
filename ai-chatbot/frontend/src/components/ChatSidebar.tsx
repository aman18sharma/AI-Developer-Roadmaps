import type { Conversation } from "../types/chat";

interface Props {
  conversations: Conversation[];
  activeConversationId?: string;
  onSelect: (id: string) => void;
  onNewChat: () => void;
}

export default function ChatSidebar({
  conversations,
  activeConversationId,
  onSelect,
  onNewChat,
}: Props) {
  return (
    <aside className="sidebar">
      {/* Fixed header */}
      <div className="sidebar-top">
        <div className="sidebar-brand">
          <div className="sidebar-logo">B & W</div>
          <span>Black &amp; White</span>
        </div>

        <button
          type="button"
          className="new-chat-button"
          onClick={onNewChat}
        >
          <span className="new-chat-icon">＋</span>
          <span>New chat</span>
          {/* <kbd>Ctrl K</kbd> */}
        </button>
      </div>

      {/* Only this section scrolls */}
      <div className="sidebar-scroll">
        <div className="sidebar-section">
          <div className="section-label">
            Recent
          </div>

          {conversations.length === 0 ? (
            <div className="empty-history">
              Your conversations will appear here.
            </div>
          ) : (
            conversations.map((conversation) => {
              const active =
                conversation.id ===
                activeConversationId;

              return (
                <button
                  type="button"
                  key={conversation.id}
                  className={`history-item ${active ? "history-active" : ""
                    }`}
                  onClick={() =>
                    onSelect(conversation.id)
                  }
                  title={conversation.title}
                >
                  <span className="history-dot">
                    {active ? "●" : "○"}
                  </span>

                  <span className="history-title">
                    {conversation.title}
                  </span>
                </button>
              );
            })
          )}
        </div>
      </div>

      {/* Fixed footer */}
      <div className="sidebar-footer">
        <button
          type="button"
          className="sidebar-footer-item"
        >
          <span>⚙</span>
          <span>Settings</span>
        </button>

        <button
          type="button"
          className="sidebar-footer-item"
        >
          <span>◉</span>
          <span>Profile</span>
        </button>

        <div className="version">
          B & W v0.1
        </div>
      </div>
    </aside>
  );
}