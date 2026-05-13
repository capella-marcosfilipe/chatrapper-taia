import json
from pathlib import Path

import faiss
from sentence_transformers import SentenceTransformer

DATA_DIR   = Path(__file__).parent.parent.parent / "data"
INDEX_FILE = DATA_DIR / "faiss_index.bin"
META_FILE  = DATA_DIR / "chunks_meta.json"
MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

print("[retriever] Carregando modelo de embeddings...")
_model = SentenceTransformer(MODEL_NAME)

print("[retriever] Carregando índice FAISS...")
_index = faiss.read_index(str(INDEX_FILE))

print("[retriever] Carregando metadados...")
with open(META_FILE, encoding="utf-8") as f:
    _meta: list[dict] = json.load(f)

print(f"[retriever] Pronto. {_index.ntotal} vetores no índice.")


def retrieve_chunks(query: str, top_k: int = 5) -> list[dict]:
    """
    Busca os chunks mais similares à query.

    Retorna:
        [
            {
                "texto":   "...",
                "titulo":  "...",
                "artista": "...",
                "url":     "...",
                "score":   0.87,
            },
            ...
        ]
    """
    vetor = _model.encode(
        [query],
        normalize_embeddings=True,
        convert_to_numpy=True,
    ).astype("float32")

    scores, indices = _index.search(vetor, top_k)

    resultados = []
    for score, idx in zip(scores[0], indices[0]):
        if idx == -1:
            continue
        item = _meta[idx].copy()
        item["score"] = round(float(score), 4)
        resultados.append(item)

    return resultados