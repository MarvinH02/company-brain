"""/auth: signup, login, refresh, logout, me."""
from fastapi import APIRouter

router = APIRouter(prefix="/auth", tags=["auth"])

# TODO(M1) POST /auth/signup  -> create user (email lowercased, unique), return TokenOut
# TODO(M1) POST /auth/login   -> verify password; access token in body,
#                                refresh token in an httpOnly, Secure, SameSite=Lax cookie
# TODO(M1) POST /auth/refresh -> read cookie, issue new access token (rotate refresh)
# TODO(M1) POST /auth/logout  -> clear cookie
# TODO(M1) GET  /auth/me      -> UserOut + list of memberships (for the org switcher)
# Hint: rate-limit login by IP + email once M6 ratelimit exists.
