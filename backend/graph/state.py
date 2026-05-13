from typing import TypedDict


class State(TypedDict):
    """Estado compartilhado entre os nós do grafo."""
    mensagem: str
    historico: list[dict]
    chunks: list[dict]
    prompt: str
    resposta: str
