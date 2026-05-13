from pydantic import BaseModel


class Message(BaseModel):
    """Represents a message in the conversation history."""
    role: str     # "user" or "assistant"
    content: str


class ChatRequest(BaseModel):
    """Chat request sent by the client."""
    mensagem: str
    historico: list[Message] = []


class ChatResponse(BaseModel):
    """Response returned by the chatbot."""
    resposta: str
    chunks_usados: list[dict] = []
