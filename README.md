# ChatRapper — RAG Chatbot over Brazilian Rap

Chatbot that answers natural-language questions about Brazilian rap ("rap nacional") lyrics using **Retrieval-Augmented Generation orchestrated with LangGraph**. Evolution of [sabotage-similarity](https://github.com/capella-marcosfilipe/sabotage-similarity): from semantic search to a conversational assistant with memory.

Team project for an AI course at UNICAP (assignment 3), with Elcio José Ferreira da Silva, Elynne Silva de Lima and Maria Gabrielle Silva de Melo. Professor: Iago Richard Rodrigues Silva.

## How it works

```text
Scrapy ──▶ raw lyrics ──▶ chunks ──▶ embeddings ──▶ FAISS index
                                                        │
User question ──▶ LangGraph: retrieve ──▶ build prompt (chunks + chat history) ──▶ LLM ──▶ answer
```

- **Knowledge base:** lyrics crawled with Scrapy, chunked and indexed with **FAISS**.
- **Orchestration:** a LangGraph graph with nodes for question intake, context retrieval, prompt assembly, LLM call and response.
- **Generation:** external LLM via the **Hugging Face** Inference API (default `Qwen/Qwen2.5-Coder-32B-Instruct`), used only in the generation step — no ready-made chatbot API.
- **Interface:** Next.js / React chat UI talking to a Python backend.

| Folder | Content |
|---|---|
| `scraper/` | Scrapy spider for the lyrics |
| `scripts/` | Chunking and index building |
| `data/` | Raw lyrics, chunks, FAISS index |
| `backend/` | Python API with the LangGraph graph (`graph/`), routes, schemas, services |
| `frontend/` | Next.js chat interface |

## Running

Requirements: a Hugging Face token ([huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)).

```bash
echo 'HF_TOKEN="your_token"' > .env
docker compose up --build
```

- Frontend: http://localhost:3000
- Backend: http://localhost:8000/docs

Manual setup (without Docker) is described in [`INSTRUCTIONS.md`](INSTRUCTIONS.md).
