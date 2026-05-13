from fastapi import APIRouter

router = APIRouter(tags=["health"])


@router.get("/health")
def health():
    """Verifica se a API está funcionando."""
    return {"status": "ok"}
