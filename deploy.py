#!/usr/bin/env python3
"""Deploy site/ + functions/ to Netlify via file-digest API. Auth injected on the wire (service 'netlify')."""
import hashlib, io, json, os, zipfile, urllib.request, urllib.parse
SITE_ID = "f942d81b-fe35-498f-9e91-88d45dbbff1a"
API = "https://api.netlify.com/api/v1"
ROOT = os.path.dirname(os.path.abspath(__file__))
def req(method, url, data=None, ctype="application/json"):
    r = urllib.request.Request(url, data=data, method=method, headers={"Content-Type": ctype})
    with urllib.request.urlopen(r, timeout=120) as resp:
        b = resp.read(); return json.loads(b) if b else {}
files, blobs = {}, {}
site = os.path.join(ROOT, "site")
for dp, dn, fn in os.walk(site):
    dn[:] = [d for d in dn if d != "work"]
    for f in fn:
        full = os.path.join(dp, f); rel = "/" + os.path.relpath(full, site)
        data = open(full, "rb").read(); h = hashlib.sha1(data).hexdigest()
        files[rel] = h; blobs[h] = (rel, data)
funcs, fblobs = {}, {}
fdir = os.path.join(ROOT, "functions")
for f in sorted(os.listdir(fdir)) if os.path.isdir(fdir) else []:
    if not f.endswith(".js"): continue
    name = f[:-3]; buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
        zi = zipfile.ZipInfo(f, date_time=(2026, 1, 1, 0, 0, 0)); z.writestr(zi, open(os.path.join(fdir, f), "rb").read())
    data = buf.getvalue(); h = hashlib.sha256(data).hexdigest()
    funcs[name] = h; fblobs[h] = (name, data)
dep = req("POST", f"{API}/sites/{SITE_ID}/deploys", json.dumps({"files": files, "functions": funcs}).encode())
did = dep["id"]
for h in dep.get("required", []):
    rel, data = blobs[h]; req("PUT", f"{API}/deploys/{did}/files{urllib.parse.quote(rel)}", data, "application/octet-stream")
for h in dep.get("required_functions", []):
    name, data = fblobs[h]; req("PUT", f"{API}/deploys/{did}/functions/{name}?runtime=js", data, "application/octet-stream")
print("deploy", did, "files", len(files), "uploaded", len(dep.get("required", [])), "functions", list(funcs), "uploaded", len(dep.get("required_functions", [])))
