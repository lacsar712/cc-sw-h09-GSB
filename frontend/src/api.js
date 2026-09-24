export async function api(path, opts = {}) {
  const token = localStorage.getItem('tok') || ''
  const headers = { 'Content-Type': 'application/json', ...(opts.headers || {}) }
  if (token) headers.Authorization = 'Bearer ' + token
  let body = opts.body
  if (path === '/api/jobs' && (opts.method || 'GET').toUpperCase() === 'POST' && body) {
    try {
      const o = JSON.parse(body)
      if (!String(o.lamp || '').trim()) o.lamp = '系统灯种'
      body = JSON.stringify(o)
    } catch {}
  }
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
