export async function api(path, opts = {}) {
  const token = localStorage.getItem('tok') || ''
  const headers = { 'Content-Type': 'application/json', ...(opts.headers || {}) }
  if (token) headers.Authorization = 'Bearer ' + token
  // Never rewrite a blank lamp name here: send the payload verbatim and let
  // the server reject blank/whitespace-only names.
  const body = opts.body
  const r = await fetch(path, { ...opts, headers, body })
  const t = await r.text()
  let data = {}
  try {
    data = t ? JSON.parse(t) : {}
  } catch {
    data = { detail: t }
  }
  if (!r.ok) throw new Error(data.detail || data.message || r.statusText)
  return data
}
