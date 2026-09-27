"""LLM-as-judge for answer quality."""
from dataclasses import dataclass

from app.providers.base import LLMProvider


@dataclass
class Judgement:
    correctness: int      # 1-5
    faithful: bool
    abstained: bool
    reason: str


async def judge_answer(llm: LLMProvider, question: str, reference: str | None,
                       answer: str, sources: list[str], prompt_version: str = "judge_v1"
                       ) -> Judgement:
    """TODO(M5): fill eval/prompts/{prompt_version}.txt, call llm.complete(json_mode=True,
    temperature=0), parse + validate JSON (retry once on malformed output).

    For unanswerable cases (reference is None): correctness is 5 if abstained else 1.
    """
    raise NotImplementedError


async def check_citation(llm: LLMProvider, sentence: str, chunk_text: str) -> bool:
    """TODO(M5, stretch): does `chunk_text` support `sentence`? -> citation precision."""
    raise NotImplementedError
