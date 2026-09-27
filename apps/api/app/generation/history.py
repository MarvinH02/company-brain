from uuid import UUID

from app.providers.base import ChatMessage, LLMProvider


async def load_recent_history(conversation_id: UUID, max_turns: int = 6) -> list[ChatMessage]:
    """TODO(M4): last `max_turns` messages, oldest first, content only (no sources)."""
    raise NotImplementedError


async def rewrite_query(llm: LLMProvider, question: str, history: list[ChatMessage]) -> str:
    """TODO(M4): if history is empty return question unchanged (skip the LLM call).
    Otherwise use prompts/rewrite_v1.txt. Retrieval uses the rewritten query."""
    raise NotImplementedError


async def generate_title(llm: LLMProvider, first_question: str) -> str:
    """TODO(M4): <= 6 words. Run it after the first answer is saved (don't delay the stream)."""
    raise NotImplementedError
