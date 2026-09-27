"""The most important test in the repo (M1+). Extend the route list as you add routes.

For every org-scoped route: a member of org B requesting org A's resource gets 404.
"""
import pytest

ORG_SCOPED_ROUTES = [
    ("GET", "/orgs/{org}/members"),
    ("GET", "/orgs/{org}/documents"),
    # TODO(M2+): ("GET", "/orgs/{org}/documents/{doc}"), search, conversations, admin ...
]


@pytest.mark.skip(reason="TODO(M1): implement client/user/org fixtures in conftest.py")
@pytest.mark.parametrize("method,path", ORG_SCOPED_ROUTES)
async def test_cross_tenant_access_is_404(method, path):
    """TODO(M1): create org A (with data) and user B in org B only; call the route
    for org A with B's token; assert status == 404."""
