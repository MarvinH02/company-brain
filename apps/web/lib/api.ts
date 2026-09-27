// Typed API client. Run `npm run gen:api` once the API serves /openapi.json,
// then import types from "./api-types".

const BASE = process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000";

/**
 * TODO(M1): fetch wrapper.
 * - adds Authorization: Bearer <access token> (kept in memory, see lib/auth.ts)
 * - credentials: "include" so the refresh cookie is sent to /auth/refresh
 * - on 401: call /auth/refresh once, retry the request, else redirect to /login
 * - throws a typed ApiError(status, detail) on non-2xx
 */
export async function apiFetch<T>(path: string, init?: RequestInit): Promise<T> {
  throw new Error(`TODO(M1): apiFetch ${BASE}${path} ${init?.method ?? "GET"}`);
}

// TODO(M1): login, signup, me, createOrg, listOrgs, invite
// TODO(M2): uploadDocument (FormData), listDocuments, getDocumentFileUrl
// TODO(M3): search
// TODO(M4): listConversations, getConversation, createConversation
// TODO(M6): usage, feedback, evalRuns
