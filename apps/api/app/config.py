"""Typed settings loaded from environment variables (.env)."""
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    database_url: str
    redis_url: str
    jwt_secret: str
    access_token_minutes: int = 15
    refresh_token_days: int = 14

    s3_endpoint_url: str | None = None
    s3_bucket: str = "documents"
    s3_access_key: str = ""
    s3_secret_key: str = ""

    llm_provider: str = "openai"
    llm_model: str = ""
    embedding_provider: str = "openai"
    embedding_model: str = ""
    embedding_dim: int = 1536
    rerank_provider: str = "none"
    rerank_model: str = ""

    chunk_tokens: int = 500
    chunk_overlap: int = 75
    retrieve_k: int = 30
    rerank_top_n: int = 6
    rrf_k: int = 60

    max_upload_mb: int = 25


def get_settings() -> Settings:
    """TODO(M1): return a cached Settings instance (hint: functools.lru_cache)."""
    raise NotImplementedError
