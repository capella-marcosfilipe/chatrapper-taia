# Instruções para Build da Aplicação

## Pré-requisitos

- Python 3.10+ instalado
- Node.js 18+ e npm instalados
- Git instalado
- Token da HuggingFace (obtenha em <https://huggingface.co/settings/tokens>)
- **Docker e Docker Compose** (opcional, para subir tudo de uma vez — veja a seção Docker abaixo)

## Passo a Passo para Execução (Manual)

### 1. Clone o repositório

```bash
git clone <url-do-repositorio>
cd av-03-chatbot-com-rag-e-langgraph-sabotageai
```

### 2. Crie um ambiente virtual (recomendado)

```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Linux/Mac
```

### 3. Instale as dependências

```bash
# Dependências gerais (inclui scraper e scripts)
pip install -r requirements.txt

# Dependências do backend
pip install -r backend/requirements.txt

# Dependências do frontend
cd frontend
npm install
cd ..
```

### 4. Configure as variáveis de ambiente

Crie um arquivo `.env` na **raiz do projeto** com o seguinte conteúdo:

```env
HF_TOKEN="seu_token_da_huggingface_aqui"
# HF_MODEL="Qwen/Qwen2.5-Coder-32B-Instruct"  # opcional, este é o default
```

> **Importante:** O arquivo `.env` deve ficar na raiz do projeto (mesmo nível deste arquivo), **não** dentro da pasta `backend/`.

### 5. Execute o servidor backend

```bash
cd backend
python main.py
```

A API estará disponível em: **<http://localhost:8000>**

Você pode testar a saúde da API acessando: <http://localhost:8000/health>

### 6. Execute o frontend

Em outro terminal, na raiz do projeto:

```bash
cd frontend
npm run dev
```

A interface web estará disponível em: **<http://localhost:3000>**

> **Nota:** O frontend faz requisições para `http://localhost:8000` por padrão. Se o backend estiver em outra porta, crie um arquivo `frontend/.env.local` com `NEXT_PUBLIC_API_URL=http://localhost:SUA_PORTA`.

---

## Estrutura do Projeto

```text
av-03-chatbot-com-rag-e-langgraph-sabotageai/
├── backend/              # API FastAPI
│   ├── main.py           # Ponto de entrada
│   ├── routes/           # Rotas (/chat, /health)
│   ├── services/         # LLM e Retriever
│   ├── graph/            # Grafo LangGraph
│   └── schemas/          # Modelos Pydantic
├── data/                 # Base de conhecimento
│   ├── letras_raw.json   # Dados brutos do scraping
│   ├── letras_chunks.json # Textos fragmentados
│   ├── faiss_index.bin   # Índice vetorial FAISS
│   └── chunks_meta.json  # Metadados dos chunks
├── scraper/              # Spider Scrapy para coleta de dados
├── scripts/              # Scripts auxiliares
│   ├── build_chunks.py   # Gera chunks a partir do raw
│   └── build_index.py    # Gera embeddings e índice FAISS
├── frontend/             # Interface web do chatbot
├── .env                  # Variáveis de ambiente (NÃO versionado)
├── .env.example          # Exemplo de .env
└── requirements.txt      # Dependências do projeto
```

---

## Base de Conhecimento

O chatbot utiliza uma base de dados de **letras de rap nacional brasileiro**. Os dados foram coletados via web scraping e processados da seguinte forma:

1. **Coleta:** Spider Scrapy coletou letras de sites especializados
2. **Fragmentação:** Textos divididos em chunks menores para recuperação
3. **Embeddings:** Geração de vetores com `sentence-transformers/all-MiniLM-L6-v2`
4. **Indexação:** Armazenamento em índice FAISS para busca por similaridade

Os dados já processados estão disponíveis na pasta `data/`.

---

## (Opcional) Rebuild da Base de Conhecimento

Caso precise reconstruir o índice vetorial:

### Gerar chunks a partir dos dados brutos

```bash
python scripts/build_chunks.py
```

### Gerar o índice FAISS

```bash
python scripts/build_index.py
```

---

## (Opcional) Executar o Scraper

Para coletar novos dados:

```bash
cd scraper
scrapy crawl rap_spider
```

Os dados brutos serão salvos em `data/letras_raw.json`.

---

## Subir com Docker (Frontend + Backend de uma vez)

Se você tem **Docker e Docker Compose** instalados, pode subir toda a aplicação com um único comando:

```bash
docker compose up --build
```

Isso irá:

1. Construir a imagem do **backend** (Python + dependências + dados)
2. Construir a imagem do **frontend** (Node.js + Next.js)
3. Iniciar ambos os serviços integrados

- **Frontend:** <http://localhost:3000>
- **Backend API:** <http://localhost:8000>
- **Health Check:** <http://localhost:8000/health>

Para derrubar os serviços:

```bash
docker compose down
```

> **Importante:** É necessário ter o arquivo `.env` na raiz do projeto com o `HF_TOKEN` configurado antes de rodar o Docker, pois o backend precisa do token para acessar a LLM.

---

## Endpoints da API

### `POST /chat`

Envia uma pergunta e recebe a resposta do chatbot.

**Request:**

```json
{
  "mensagem": "Quais são os principais temas do rap do Racionais?",
  "historico": []
}
```

**Response:**

```json
{
  "resposta": "Os Racionais MC's abordam temas como...",
  "chunks_usados": [...]
}
```

### `GET /health`

Verifica se a API está funcionando.

**Response:** `{"status": "ok"}`

---

## Tecnologias Utilizadas

### Backend

- **FastAPI** — framework web Python de alta performance
- **LangGraph** — orquestração do fluxo RAG com grafos
- **FAISS** — índice vetorial para busca por similaridade
- **Sentence Transformers** — geração de embeddings (`all-MiniLM-L6-v2`)
- **HuggingFace Inference API** — chamada da LLM (`Qwen/Qwen2.5-Coder-32B-Instruct`)
- **Pydantic** — validação de schemas
- **python-dotenv** — gerenciamento de variáveis de ambiente

### Frontend

- **Next.js 16** — framework React com App Router
- **React 19** — biblioteca de UI
- **TypeScript** — tipagem estática
- **Tailwind CSS 4** — estilização utility-first
- **PostCSS** — processamento de CSS

---
