import re, sys, json, numpy as np, soundfile as sf, subprocess
from kokoro_onnx import Kokoro
K = Kokoro("/home/claude/tts/kokoro-v1.0.onnx", "/home/claude/tts/voices-v1.0.bin")
SR = 24000
FIX = [("JevK5", "Jev K five"), ("LoRA", "Laura"), ("Qwen", "Kwen"), ("RLCD", "R L C D"), ("PPO", "P P O"), ("GRPO", "G R P O"),
       ("DiffusionGemma", "Diffusion Gemma"), ("SemIf", "Sem If"), ("mmBERT", "M M BERT"), ("ModernBERT", "Modern BERT"),
       ("InfoNCE", "Info N C E"), ("NanoJev", "Nano Jev"), ("Open-Jev", "Open Jev"), ("OpenJev", "Open Jev"), ("TD(λ)", "T D lambda"),
       ("—", ", "), ("–", " to "), ("e.g.", "for example"), ("i.e.", "that is"), ("vs.", "versus"), ("LLM", "L L M"), ("LLMs", "L L Ms"),
       ("RAG", "rag"), ("API", "A P I"), ("CE", "C E"), ("2B", "2 B"), ("4B", "4 B"), ("9B", "9 B")]

def sections(md):
    txt = open(md).read(); out = []
    for m in re.finditer(r"^## ([0-9]+):([0-9]+)[–-]([0-9]+):([0-9]+)[^\n]*\n(.*?)(?=^## |\Z)", txt, re.S | re.M):
        body = m.group(5)
        body = re.sub(r"^\s*[-*>#].*$", lambda x: x.group(0).lstrip("->*# "), body, flags=re.M)
        body = re.sub(r"[*_`]", "", body); body = re.sub(r"\[(.*?)\]\(.*?\)", r"\1", body)
        body = " ".join(l.strip() for l in body.splitlines() if l.strip() and not l.strip().lower().startswith(("visual", "on-screen", "on screen", "note")))
        out.append(dict(start=int(m.group(1)) * 60 + int(m.group(2)), end=int(m.group(3)) * 60 + int(m.group(4)), text=body.strip()))
    return out

def say(text, window, voice, base=1.0):
    import re as _re
    sents = _re.split(r'(?<=[.?!])\s+', text.strip())
    dropped = []
    for sp in (base, 1.12, 1.16, 1.2):
        s_, sr_ = K.create(_fix(text), voice=voice, speed=sp, lang="en-us")
        if len(s_) / sr_ <= window: return s_, len(s_) / sr_, sp
    while True:
        s_, sr_ = K.create(_fix(" ".join(sents)), voice=voice, speed=1.18, lang="en-us")
        if len(s_) / sr_ <= window or len(sents) <= 2: break
        mid = list(range(1, len(sents) - 1)); j = max(mid, key=lambda i: len(sents[i]))
        dropped.append(sents.pop(j))
    if dropped:
        with open("/tmp/vo_dropped.log", "a") as f: f.write("\n".join("  - " + d for d in dropped) + "\n")
    return len(s_) / sr_ <= window + 0.2 and (s_, len(s_) / sr_, 1.18) or _say(" ".join(sents), window, voice, base)

def _fix(text):
    for a, b in FIX: text = re.sub(r"(?<![A-Za-z])" + re.escape(a) + r"(?![A-Za-z])", b, text)
    return text

def _say(text, window, voice, base=1.0):
    for a, b in FIX: text = re.sub(r"(?<![A-Za-z])" + re.escape(a) + r"(?![A-Za-z])", b, text)
    speed = base
    while True:
        s, sr = K.create(text, voice=voice, speed=speed, lang="en-us")
        d = len(s) / sr
        if d <= window or speed >= 1.22: return s, d, speed
        speed = min(1.22, speed * max(1.03, d / window * 1.01))

if __name__ == "__main__":
    md, starts_json, total, out, voice = sys.argv[1], sys.argv[2], float(sys.argv[3]), sys.argv[4], sys.argv[5]
    secs = sections(md); starts = json.loads(starts_json)
    assert len(starts) == len(secs), (len(starts), len(secs))
    track = np.zeros(int((total + 1) * SR), np.float32); report = []
    for i, (sec, st) in enumerate(zip(secs, starts)):
        nxt = starts[i + 1] if i + 1 < len(starts) else total - 0.8
        window = nxt - st - 0.7
        s, d, sp = say(sec["text"], window, voice, float(sys.argv[6]) if len(sys.argv) > 6 else 1.0)
        a = int((st + 0.35) * SR); track[a:a + len(s)] += s[:len(track) - a]
        report.append(f"{st:6.1f}s  window {window:5.1f}s  speech {d:5.1f}s  speed {sp:.2f}  {'OVER' if d > window + 0.3 else 'ok'}")
    sf.write(out, track, SR); print("\n".join(report))
