// TODO(M1): in-memory access token store + React context (AuthProvider, useAuth).
// Why not localStorage: any XSS could read it. Memory + httpOnly refresh cookie is safer.
export {};
