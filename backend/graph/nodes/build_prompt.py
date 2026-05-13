"""Node 2: monta o prompt completo para a LLM."""

from graph.state import State


def build_prompt(state: State) -> dict:
    """Monta o prompt completo para a LLM."""
    # Contexto dos chunks
    if state["chunks"]:
        contexto = "\n\n".join(
            f"[{c['artista']} — {c['titulo']}]\n{c['texto']}"
            for c in state["chunks"]
        )
    else:
        contexto = "[Nenhum trecho relevante encontrado]"

    # Histórico formatado
    historico_fmt = ""
    for msg in state["historico"][-6:]:  # últimas 6 mensagens (3 turnos)
        role = "Usuário" if msg["role"] == "user" else "Assistente"
        historico_fmt += f"{role}: {msg['content']}\n"

    prompt = f"""Você é um assistente especializado em rap nacional brasileiro.
Use apenas os trechos de letras abaixo como base para responder.
Se a resposta não estiver nos trechos, diga que não encontrou informação suficiente.

--- CONTEXTO ---
{contexto}

--- HISTÓRICO ---
{historico_fmt}
--- PERGUNTA ---
{state["mensagem"]}

--- RESPOSTA ---"""

    return {"prompt": prompt}
