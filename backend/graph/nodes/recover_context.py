"""Node 1: busca os chunks mais relevantes para a pergunta atual."""
from graph.state import State
from services.retriever_service import retrieve_chunks


def recover_context(state: State) -> dict:
    """Busca os chunks mais relevantes para a pergunta atual."""
    chunks = retrieve_chunks(query=state["mensagem"], top_k=5)
    return {"chunks": chunks}
