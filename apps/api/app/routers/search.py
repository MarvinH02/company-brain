"""/orgs/{org_id}/search: retrieval without generation. Used by the debug view + eval."""
from fastapi import APIRouter

router = APIRouter(prefix="/orgs/{org_id}/search", tags=["search"])

# TODO(M3) POST "" SearchIn -> list[SearchHit]
#   call retrieval.service.retrieve(org_id, query, mode, k, filters)
#   save a RetrievalTrace; return hits with every per-stage score for the debug view
