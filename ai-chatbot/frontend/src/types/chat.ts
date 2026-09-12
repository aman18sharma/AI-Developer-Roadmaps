export type MessageRole =
  | "user"
  | "assistant";

export interface Message {
  id?: number;
  role: MessageRole;
  content: string;
  created_at?: string;
}

export interface ChatResponse {
  response: string;
  conversation_id: string;
}

export interface Conversation {
  id: string;
  title: string;
  created_at: string;
  updated_at: string;
}

export interface ConversationDetail
  extends Conversation {
  messages: Message[];
}