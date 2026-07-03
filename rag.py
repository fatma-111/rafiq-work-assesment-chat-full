 ---------------------------------------------------------------------------
# RAG SERVICES
# ---------------------------------------------------------------------------
EMBEDDING_MODEL = "models/text-embedding-004"
EMBEDDING_DIM = 768
from typing import List
from fastapi import HTTPException
EMBEDDING_MODEL = "text-embedding-004"   # ← remove "models/" prefix
EMBEDDING_DIM   = 768

def generate_embedding(text: str) -> List[float]:
    if not text:
        raise HTTPException(status_code=400, detail="Empty text")

    if not GEMINI_ENABLED or client is None:
        raise HTTPException(status_code=503, detail="Gemini disabled: set GEMINI_API_KEY")
    try:
        result = client.models.embed_content(
            model=EMBEDDING_MODEL,
            contents=text
            contents=text,
        )

        return result.embeddings[0].values

        # google-genai SDK ≥ 0.8 returns EmbedContentResponse
        # .embeddings is a list of ContentEmbedding; each has .values
        embedding = result.embeddings[0].values
        return embedding
    except HTTPException:
        raise
    except Exception as exc:
        raise HTTPException(
            status_code=502,
            detail=f"Embedding generation failed: {exc}"
            detail=f"Embedding generation failed: {exc}",
        )

def ensure_faq_kb_table(conn) -> None:
    """Ensure the faq_knowledge_base table and pgvector extension exist."""
    cur = conn.cursor()
