"""Password hashing and JWT helpers."""
from datetime import timedelta
from uuid import UUID


def hash_password(plain: str) -> str:
    """TODO(M1): hash with argon2 (pwdlib). Never store or log the plain password."""
    raise NotImplementedError


def verify_password(plain: str, hashed: str) -> bool:
    """TODO(M1): constant-time verify via pwdlib."""
    raise NotImplementedError


def create_access_token(user_id: UUID, expires: timedelta | None = None) -> str:
    """TODO(M1): signed JWT with claims sub=user_id, type='access', exp, iat.

    Short-lived (settings.access_token_minutes). Algorithm HS256 is fine here.
    """
    raise NotImplementedError


def create_refresh_token(user_id: UUID) -> str:
    """TODO(M1): like the access token but type='refresh' and a longer expiry.

    Stretch: store a hash of it (or a jti) so refresh tokens can be revoked.
    """
    raise NotImplementedError


def decode_token(token: str, expected_type: str) -> UUID:
    """TODO(M1): verify signature + expiry + type, return the user id.

    Raise a 401 HTTPException on any failure; don't leak which check failed.
    """
    raise NotImplementedError


def create_invite_token() -> tuple[str, str]:
    """TODO(M1): return (raw_token, sha256_hex). Email/show the raw one, store only the hash."""
    raise NotImplementedError
