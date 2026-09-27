"""/orgs: create/list workspaces, members, invites."""
from fastapi import APIRouter

router = APIRouter(prefix="/orgs", tags=["orgs"])

# TODO(M1) POST /orgs                               -> creator becomes 'owner'
# TODO(M1) GET  /orgs                               -> orgs the user belongs to
# TODO(M1) GET  /orgs/{org_id}/members              -> any member
# TODO(M1) POST /orgs/{org_id}/invites              -> admin/owner; returns invite link
# TODO(M1) POST /invites/{token}/accept             -> logged-in user joins the org
# TODO(M6) PATCH/DELETE /orgs/{org_id}/members/{user_id} -> admin/owner; never remove last owner
