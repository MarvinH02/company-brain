"""arq worker entrypoint: `arq app.worker.WorkerSettings`."""


async def ingest_document(ctx: dict, document_id: str) -> None:
    """TODO(M2): open a DB session and call ingestion.pipeline.run_ingestion(document_id)."""
    raise NotImplementedError


async def startup(ctx: dict) -> None:
    """TODO(M2): create shared clients once (db sessionmaker, storage, embedder) and put them in ctx."""
    raise NotImplementedError


class WorkerSettings:
    # TODO(M2): redis_settings = RedisSettings.from_dsn(settings.redis_url)
    functions = [ingest_document]
    on_startup = startup
    max_tries = 3
    job_timeout = 600
