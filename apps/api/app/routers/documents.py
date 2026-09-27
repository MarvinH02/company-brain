"""/orgs/{org_id}/documents: upload, list, get, delete, re-ingest."""
from fastapi import APIRouter

router = APIRouter(prefix="/orgs/{org_id}/documents", tags=["documents"])

# TODO(M2) POST ""  (multipart UploadFile)
#   1. reject > settings.max_upload_mb; sniff MIME from bytes, not the filename
#   2. sha256 while streaming; if (org_id, checksum) exists -> return existing doc (409 or 200)
#   3. storage.put(f"{org_id}/{doc_id}/{filename}", ...)
#   4. insert Document(status='pending'); enqueue ingest_document(doc_id) via arq
#   5. return 202 + DocumentOut
# TODO(M2) GET ""                -> list with chunk_count (one query, GROUP BY; no N+1)
# TODO(M2) GET "/{doc_id}"       -> detail
# TODO(M2) GET "/{doc_id}/file"  -> short-lived presigned URL for the PDF viewer
# TODO(M6) DELETE "/{doc_id}"    -> admin; delete chunks, file, cache keys
# TODO(M6) POST "/{doc_id}/reingest" -> admin; re-enqueue (pipeline must be idempotent)
