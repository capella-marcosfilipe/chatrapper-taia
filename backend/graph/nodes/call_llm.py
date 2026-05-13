"""Node 3: envia o prompt para a LLM e obtém a resposta."""

from graph.state import State
from services.llm_service import generate_response


def call_llm(state: State) -> dict:
    """Envia o prompt para a LLM e obtém a resposta."""
    resposta = generate_response(state["prompt"])
    return {"resposta": resposta}
