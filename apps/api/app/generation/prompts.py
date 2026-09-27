"""Prompt construction. Prompt text lives in app/prompts/*.txt, versioned by filename."""
from pathlib import Path

from app.providers.base import ChatMessage
from app.retrieval.types import ScoredChunk

PROMPT_DIR = Path(__file__).parent.parent / "prompts"


def load_prompt(version: str = "answer_v1") -> str:
    """TODO(M4): read PROMPT_DIR / f"{version}.txt"; cache it."""
    raise NotImplementedError


def format_sources(chunks: list[ScoredChunk]) -> str:
    """TODO(M4): number sources from 1, e.g.

    <source id="1" title="Employee Handbook" pages="12-13">
    ...chunk text...
    </source>

    Clear delimiters make it harder for text inside documents to pose as instructions.
    """
    raise NotImplementedError


def build_answer_messages(question: str, chunks: list[ScoredChunk],
                          history: list[ChatMessage], prompt_version: str = "answer_v1"
                          ) -> list[ChatMessage]:
    """TODO(M4): [system prompt] + recent history + a user turn containing the
    formatted sources followed by the question."""
    raise NotImplementedError
