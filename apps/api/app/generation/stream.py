"""The chat endpoint's engine: retrieve -> prompt -> stream -> cite -> persist."""
from collections.abc import AsyncIterator
from uuid import UUID


def sse_event(event: str, data: dict) -> str:
    """TODO(M4): format one Server-Sent Event: f"event: {event}\\ndata: {json}\\n\\n"."""
    raise NotImplementedError


async def answer_stream(org_id: UUID, user_id: UUID, conversation_id: UUID,
                        question: str) -> AsyncIterator[str]:
    """TODO(M4): yields SSE strings in this order:

    1. save the user Message
    2. history = load_recent_history(); query = rewrite_query(...)
    3. result = retrieve(org_id, query)
    4. yield sse_event("retrieval", {"sources": [...title, pages, snippet...]})
    5. async for delta in llm.stream(build_answer_messages(...)):
           yield sse_event("token", {"text": delta})
    6. citations = extract_citations(full_answer, result.chunks)
       yield sse_event("citations", {...})
    7. persist assistant Message + Citations + RetrievalTrace (latency, tokens, prompt_version)
       yield sse_event("done", {"message_id": ..., "latency_ms": ...})

    On exception: yield sse_event("error", {"message": "..."}) and log it.
    On client disconnect (asyncio.CancelledError): save the partial answer, then re-raise.
    """
    raise NotImplementedError
    yield ""  # pragma: no cover
