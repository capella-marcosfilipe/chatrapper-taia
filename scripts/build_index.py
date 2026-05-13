"""
Lê data/letras_chunks.json, gera embeddings com sentence-transformers
e salva o índice FAISS em data/faiss_index.bin.

Uso:
    python scripts/build_index.py
"""

import json
from pathlib import Path

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

DATA_DIR    = Path(__file__).parent.parent / "data"
CHUNKS_FILE = DATA_DIR / "letras_chunks.json"
INDEX_FILE  = DATA_DIR / "faiss_index.bin"
META_FILE   = DATA_DIR / "chunks_meta.json"

MODEL_NAME  = "sentence-transformers/all-MiniLM-L6-v2"
BATCH_SIZE  = 64


def main():
    print(f"Carregando chunks de {CHUNKS_FILE}...")
    with open(CHUNKS_FILE, encoding="utf-8") as f:
        chunks = json.load(f)

    print(f"Total de chunks: {len(chunks)}")

    textos = [c["texto"] for c in chunks]

    print(f"Carregando modelo '{MODEL_NAME}'...")
    model = SentenceTransformer(MODEL_NAME)

    print("Gerando embeddings...")
    embeddings = model.encode(
        textos,
        batch_size=BATCH_SIZE,
        show_progress_bar=True,
    )

    embeddings = np.array(embeddings, dtype="float32")
    dim = embeddings.shape[1]
    print(f"Embeddings gerados: {embeddings.shape}")

    # IndexFlatIP com vetores normalizados = cosine similarity
    index = faiss.IndexFlatIP(dim)
    index.add(x=embeddings) # type: ignore
    print(f"Índice FAISS criado com {index.ntotal} vetores.")

    faiss.write_index(index, str(INDEX_FILE))
    print(f"Índice salvo em: {INDEX_FILE}")

    # Salva metadados separados (texto, artista, titulo, url)
    meta = [
        {
            "chunk_id":    c["chunk_id"],
            "artista":     c["artista"],
            "titulo":      c["titulo"],
            "url":         c["url"],
            "texto":       c["texto"],
        }
        for c in chunks
    ]
    with open(META_FILE, "w", encoding="utf-8") as f:
        json.dump(meta, f, ensure_ascii=False, indent=2)
    print(f"Metadados salvos em: {META_FILE}")


if __name__ == "__main__":
    main()