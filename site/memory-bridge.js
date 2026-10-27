(() => {
  const ready = window.projectMemoryReady;
  if (!ready) return;
  const css = 'position:fixed;right:16px;bottom:16px;z-index:20;background:#fff;color:#18211f;border:1px solid #c8d1ca;border-radius:12px;padding:10px;box-shadow:0 8px 30px #0002;font:14px system-ui;max-width:280px';
  const panel = document.createElement('aside'); panel.style.cssText = css; panel.setAttribute('aria-label','Private work memory');
  panel.innerHTML = '<strong>Private work</strong><div data-memory-status style="margin:6px 0;opacity:.75">Checking account…</div><div style="display:flex;gap:6px;flex-wrap:wrap"><button type="button" data-memory-account>Sign in</button><button type="button" data-memory-save disabled>Save result</button><button type="button" data-memory-restore disabled>View saved work</button></div><div data-memory-list style="margin-top:8px"></div>';
  document.body.append(panel);
  const status = panel.querySelector('[data-memory-status]'), save = panel.querySelector('[data-memory-save]'), restore = panel.querySelector('[data-memory-restore]'), account = panel.querySelector('[data-memory-account]'), list = panel.querySelector('[data-memory-list]');
  let client, pending;
  const authenticated = () => Boolean(client && client.authenticated && client.user && !client.user.isAnonymous);
  function render() { const ok = authenticated(); status.textContent = ok ? `Signed in${client.user.email ? ` as ${client.user.email}` : ''}` : 'Sign in to save private work'; save.disabled = !ok || !pending; restore.disabled = !ok; account.textContent = ok ? 'Account' : 'Sign in'; }
  ready.then(c => { client = c; render(); c.onAuth?.(() => { pending = null; list.textContent = ''; render(); }); }).catch(() => { status.textContent = 'Account unavailable'; });
  account.onclick = () => window.openProjectAccount?.(authenticated() ? 'account' : 'signin');
  window.addEventListener('project-memory-work', e => { pending = e.detail || null; render(); });
  save.onclick = async () => { if (!authenticated() || !pending) return; save.disabled = true; status.textContent = 'Saving…'; try { await client.set(`work:${pending.id || Date.now()}`, { ...pending, savedAt: new Date().toISOString() }); status.textContent = 'Saved privately'; pending = null; render(); } catch (e) { status.textContent = e.message || 'Save failed'; render(); } };
  restore.onclick = async () => { if (!authenticated()) return; list.textContent = 'Loading saved work…'; try { const keys = (await client.keys()).filter(k => k.startsWith('work:')); const rows = []; for (const key of keys) { const item = await client.get(key); if (item) rows.push({ key, item }); } list.replaceChildren(...rows.reverse().map(({key,item}) => { const b = document.createElement('button'); b.type='button'; b.textContent = item.label || key; b.style.cssText='display:block;margin:4px 0;max-width:100%;text-align:left'; b.onclick=()=>{ window.dispatchEvent(new CustomEvent('project-memory-restore',{detail:item})); status.textContent='Saved work selected'; }; return b; })); if (!rows.length) list.textContent='No saved work yet.'; } catch (e) { list.textContent = e.message || 'Could not load saved work'; } };
})();
