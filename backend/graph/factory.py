from langgraph.graph import StateGraph, END

from graph.state import State
from graph.nodes import recover_context, build_prompt, call_llm


def build_graph():
    """Constrói e compila o grafo de conversação."""
    graph = StateGraph(State)

    graph.add_node("recuperar_contexto", recover_context)
    graph.add_node("montar_prompt", build_prompt)
    graph.add_node("chamar_llm", call_llm)

    graph.set_entry_point("recuperar_contexto")
    graph.add_edge("recuperar_contexto", "montar_prompt")
    graph.add_edge("montar_prompt", "chamar_llm")
    graph.add_edge("chamar_llm", END)

    return graph.compile()


# Instância compilada — importada onde for necessário.
app_graph = build_graph()
