"""FastAPI dependencies: the tenancy boundary of the whole app.

Every org-scoped route declares `membership: Membership = Depends(get_membership)`
and passes `membership.org_id` into every query. No exceptions.
"""
from collections.abc import Callable
from uuid import UUID

from fastapi import Request
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Membership, User


async def get_current_user(request: Request, session: AsyncSession) -> User:
    """TODO(M1): read `Authorization: Bearer <token>`, decode_token(..., 'access'),
    load the user, 401 if missing. (Wire `session` with Depends(get_session).)"""
    raise NotImplementedError


async def get_membership(org_id: UUID, user: User, session: AsyncSession) -> Membership:
    """TODO(M1): return the user's membership in `org_id` (taken from the URL path).

    Return **404, not 403**, when the user isn't a member: don't reveal that the
    org exists. Your cross-tenant test relies on this.
    """
    raise NotImplementedError


def require_role(*roles: str) -> Callable:
    """TODO(M1): dependency factory. `Depends(require_role("owner", "admin"))`
    wraps get_membership and raises 403 if membership.role not in roles."""
    raise NotImplementedError
