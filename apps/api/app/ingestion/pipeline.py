"""Orchestrates ingestion of one document. Called by the worker."""
from uuid import UUID


async def run_ingestion(document_id: UUID) -> None:
    """TODO(M2): the whole pipeline, idempotent (safe to retry):

    1. load Document; set status='processing'
    2. bytes = storage.get(doc.storage_key)
    3. pages = get_parser(doc.mime_type).parse(bytes); doc.page_count = len(pages)
    4. pages = strip_repeated_lines(pages); normalize each page's text
    5. drafts = chunk_pages(pages, settings.chunk_tokens, settings.chunk_overlap)
    6. vectors = embed_texts(embedder, [contextual_header(...) for d in drafts])
    7. in ONE transaction: DELETE old chunks for this doc, INSERT new ones, status='ready'
    8. on any exception: status='failed', error=str(e)[:500], log with doc id, re-raise

    Log timings for each stage; they're great for the admin dashboard.
    """
    raise NotImplementedError
