// Streaming client for POST /orgs/{org}/conversations/{id}/messages.
// EventSource can't send a POST body or auth header, so parse SSE from fetch() yourself.

export type StreamEvent =
  | { event: "retrieval"; data: { sources: unknown[] } }
  | { event: "token"; data: { text: string } }
  | { event: "citations"; data: { citations: unknown[] } }
  | { event: "done"; data: { message_id: string; latency_ms: number } }
  | { event: "error"; data: { message: string } };

/**
 * TODO(M4):
 * - fetch with method POST, JSON body, auth header, signal
 * - res.body.getReader() + TextDecoder; buffer text; split on "\n\n"
 * - each block: lines "event: x" and "data: {...}" -> JSON.parse -> yield StreamEvent
 * - keep the incomplete tail in the buffer for the next read
 */
export async function* streamAnswer(
  orgId: string,
  conversationId: string,
  content: string,
  signal?: AbortSignal,
): AsyncGenerator<StreamEvent> {
  throw new Error(`TODO(M4): stream ${orgId}/${conversationId}: ${content} ${signal}`);
}
