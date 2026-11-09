import React, { useEffect, useRef, useState } from 'react';
import { createRoot } from 'react-dom/client';
import { checkReadiness } from './api/client';
import './tokens.css';
import './style.css';

type State = 'empty' | 'loading' | 'ready' | 'unavailable';
const messages: Record<State, string> = {
  empty: 'No business tools are available at this stage.',
  loading: 'Checking the service…',
  ready: 'The service and database are ready. Business tools will follow in later stages.',
  unavailable: 'Could not confirm service readiness. Check the API configuration and try again.',
};

function Foundation() {
  const [state, setState] = useState<State>('empty');
  const active = useRef<AbortController | null>(null);
  useEffect(() => () => active.current?.abort(), []);
  async function check() {
    if (active.current) return;
    const controller = new AbortController();
    active.current = controller;
    setState('loading');
    try {
      const baseUrl = import.meta.env.VITE_API_BASE_URL ??
        (import.meta.env.PROD ? 'https://api.romear.invalid' : 'http://localhost:8000');
      if (import.meta.env.PROD && !baseUrl.startsWith('https://')) {
        throw new Error('Production requires HTTPS');
      }
      await checkReadiness(baseUrl,
        AbortSignal.any([controller.signal, AbortSignal.timeout(10_000)]));
      if (!controller.signal.aborted) setState('ready');
    } catch {
      if (!controller.signal.aborted) setState('unavailable');
    } finally {
      active.current = null;
    }
  }
  return <main>
    <header><a href="/" aria-label="ROMEAR Business home">ROMEAR <span>Business</span></a></header>
    <section aria-labelledby="title">
      <p className="eyebrow">Built around your city</p>
      <h1 id="title">Good places.<br />Shared experiences.</h1>
      <p>The foundation for club, venue and platform management. Starting in Nagpur.</p>
      <div className="status" role="status" aria-live="polite" aria-busy={state === 'loading'}>
        {messages[state]}
      </div>
      <button onClick={check} disabled={state === 'loading'}>Check connection</button>
      <p className="note">Stage 00 · No accounts, bookings, payments or management actions yet.</p>
    </section>
  </main>;
}

createRoot(document.getElementById('root')!).render(<React.StrictMode><Foundation /></React.StrictMode>);
