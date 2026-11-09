import { afterEach, expect, test, vi } from 'vitest';
import { checkReadiness } from './client';

afterEach(() => vi.unstubAllGlobals());

test('readiness must come from a successful real response', async () => {
  vi.stubGlobal('fetch', vi.fn().mockResolvedValue(new Response('{"status":"ready"}')));
  await expect(checkReadiness('http://localhost:8000')).resolves.toBeUndefined();
});

test.each([
  new Response('{}', { status: 503 }),
  new Response('{"status":"ok"}'),
  new Response('bad-json'),
])('never promotes failure or stale payload to ready', async (response) => {
  vi.stubGlobal('fetch', vi.fn().mockResolvedValue(response));
  await expect(checkReadiness('http://localhost:8000')).rejects.toThrow();
});

test('network failure stays failed', async () => {
  vi.stubGlobal('fetch', vi.fn().mockRejectedValue(new TypeError('offline')));
  await expect(checkReadiness('http://localhost:8000')).rejects.toThrow('offline');
});
