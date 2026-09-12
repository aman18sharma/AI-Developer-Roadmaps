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

      <div className="sidebar-brand">
        <div className="sidebar-logo">✦</div>
        <span>Black & White</span>
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

      <div className="sidebar-scroll">

        <div className="sidebar-section">
          <div className="section-label">
            Recent
          </div>

          {conversations.length === 0 && (
            <div className="empty-history">
              Your conversations
              will appear here.
            </div>
          )}

          {conversations.map((conversation) => {
            const active =
              conversation.id ===
              activeConversationId;

            return (
              <button
                key={conversation.id}
                className={`history-item ${active ? "history-active" : ""
                  }`}
                onClick={() =>
                  onSelect(conversation.id)
                }
              >
                <span className="history-dot">
                  {active ? "●" : "○"}
                </span>

                <span className="history-title">
                  {conversation.title}
                </span>
              </button>
            );
          })}
        </div>

      </div>

      {/* <div className="sidebar-footer">

        <button className="sidebar-footer-item">
          <span>⌘</span>
          Settings
        </button>

        <button className="sidebar-footer-item">
          <span>◉</span>
          Profile
        </button>

        <div className="version">
          Black & White v0.1
        </div>

      </div> */}
    </aside>
  );
}