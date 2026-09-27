"""/orgs/{org_id}/conversations: chat with streaming answers."""
from fastapi import APIRouter

router = APIRouter(prefix="/orgs/{org_id}/conversations", tags=["chat"])

# TODO(M4) POST ""                      -> new conversation
# TODO(M4) GET  ""                      -> user's conversations, newest first (paginate)
# TODO(M4) GET  "/{conv_id}"            -> messages + citations (check conv.user_id == user)
# TODO(M4) POST "/{conv_id}/messages"   -> StreamingResponse(text/event-stream)
#          body: MessageIn(content). Delegates to generation.stream.answer_stream(...)
# TODO(M6) POST "/{conv_id}/messages/{msg_id}/feedback" -> thumbs up/down
