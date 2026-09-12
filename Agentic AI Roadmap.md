# Agentic AI Engineer → FDE — Progress Tracker

Check off each box as you complete it. This follows the **Lean 4-Phase Roadmap** sequence. Click the linked resource to go straight to the material.

> Tip on GitHub: paste this file into a repo as `PROGRESS.md` or your repo's `README.md`. Checkboxes (`- [ ]`) render as clickable, persistent checkboxes on GitHub — check one and it stays checked in the file once you commit the change.

---

## Phase 1 — Foundation + First Working Agent (Months 1–2)

### Engineering foundation
- [ ] Python fundamentals (typed, OOP, async) — [Python Official Tutorial](https://docs.python.org/3/tutorial/) · [Corey Schafer's Python Playlist](https://www.youtube.com/@coreyms)
- [ ] Git & GitHub workflow — [freeCodeCamp: Git and GitHub for Beginners](https://www.youtube.com/watch?v=RGOj5yH7evk)
- [ ] SQL fundamentals — [SQLBolt (interactive)](https://sqlbolt.com/) · [Mode SQL Tutorial](https://mode.com/sql-tutorial)
- [ ] Docker basics — [Docker Official Docs — Get Started](https://docs.docker.com/get-started/) · [TechWorld with Nana: Docker Tutorial](https://www.youtube.com/watch?v=3c-iBn73dDE)
- [ ] FastAPI basics (routing, validation, async) — [FastAPI Official Docs](https://fastapi.tiangolo.com/)
- [ ] Build: dockerized CRUD API + Postgres + tests + CI — *(your own repo)*

### LLM & Claude API fundamentals
- [ ] Claude API basics (messages, streaming, system prompts) — [Claude API Docs](https://docs.claude.com/en/docs/overview)
- [ ] Anthropic Academy — *Claude 101* + *Building with the Claude API* — [Anthropic Academy / anthropic.com/learn](https://www.anthropic.com/learn)
- [ ] Prompt engineering fundamentals — [Anthropic Prompt Engineering Interactive Tutorial (GitHub)](https://github.com/anthropics/prompt-eng-interactive-tutorial)
- [ ] Structured outputs with Pydantic — [Pydantic Docs](https://docs.pydantic.dev/latest/)
- [ ] How LLMs actually work (conceptual depth) — [Andrej Karpathy: "Deep Dive into LLMs like ChatGPT" (YouTube)](https://www.youtube.com/watch?v=7xTGNNLPyMI) · [3Blue1Brown: Transformers, visually explained](https://www.youtube.com/watch?v=wjZofJX0v4M)
- [ ] Build: LLM API wrapper service with retries, cost logging, streaming — *(your own repo)*

### First agent (no framework)
- [ ] Claude tool use / function calling — [Claude Tool Use Docs](https://docs.claude.com/en/docs/agents-and-tools/tool-use/overview)
- [ ] Anthropic Cookbook — tool use recipes — [anthropics/anthropic-cookbook (GitHub)](https://github.com/anthropics/anthropic-cookbook)
- [ ] **Build: raw agent loop from scratch, no framework, 3+ tools, error handling, max-iteration guard** — *(your own repo — this is the single most important checkbox in Phase 1)*

**Phase 1 exit criteria:** ☐ I can build a working 3-tool agent with error handling in under a day, with zero framework.

---

## Phase 2 — RAG, One Framework, Real Evaluation (Months 2–4)

### RAG fundamentals
- [ ] Embeddings & vector similarity concepts — [Pinecone Learning Center](https://www.pinecone.io/learn/)
- [ ] Build basic RAG from scratch (embed, cosine similarity, top-k, no vector DB abstraction) — *(your own repo)*
- [ ] pgvector setup and usage — [pgvector (GitHub)](https://github.com/pgvector/pgvector)
- [ ] DeepLearning.AI: *Building and Evaluating Advanced RAG Applications* — [DeepLearning.AI Short Courses](https://www.deeplearning.ai/short-courses/)
- [ ] DeepLearning.AI: *LangChain for LLM Application Development* — [DeepLearning.AI Short Courses](https://www.deeplearning.ai/short-courses/)

### Framework depth (LangGraph — pick one)
- [ ] LangGraph fundamentals (state, nodes, conditional edges) — [LangGraph Official Docs](https://langchain-ai.github.io/langgraph/)
- [ ] DeepLearning.AI: *AI Agents in LangGraph* (Harrison Chase) — [Course Link](https://www.deeplearning.ai/short-courses/ai-agents-in-langgraph/)
- [ ] LangChain Academy (structured, includes memory/multi-agent modules) — [academy.langchain.com](https://academy.langchain.com/)
- [ ] Rebuild your Phase-1 raw agent loop in LangGraph and compare — *(your own repo)*

### Evaluation & tracing (build before your second agent)
- [ ] Build a 20–30 example golden dataset for your RAG agent — *(your own repo)*
- [ ] Write an LLM-as-judge evaluation script — [openai/evals (GitHub, concepts transfer across providers)](https://github.com/openai/evals) · [confident-ai/deepeval (GitHub)](https://github.com/confident-ai/deepeval)
- [ ] Set up Langfuse tracing (self-hosted, free) on every agent going forward — [langfuse/langfuse (GitHub)](https://github.com/langfuse/langfuse) · [Langfuse Docs](https://langfuse.com/docs)
- [ ] Read: "Your AI product needs evals" — [Hamel Husain's blog](https://hamel.dev/blog/posts/evals/)

**Phase 2 exit criteria:** ☐ I have one RAG-backed agent with tracing and a real eval suite that would catch a regression.

---

## Phase 3 — Multi-Agent, MCP, Production — ONE Real Project (Months 4–6)

*(Pick ONE project below — don't do all three)*
- [ ] Project chosen: ☐ Enterprise knowledge assistant  ☐ Customer support agent  ☐ Data analyst agent (NL-to-SQL)

### Multi-agent (add only once the project needs it)
- [ ] Router/supervisor pattern — [LangGraph multi-agent examples](https://langchain-ai.github.io/langgraph/tutorials/multi_agent/multi_agent_collaboration/)
- [ ] ReAct pattern (paper) — [ReAct: Synergizing Reasoning and Acting in Language Models (arXiv)](https://arxiv.org/abs/2210.03629)
- [ ] Reflection pattern (paper) — [Reflexion: Language Agents with Verbal Reinforcement Learning (arXiv)](https://arxiv.org/abs/2303.11366)

### MCP
- [ ] MCP core concepts — [Model Context Protocol Official Spec/Docs](https://modelcontextprotocol.io/)
- [ ] Anthropic Academy: *Introduction to MCP* + *MCP Advanced Topics* — [anthropic.com/learn](https://www.anthropic.com/learn)
- [ ] DeepLearning.AI: *MCP: Build Rich-Context AI Apps with Anthropic* — [DeepLearning.AI Short Courses](https://www.deeplearning.ai/short-courses/)
- [ ] Reference MCP servers — [modelcontextprotocol/servers (GitHub)](https://github.com/modelcontextprotocol/servers)
- [ ] Browse community MCP servers for examples — [awesome-mcp-servers (GitHub)](https://github.com/punkpeye/awesome-mcp-servers)
- [ ] **Build: one real MCP server wrapping your database or a real API** — *(your own repo)*

### Deployment & production hardening
- [ ] FastAPI deployment on AWS (ECS or Lambda) — [AWS Lambda Docs](https://docs.aws.amazon.com/lambda/) · [AWS ECS Docs](https://docs.aws.amazon.com/ecs/)
- [ ] RDS/Postgres + pgvector in production — [AWS RDS Docs](https://docs.aws.amazon.com/rds/)
- [ ] CI/CD pipeline (lint, test, deploy) — [GitHub Actions Docs](https://docs.github.com/en/actions)
- [ ] Wire your eval suite into CI as a regression gate — *(your own repo)*
- [ ] **Deliberately introduce a regression and confirm your CI gate catches it** — *(your own repo)*
- [ ] AWS Free Tier account set up — [AWS Free Tier](https://aws.amazon.com/free/)

**Phase 3 exit criteria:** ☐ I have one deployed, evaluated, documented project I could demo live and defend under questioning.

---

## Phase 4 — FDE Reps + Positioning (Months 6–9)

### Discovery & scoping practice
- [ ] Run mock discovery exercise #1 (vague problem → spec in 2 hrs → demo slice in 2 days)
- [ ] Run mock discovery exercise #2
- [ ] Run mock discovery exercise #3
- [ ] Run mock discovery exercise #4 *(optional)*
- [ ] Run mock discovery exercise #5 *(optional)*
- [ ] Study FDE methodology — [Palantir Forward Deployed Engineer talks/interviews (YouTube — search)](https://www.youtube.com/results?search_query=palantir+forward+deployed+engineer) · [Pragmatic Engineer Newsletter](https://newsletter.pragmaticengineer.com/)
- [ ] Study customer discovery methodology — [Y Combinator YouTube Channel](https://www.youtube.com/@ycombinator)

### Portfolio & positioning
- [ ] Rewrite Phase 3 project README as a customer-facing pitch (problem, architecture, trade-offs, impact)
- [ ] Pin exactly 3 repos: raw agent loop / RAG+eval project / production project
- [ ] Write resume headline + LinkedIn headline + About section
- [ ] Write 30-second and 2-minute self-introductions

### Interview prep (concentrated, not exhaustive)
- [ ] Rehearse 3–5 FDE case-study answers (discovery → scoped build → measured impact)
- [ ] Review system design fundamentals — [ByteByteGo (YouTube)](https://www.youtube.com/@ByteByteGo) · [system-design-primer (GitHub)](https://github.com/donnemartin/system-design-primer)
- [ ] Mock interview: agent architecture trade-off questions
- [ ] Mock interview: cold ambiguous customer-problem scoping, out loud, under 15 minutes

**Phase 4 exit criteria:** ☐ I can take a cold, ambiguous customer problem live and produce a credible scoped approach in under 15 minutes.

---

## Ongoing / Cross-Cutting (check periodically, not once)

- [ ] Subscribed to one newsletter — [The Batch (deeplearning.ai)](https://www.deeplearning.ai/the-batch/) or [Latent Space](https://www.latent.space/)
- [ ] Joined one community — [r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/) or Anthropic Developer Discord (linked from [docs.claude.com](https://docs.claude.com))
- [ ] Reviewed official docs directly at least once this month (not just blog summaries) — [docs.claude.com](https://docs.claude.com) · [modelcontextprotocol.io](https://modelcontextprotocol.io) · [langchain-ai.github.io/langgraph](https://langchain-ai.github.io/langgraph/)

---

## Reference-only (dip in when a specific job needs it — not sequential)

- [ ] Kubernetes — [TechWorld with Nana: Kubernetes Tutorial (YouTube)](https://www.youtube.com/watch?v=X48VuDVv0do) · [Kubernetes Official Docs](https://kubernetes.io/docs/home/)
- [ ] Event-driven architecture (SQS/queues) — [AWS SQS Docs](https://docs.aws.amazon.com/sqs/)
- [ ] Multi-agent frameworks beyond LangGraph (CrewAI, AutoGen) — [crewAIInc/crewAI (GitHub)](https://github.com/crewAIInc/crewAI) · [microsoft/autogen (GitHub)](https://github.com/microsoft/autogen)
- [ ] Hugging Face Agents Course (broader, ~20–30 hrs, certificate) — [huggingface.co/learn/agents-course](https://huggingface.co/learn/agents-course)
- [ ] Advanced retrieval (hybrid search, reranking, graph RAG) — [Pinecone Learning Center](https://www.pinecone.io/learn/)

---

### Progress summary
Total core checkboxes (Phases 1–4, excluding optional/reference): count them as you go — GitHub renders a `x / y` completion count automatically in the repo file preview once you're checking boxes via the web UI's task-list widget on an Issue or PR; in a plain README it won't auto-count, so if you want a visible percentage, consider using a GitHub Issue instead of a README for this checklist — Issues render a live "X of Y tasks complete" progress bar.
