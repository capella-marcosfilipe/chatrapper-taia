from fastapi import APIRouter, HTTPException

from graph import app_graph
from schemas import ChatRequest, ChatResponse

router = APIRouter(prefix="/chat", tags=["chat"])


@router.post("/", response_model=ChatResponse)
def chat(req: ChatRequest):
    """Processa a pergunta do usuário e retorna a resposta do chatbot."""
    try:
        resultado = app_graph.invoke({
            "mensagem": req.mensagem,
            "historico": [m.model_dump() for m in req.historico],
            "chunks": [],
            "prompt": "",
            "resposta": "",
        })
        return ChatResponse(
            resposta=resultado["resposta"],
            chunks_usados=resultado.get("chunks", []),
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
