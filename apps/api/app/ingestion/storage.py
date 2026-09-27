"""Object storage (MinIO locally, S3 in prod; GCS/Azure have S3-compatible or similar APIs)."""
from typing import BinaryIO, Protocol


class Storage(Protocol):
    def put(self, key: str, fileobj: BinaryIO, content_type: str) -> None: ...
    def get(self, key: str) -> bytes: ...
    def delete(self, key: str) -> None: ...
    def presigned_url(self, key: str, expires_seconds: int = 300) -> str: ...


class S3Storage:
    """TODO(M2): implement Storage with boto3 (endpoint_url=settings.s3_endpoint_url
    for MinIO). Create the bucket on startup if missing (dev only)."""
