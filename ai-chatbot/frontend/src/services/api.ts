import type {
  AIModel,
  ChatResponse,
  Conversation,
  ConversationDetail,
} from "../types/chat";


const API_URL =
  import.meta.env.VITE_API_URL ||
  "http://localhost:8000";


function authHeaders() {
  const token =
    localStorage.getItem("access_token");

  return {
    "Content-Type": "application/json",
    ...(token
      ? {
          Authorization: `Bearer ${token}`,
        }
      : {}),
  };
}


/* =========================================
   AUTH
========================================= */

export async function login(
  email: string,
  password: string
) {
  const formData = new URLSearchParams();

  formData.append(
    "username",
    email
  );

  formData.append(
    "password",
    password
  );

  const response = await fetch(
    `${API_URL}/api/auth/login`,
    {
      method: "POST",

      headers: {
        "Content-Type":
          "application/x-www-form-urlencoded",
      },

      body: formData,
    }
  );

  if (!response.ok) {
    const error =
      await response.json().catch(
        () => null
      );

    throw new Error(
      error?.detail ||
        "Invalid email or password"
    );
  }

  const result = await response.json();

  localStorage.setItem(
    "access_token",
    result.access_token
  );

  return result;
}

export async function register(
  name: string,
  email: string,
  password: string
) {
  const response = await fetch(
    `${API_URL}/api/auth/register`,
    {
      method: "POST",

      headers: {
        "Content-Type":
          "application/json",
      },

      body: JSON.stringify({
        name,
        email,
        password,
      }),
    }
  );

  if (!response.ok) {
    const error =
      await response.json().catch(
        () => null
      );

    throw new Error(
      error?.detail ||
        "Registration failed"
    );
  }

  return response.json();
}


export function logout() {
  localStorage.removeItem(
    "access_token"
  );
}


export function isAuthenticated() {
  return Boolean(
    localStorage.getItem(
      "access_token"
    )
  );
}


/* =========================================
   CHAT
========================================= */

export async function sendMessage(
  message: string,
  conversationId?: string,
  model: string = "gpt-4o-mini"
): Promise<ChatResponse> {

  const response = await fetch(
    `${API_URL}/api/chat`,
    {
      method: "POST",

      headers: authHeaders(),

      body: JSON.stringify({
        message,
        conversation_id:
          conversationId,
        model,
      }),
    }
  );

  if (!response.ok) {

    const error =
      await response.json().catch(
        () => null
      );

    throw new Error(
      error?.error?.message ||
        error?.detail ||
        "Failed to send message"
    );
  }

  return response.json();
}


/* =========================================
   CONVERSATIONS
========================================= */

export async function getConversations()
: Promise<Conversation[]> {

  const response = await fetch(
    `${API_URL}/api/conversations`,
    {
      headers: authHeaders(),
    }
  );

  if (!response.ok) {

    if (response.status === 401) {
      logout();
    }

    const error =
      await response.json().catch(
        () => null
      );

    throw new Error(
      error?.error?.message ||
        error?.detail ||
        "Failed to load conversations"
    );
  }

  return response.json();
}


export async function getConversation(
  id: string
): Promise<ConversationDetail> {

  const response = await fetch(
    `${API_URL}/api/conversations/${id}`,
    {
      headers: authHeaders(),
    }
  );

  if (!response.ok) {

    const error =
      await response.json().catch(
        () => null
      );

    throw new Error(
      error?.error?.message ||
        error?.detail ||
        "Failed to load conversation"
    );
  }

  return response.json();
}


/* =========================================
   MODELS
========================================= */

export async function getModels()
: Promise<AIModel[]> {

  const response = await fetch(
    `${API_URL}/api/models`
  );

  if (!response.ok) {
    throw new Error(
      "Failed to load models"
    );
  }

  return response.json();
}


/* =========================================
   CURRENT USER
========================================= */

export async function getCurrentUser() {

  const response = await fetch(
    `${API_URL}/api/auth/me`,
    {
      headers: authHeaders(),
    }
  );

  if (!response.ok) {
    throw new Error(
      "Failed to load user"
    );
  }

  return response.json();
}