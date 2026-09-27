"""/orgs/{org_id}/admin: dashboard data. All routes require_role('owner', 'admin')."""
from fastapi import APIRouter

router = APIRouter(prefix="/orgs/{org_id}/admin", tags=["admin"])

# TODO(M6) GET /usage?days=30   -> per-day questions, tokens, est. cost, p50/p95 latency
#          (hint: percentile_cont(0.95) WITHIN GROUP (ORDER BY latency_ms))
# TODO(M6) GET /feedback        -> thumbs-down messages joined with their retrieval trace
# TODO(M6) POST /feedback/{id}/to-eval -> append a draft case to an eval dataset for review
# TODO(M6) GET /eval-runs       -> summaries for the metric-over-time chart
