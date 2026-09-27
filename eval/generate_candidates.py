"""Draft eval cases with an LLM, for YOU to review. Never add them unreviewed."""


async def draft_cases(org_slug: str, n: int, out_path: str) -> None:
    """TODO(M5):
    * sample n random chunks (stratify by document so every doc is represented)
    * ask the LLM for {question, answer, quote} where quote is a VERBATIM span of the chunk,
      and the question avoids copying the chunk's wording (paraphrase)
    * verify the quote really is in the chunk (drop otherwise)
    * write to out_path as JSONL with source="generated_unreviewed"
    Then review by hand, edit, and move good ones into datasets/ with source="generated_reviewed".
    """
    raise NotImplementedError
