"""Redis-backed rate limiting."""


async def check_rate_limit(key: str, limit: int, window_seconds: int) -> None:
    """TODO(M6): raise HTTP 429 (with Retry-After) if `key` exceeded `limit` in the window.

    Simple version: INCR + EXPIRE on f"rl:{key}:{window_start}" (fixed window).
    Better: sliding window with a sorted set (ZADD now, ZREMRANGEBYSCORE old, ZCARD).
    Use keys like f"user:{user_id}:ask" and f"org:{org_id}:ask".
    """
    raise NotImplementedError
