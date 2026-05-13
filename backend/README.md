# Backend — Chatbot de Rap Nacional com RAG

Backend da API do chatbot, desenvolvido como atividade acadêmica. Implementa um chatbot com **RAG (Retrieval-Augmented Generation)** usando **LangGraph** para orquestrar o fluxo de recuperação de contexto e geração de respostas sobre rap nacional brasileiro.

## Tecnologias utilizadas

- **FastAPI** — framework web assíncrono para construção da API
- **LangGraph** — orquestração do fluxo de RAG em grafo (3 nós: recuperar contexto → montar prompt → chamar LLM)
- **FAISS** — busca vetorial por similaridade para recuperar trechos relevantes
- **Sentence Transformers** — geração de embeddings para as consultas
- **HuggingFace Inference API** — geração de respostas com o modelo `Qwen/Qwen2.5-Coder-32B-Instruct`
- **Pydantic** — validação de schemas de entrada e saída
- **python-dotenv** — gerenciamento de variáveis de ambiente

## Endpoint

### `POST /chat`

Processa a pergunta do usuário e retorna a resposta do chatbot.

**Entrada (JSON):**

```json
{
  "mensagem": "Quais são os principais temas do rap do Racionais?",
  "historico": [
    { "role": "user", "content": "Oi, quero saber sobre rap nacional" },
    { "role": "assistant", "content": "Claro! Sobre o que você gostaria de saber?" }
  ]
}
```

| Campo | Tipo | Obrigatório | Descrição |
|---|---|---|---|
| `mensagem` | `str` | Sim | Pergunta atual do usuário |
| `historico` | `list[Message]` | Não | Histórico da conversa (`role`: `"user"` ou `"assistant"`, `content`: texto da mensagem) |

**Saída (JSON):**

```json
{
  "resposta": "Os Racionais MC's abordam temas como...",
  "chunks_usados": [
    {
      "texto": "Trecho da letra...",
      "titulo": "Nome da música",
      "artista": "Nome do artista",
      "url": "https://...",
      "score": 0.87
    }
  ]
}
```

| Campo | Tipo | Descrição |
|---|---|---|
| `resposta` | `str` | Resposta gerada pela LLM |
| `chunks_usados` | `list[dict]` | Trechos de letras usados como contexto, com score de similaridade |

### `GET /health`

Verifica se a API está funcionando.

**Resposta:** `{"status": "ok"}`

## Estrutura do grafo (LangGraph)

O fluxo de RAG é organizado em 3 nós:

1. **recuperar_contexto** — Busca os 5 chunks mais relevantes no índice FAISS
2. **montar_prompt** — Monta o prompt com contexto, histórico e pergunta
3. **chamar_llm** — Envia o prompt para a HuggingFace e obtém a resposta

## Como executar

1. Instale as dependências do backend:

   ```bash
   cd backend
   pip install -r requirements.txt
   ```

2. Configure as variáveis de ambiente:
   - Crie um arquivo `.env` na **raiz do projeto** (não na pasta backend) com o seguinte conteúdo:

     ```env
     HF_TOKEN="seu_token_da_huggingface"
     # HF_MODEL="Qwen/Qwen2.5-Coder-32B-Instruct"  # opcional
     ```

   - Obtenha seu token em: <https://huggingface.co/settings/tokens>

3. Execute o servidor:

   ```bash
   cd backend
   python main.py
   ```

4. A API estará disponível em `http://localhost:8000`

## Estrutura de Arquivos

```text
backend/
├── main.py              # Ponto de entrada da aplicação FastAPI
├── requirements.txt     # Dependências do backend
├── routes/              # Rotas da API (chat, health)
├── services/            # Serviços (LLM, RAG, etc.)
├── schemas/             # Modelos Pydantic
└── graph/               # Grafo LangGraph
```
