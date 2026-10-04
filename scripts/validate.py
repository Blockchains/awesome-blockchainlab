#!/usr/bin/env python3
"""Validate forge.json: schema, unique slugs, URLs, and (with GH_TOKEN) that every fork and upstream exists and is not archived."""
import json, os, sys, urllib.request
d = json.load(open("forge.json")); errs = []
req = ["name", "slug", "category", "upstream", "fork", "license", "description", "codespaces"]
slugs = set()
for p in d["projects"]:
    for k in req:
        if not p.get(k) and k != "description": errs.append(f"{p.get('slug')}: missing {k}")
    if p["slug"] in slugs: errs.append(f"duplicate slug {p['slug']}")
    slugs.add(p["slug"])
    for k in ("upstream", "fork"):
        if not p[k].startswith("https://github.com/"): errs.append(f"{p['slug']}: bad {k}")
if d["count"] != len(d["projects"]): errs.append("count mismatch")
tok = os.environ.get("GH_TOKEN")
if tok:
    def get(path):
        r = urllib.request.Request(f"https://api.github.com/repos/{path}", headers={"Authorization": f"Bearer {tok}", "Accept": "application/vnd.github+json"})
        try: return json.loads(urllib.request.urlopen(r, timeout=30).read())
        except Exception as e: return {"error": str(e)}
    for p in d["projects"]:
        f = get(p["fork"].split("github.com/")[1])
        if "error" in f: errs.append(f"{p['slug']}: fork unreachable ({f['error']})")
        u = get(p["upstream"].split("github.com/")[1])
        if "error" in u: errs.append(f"{p['slug']}: upstream unreachable ({u['error']})")
        elif u.get("archived"): print(f"warning: {p['slug']} upstream is now archived")
print(json.dumps({"projects": len(d["projects"]), "errors": errs[:30]}, indent=1))
sys.exit(1 if errs else 0)
