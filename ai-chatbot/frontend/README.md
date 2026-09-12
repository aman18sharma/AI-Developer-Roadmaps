# Black & White — Frontend

Modern React + TypeScript frontend for the Black & White chatbot.

The frontend provides a Kimi-inspired AI workspace with persistent chat history, conversation switching, model selection, Markdown rendering, and a clean responsive chat interface.

## Features

* React + TypeScript
* Vite
* Kimi-inspired UI
* Chat history sidebar
* New Chat
* Continue previous conversations
* Dynamic model selection
* Markdown rendering
* GitHub Flavored Markdown
* Code block support
* Responsive design
* FastAPI integration
* Loading/typing state
* Conversation-aware chat requests

## Application Flow

```text
                    React UI
                       |
          +------------+------------+
          |                         |
          v                         v
    Chat History               Chat Window
          |                         |
          |                    Model Selector
          |                         |
          +------------+------------+
                       |
                       v
                API Service
                       |
                       v
                  FastAPI
                       |
                       v
                  AI Model
```

## Project Structure

```text
frontend/
│
├── src/
│   ├── components/
│   │   ├── ChatInput.tsx
│   │   ├── ChatLayout.tsx
│   │   ├── ChatMessage.tsx
│   │   ├── ChatSidebar.tsx
│   │   ├── ChatWindow.tsx
│   │   └── ModelSelector.tsx
│   │
│   ├── services/
│   │   └── api.ts
│   │
│   ├── types/
│   │   └── chat.ts
│   │
│   ├── App.tsx
│   ├── main.tsx
│   └── index.css
│
├── public/
├── .env
├── package.json
├── tsconfig.json
├── vite.config.ts
└── README.md
```

## Technology Stack

* React
* TypeScript
* Vite
* CSS
* React Markdown
* Remark GFM
* Fetch API

## Requirements

* Node.js 18+
* npm

Check your versions:

```bash
node --version
npm --version
```

## Installation

Enter the frontend directory:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Install Markdown support:

```bash
npm install react-markdown remark-gfm
```

## Environment Variables

Create:

```text
frontend/.env
```

Example:

```env
VITE_API_URL=http://localhost:8000
```

The frontend uses this variable when calling the FastAPI backend.

## Running the Application

Start Vite:

```bash
npm run dev
```

The application will normally be available at:

```text
http://localhost:5173
```

## Production Build

Create a production build:

```bash
npm run build
```

Preview the production build:

```bash
npm run preview
```

## Main Components

### ChatLayout

Controls the overall application layout.

Responsibilities:

* Sidebar
* Chat window
* Active conversation
* New chat
* Conversation refresh

### ChatSidebar

Displays:

* New Chat button
* Recent conversations
* Active conversation
* Conversation selection

Example:

```text
Recent

● FastAPI chatbot
○ RAG architecture
○ React debugging
○ AWS design
```

### ChatWindow

Handles:

* Message rendering
* Conversation loading
* Sending messages
* Loading state
* Empty/welcome screen

### ChatInput

Handles:

* User input
* Enter-to-send
* Send button
* Disabled state while AI responds

### ChatMessage

Handles:

* User messages
* Assistant messages
* Markdown rendering

### ModelSelector

Allows the user to choose the AI model:

```text
GPT-4o Mini
GPT-4o
Claude
Ollama
```

The actual model list comes from the backend.

## API Integration

API communication is centralized in:

```text
src/services/api.ts
```

### Send Message

```http
POST /api/chat
```

Example:

```json
{
  "message": "Explain FastAPI",
  "conversation_id": "abc-123",
  "model": "gpt-4o-mini"
}
```

### Get Conversations

```http
GET /api/conversations
```

### Get Conversation

```http
GET /api/conversations/{conversation_id}
```

### Get Models

```http
GET /api/models
```

## Conversation Handling

When the user clicks **New Chat**:

```text
activeConversationId = undefined
```

The current chat window resets.

When the user sends the first message:

```text
React
  |
  v
POST /api/chat
  |
  v
Backend creates conversation
  |
  v
conversation_id returned
  |
  v
React stores active conversation
```

When a previous conversation is clicked:

```text
GET /api/conversations/{id}
```

The messages are loaded into the chat window.

## Markdown

Assistant responses are rendered with:

```tsx
<ReactMarkdown
  remarkPlugins={[remarkGfm]}
>
  {message.content}
</ReactMarkdown>
```

This supports:

* Headings
* Bold text
* Italics
* Lists
* Links
* Tables
* Code blocks
* Blockquotes
* GitHub-style Markdown

## UI Design

The interface follows a modern AI workspace pattern:

```text
┌─────────────────────────────────────────┐
│ AI Studio                     Profile   │
├──────────────┬──────────────────────────┤
│ + New Chat   │                          │
│              │       AI Assistant       │
│ Recent       │                          │
│              │     Conversation         │
│ FastAPI      │                          │
│ RAG          │                          │
│ React        │                          │
│              │ ──────────────────────── │
│ Settings     │ Ask anything...      ↑   │
└──────────────┴──────────────────────────┘
```

The design intentionally uses:

* Spacious layout
* Minimal borders
* Rounded controls
* Neutral colors
* Large central composer
* Persistent chat history
* Model selection

## Model Selection

Models are loaded dynamically:

```typescript
const models = await getModels();
```

The selected model is sent with every chat request:

```typescript
await sendMessage(
  message,
  conversationId,
  selectedModel
);
```

This keeps model selection under user control.

## Responsive Design

The application supports smaller screens.

Desktop:

```text
Sidebar + Chat
```

Mobile:

```text
Chat
+
Collapsible sidebar
```

## Development Commands

Start development server:

```bash
npm run dev
```

Build:

```bash
npm run build
```

Preview:

```bash
npm run preview
```

Lint:

```bash
npm run lint
```

## Suggested Future Features

### Chat UX

* Streaming responses
* Copy response
* Copy code
* Regenerate response
* Edit user message
* Retry failed request
* Stop generation

### Files

* File upload
* PDF upload
* Image upload
* Document preview

### AI

* Multiple model providers
* Model comparison
* Model-specific settings
* Temperature control
* Agent mode

### Productivity

* Search chat history
* Rename conversation
* Delete conversation
* Pin conversation
* Export conversation

### Agentic AI

* Research mode
* Coding mode
* RAG mode
* Agent mode
* Tool selection

## Production Considerations

Before production deployment:

* Configure production API URL
* Enable authentication
* Add secure token handling
* Restrict backend CORS
* Add error boundaries
* Add analytics
* Optimize bundle size
* Add accessibility testing
* Add automated frontend tests

## Testing

Recommended test structure:

```text
src/
├── components/
└── __tests__/
    ├── ChatWindow.test.tsx
    ├── ChatSidebar.test.tsx
    ├── ChatInput.test.tsx
    └── ModelSelector.test.tsx
```

Recommended tools:

* Vitest
* React Testing Library
* Playwright

## License

## License

This project is licensed under the MIT License.

Copyright (c) 2026 Aman Sharma

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
