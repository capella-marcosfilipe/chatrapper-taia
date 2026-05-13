import os
from huggingface_hub import InferenceClient

MODEL = os.getenv("HF_MODEL", "Qwen/Qwen2.5-Coder-32B-Instruct")

_client = InferenceClient(
    model=MODEL,
    token=os.getenv("HF_TOKEN"),
)


def generate_response(prompt: str, max_tokens: int = 512) -> str:
    try:
        resposta = _client.chat_completion(
            messages=[
                {
                    "role": "system",
                    "content": (
                        "Você é um assistente especializado em rap nacional brasileiro. "
                        "Responda sempre em português, com base apenas nos trechos fornecidos."
                    ),
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
            max_tokens=max_tokens,
            temperature=0.7,
        )
        return resposta.choices[0].message.content.strip() # type: ignore

    except Exception as e:
        return f"[Erro ao chamar a LLM: {e}]"