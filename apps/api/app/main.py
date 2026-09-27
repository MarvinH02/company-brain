"""App factory."""
from fastapi import FastAPI


def create_app() -> FastAPI:
    """TODO(M1):
    * create FastAPI(title="Company Brain")
    * CORS for the web origin (credentials allowed, for the refresh cookie)
    * middleware that assigns a request_id and logs one JSON line per request
    * include routers: auth, orgs, documents, search, chat, admin
    * GET /health -> Health(db=..., redis=...) actually pinging both
    """
    raise NotImplementedError


app = create_app()
