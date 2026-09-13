# BacBlack & White — Backend

FastAPI backend for the Black & White chatbot.

The backend provides chat APIs, conversation persistence, message history, model selection, and LLM integration. It is designed to evolve into a RAG and Agentic AI platform.

## Features

* FastAPI REST API
* AI chat completion
* Xkiro/OpenAI-compatible LLM integration
* User-selected AI models
* Persistent conversations
* Persistent messages
* Conversation history
* Conversation continuation
* SQLite database for local development
* PostgreSQL-ready architecture
* Pydantic request/response validation
* SQLAlchemy ORM
* CORS support
* Health check endpoint
* Modular service architecture

## Architecture

```text
                    Client
                      |
                      v
                 FastAPI API
                      |
        +-------------+-------------+
        |             |             |
        v             v             v
       Chat      Conversations    Models
        |             |             |
        +-------------+-------------+
                      |
                      v
              Service Layer
                      |
             +--------+--------+
             |                 |
             v                 v
        SQLAlchemy          LLM Service
             |                 |
             v                 v
        SQLite/Postgres    Xkiro / LLM API
```

## Project Structure

```text
backend/
│
├── app/
│   ├── __init__.py
│   │
│   ├── api/
│   │   ├── __init__.py
│   │   ├── chat.py
│   │   ├── conversations.py
│   │   └── models.py
│   │
│   ├── ai/
│   │   ├── __init__.py
│   │   └── models.py
│   │
│   ├── db/
│   │   ├── __init__.py
│   │   └── database.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── conversation.py
│   │   └── message.py
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── chat.py
│   │   └── conversation.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── chat_service.py
│   │   ├── conversation_service.py
│   │   └── llm_service.py
│   │
│   ├── config.py
│   └── main.py
│
├── .env
├── requirements.txt
├── chatbot.db
└── README.md
```

## Requirements

Recommended environment:

* Python 3.12+
* pip
* Virtual environment
* Xkiro/OpenAI-compatible API key

SQLAlchemy should be a recent 2.x release.

## Installation

Clone the project and enter the backend directory:

```bash
cd backend
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\activate
```

Activate it on Linux/macOS:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create:

```text
backend/.env
```

Example:

```env
XKIRO_OPENAI_API_KEY=your_api_key_here
BASE_URL=https://api.xkiro.com/v1
MODEL_NAME=gpt-4o-mini
DATABASE_URL=sqlite:///./chatbot.db
```

Do not commit `.env` to Git.

## Running the Server

Start FastAPI:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://localhost:8000
```

Swagger API documentation:

```text
http://localhost:8000/docs
```

ReDoc:

```text
http://localhost:8000/redoc
```

Health check:

```text
http://localhost:8000/health
```

## API Endpoints

### Health

```http
GET /health
```

Example:

```json
{
  "status": "healthy"
}
```

### Send Chat Message

```http
POST /api/chat
```

Request:

```json
{
  "message": "Explain FastAPI",
  "conversation_id": "optional-id",
  "model": "gpt-4o-mini"
}
```

Response:

```json
{
  "response": "FastAPI is...",
  "conversation_id": "abc-123",
  "model": "gpt-4o-mini"
}
```

### List Conversations

```http
GET /api/conversations
```

### Get Conversation

```http
GET /api/conversations/{conversation_id}
```

### Get Available Models

```http
GET /api/models
```

Example:

```json
[
  {
    "id": "gpt-4o-mini",
    "name": "GPT-4o Mini",
    "description": "Fast and efficient"
  },
  {
    "id": "gpt-4o",
    "name": "GPT-4o",
    "description": "Strong general-purpose model"
  }
]
```

## Database Model

The current database uses two main tables:

```text
conversations
----------------------------
id
title
created_at
updated_at

messages
----------------------------
id
conversation_id
role
content
created_at
```

Relationship:

```text
Conversation
     |
     +---- Message
     +---- Message
     +---- Message
```

A conversation can contain many messages.

## LLM Integration

The LLM service uses an OpenAI-compatible client:

```python
client = OpenAI(
    api_key=settings.xkiro_openai_api_key,
    base_url=settings.base_url,
)
```

The selected model is passed dynamically:

```python
generate_response(
    messages=history
)
```

This allows users to select different models from the frontend.

## CORS

The backend currently allows local frontend development:

```text
http://localhost:5173
http://127.0.0.1:5173
```

Update the configuration before production deployment.

## Development Workflow

Recommended workflow:

```text
Frontend
   |
   v
POST /api/chat
   |
   v
Chat Service
   |
   +---- Load conversation
   |
   +---- Save user message
   |
   +---- Send context to LLM
   |
   +---- Save AI response
   |
   v
Return response
```

## Error Handling

The API should return appropriate HTTP errors for:

* Invalid model
* Missing conversation
* Invalid request payload
* LLM failure
* Database failure

Example:

```json
{
  "detail": "Unsupported model: unknown-model"
}
```

## Future Roadmap

### Phase 1

* Authentication
* PostgreSQL
* Alembic migrations
* Better error handling
* Structured logging

### Phase 2

* Streaming responses
* Token usage tracking
* Message metadata
* User preferences

### Phase 3

* RAG
* Document ingestion
* Embeddings
* pgvector
* Source citations

### Phase 4

* Tool calling
* Web search
* Database tools
* API tools

### Phase 5

* Agentic AI
* Agent orchestrator
* Research agent
* Coding agent
* Planning agent
* Memory

### Phase 6

* Docker
* AWS deployment
* CI/CD
* Observability
* Evaluation
* Production security

## Testing

Run tests with:

```bash
pytest
```

Recommended future test structure:

```text
tests/
├── test_chat.py
├── test_conversations.py
├── test_models.py
└── test_services.py
```

## Security

Never commit:

```text
.env
API keys
database credentials
production secrets
```

For production:

* Use secret management
* Add authentication
* Add rate limiting
* Validate all inputs
* Restrict CORS origins
* Add request logging
* Protect internal tools
* Add prompt-injection defenses

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

See the [LICENSE](LICENSE) file for the complete license text.
