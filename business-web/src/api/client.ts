import type { paths } from './schema';

type Ready = paths['/ready']['get']['responses'][200]['content']['application/json'];

export async function checkReadiness(baseUrl: string, signal?: AbortSignal): Promise<void> {
  const response = await fetch(`${baseUrl.replace(/\/$/, '')}/ready`, {
    signal: signal ?? AbortSignal.timeout(10_000), cache: 'no-store',
  });
  if (!response.ok) throw new Error('Service unavailable');
  const body: Ready = await response.json();
  if (body.status !== 'ready') throw new Error('Unexpected readiness response');
}
