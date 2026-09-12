import type {
  ChatResponse,
  Conversation,
  ConversationDetail,
} from "../types/chat";


const API_URL =
  import.meta.env.VITE_API_URL ||
  "http://localhost:8000";


export async function sendMessage(
  message: string,
  conversationId?: string
): Promise<ChatResponse> {

  const response = await fetch(
    `${API_URL}/api/chat`,
    {
      method: "POST",

      headers: {
        "Content-Type": "application/json",
      },

      body: JSON.stringify({
        message,
        conversation_id:
          conversationId,
      }),
    }
  );

  if (!response.ok) {
    throw new Error(
      "Failed to send message"
    );
  }

  return response.json();
}


export async function getConversations()
: Promise<Conversation[]> {

  const response = await fetch(
    `${API_URL}/api/conversations`
  );

  if (!response.ok) {
    throw new Error(
      "Failed to load conversations"
    );
  }

  return response.json();
}


export async function getConversation(
  id: string
): Promise<ConversationDetail> {

  const response = await fetch(
    `${API_URL}/api/conversations/${id}`
  );

  if (!response.ok) {
    throw new Error(
      "Failed to load conversation"
    );
  }

  return response.json();
}