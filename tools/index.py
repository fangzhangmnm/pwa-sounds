#!/usr/bin/env python3
# tools/index.py —— 核对 / 补全 index.json：每条 file 存在、bytes 与 sha256 对得上（--write 把实测值写回去）。created 2026-10-07 by Claude Fable 5.1
# 用法：python3 tools/index.py [--write]。目录条目的其他字段（名字、许可证、出处）人手写；这个脚本只管字节事实，不编造。
import hashlib, json, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""): h.update(b)
    return h.hexdigest()
def main():
    write = "--write" in sys.argv
    idx = json.load(open(os.path.join(ROOT, "index.json"), encoding="utf-8"))
    bad = 0
    for e in idx["sounds"]:
        for key, path_key in (("", "file"), ("license.", "file")):
            obj = e if key == "" else e.get("license", {})
            rel = obj.get(path_key)
            if not rel: continue
            p = os.path.join(ROOT, rel)
            if not os.path.isfile(p): print(f"MISSING {rel}"); bad += 1; continue
            n, h = os.path.getsize(p), sha(p)
            if write: obj["bytes"], obj["sha256"] = n, h
            elif obj.get("bytes") != n or obj.get("sha256") != h: print(f"MISMATCH {rel}: bytes {obj.get('bytes')}→{n} sha256 {str(obj.get('sha256'))[:12]}→{h[:12]}"); bad += 1
    if write:
        with open(os.path.join(ROOT, "index.json"), "w", encoding="utf-8") as f: f.write(json.dumps(idx, ensure_ascii=False, indent=1) + "\n")
        print("index.json written")
    else: print("OK" if not bad else f"{bad} problem(s)"); sys.exit(1 if bad else 0)
main()
