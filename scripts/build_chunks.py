"""Lê data/letras_raw.json e gera data/letras_chunks.json com chunks + metadados."""
import json
from pathlib import Path

DATA_DIR    = Path(__file__).parent.parent / "data"
INPUT_FILE  = DATA_DIR / "letras_raw.json"
OUTPUT_FILE = DATA_DIR / "letras_chunks.json"

CHUNK_SIZE = 100
OVERLAP    = 20


def make_chunks(texto: str, chunk_size: int, overlap: int) -> list[str]:
    palavras = texto.split()
    chunks, inicio = [], 0
    while inicio < len(palavras):
        fim = inicio + chunk_size
        chunks.append(" ".join(palavras[inicio:fim]))
        if fim >= len(palavras):
            break
        inicio += chunk_size - overlap
    return chunks


def main():
    with open(INPUT_FILE, encoding="utf-8") as f:
        letras = json.load(f)

    print(f"Letras carregadas: {len(letras)}")

    todos_chunks = []
    chunk_id = 0

    for musica in letras:
        chunks = make_chunks(musica["letra"], CHUNK_SIZE, OVERLAP)
        for i, chunk in enumerate(chunks):
            todos_chunks.append({
                "chunk_id":    chunk_id,
                "chunk_index": i,
                "artista":     musica["artista"],
                "titulo":      musica["titulo"],
                "url":         musica["url"],
                "texto":       chunk,
            })
            chunk_id += 1

        print(f"  [{musica['artista']}] '{musica['titulo']}': {len(chunks)} chunks")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(todos_chunks, f, ensure_ascii=False, indent=2)

    print(f"\nTotal de chunks: {chunk_id}")
    print(f"Salvo em: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()