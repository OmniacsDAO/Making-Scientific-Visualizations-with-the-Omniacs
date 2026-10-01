"""Music bed + mix + burned captions for Manim explainers.
usage: python3 finish.py <video.mp4> <timeline.json> <vo_meta.json> <sections.json> <out.mp4> [seed]
sections.json: [[start_seconds, style], ...]  style in: intro, groove, mystery, drive, resolve
"""
import numpy as np, wave, json, sys, subprocess, re
SR = 44100
rng = np.random.default_rng(int(sys.argv[6]) if len(sys.argv) > 6 else 7)

def T(l): return np.arange(int(l * SR)) / SR
def lp(x, k, n=2):
    for _ in range(n): x = np.convolve(x, np.ones(k) / k, mode='same')
    return x
def hp(x): return np.diff(x, prepend=0)
def nz(l): return rng.standard_normal(int(l * SR))
def env(l, a, r): t = T(l); return np.minimum(1, t / max(a, 1e-3)) * np.clip((l - t) / max(r, 1e-3), 0, 1)
def note(m): return 440 * 2 ** ((m - 69) / 12)
def kick(l=0.4): t = T(l); f = 45 + 110 * np.exp(-t * 30); return np.tanh(np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 8) * 2)
def clap(): t = T(0.2); return hp(hp(nz(0.2))) * np.exp(-t * 22) * 0.35
def hat(l=0.04): t = T(l); return hp(hp(hp(nz(l)))) * np.exp(-t * 100) * 0.1
def pluck(f, l=0.45, k=9):
    t = T(l); s = sum(np.sin(2 * np.pi * f * h * t) * np.exp(-t * k * h) / h for h in (1, 2, 3))
    return s * np.minimum(1, t * 800)
def pad(ms, l, b=7):
    t = T(l); s = np.zeros_like(t)
    for m in ms:
        f = note(m)
        for d in (-0.004, 0, 0.004):
            ph = np.cumsum(f * (1 + d) * (1 + 0.003 * np.sin(2 * np.pi * 4.5 * t + m))) / SR; s += 2 * (ph % 1) - 1
    return lp(s / (len(ms) * 3), b, 3) * env(l, min(0.8, l / 3), min(1.0, l / 3))
def bass(f, l): t = T(l); return lp(np.sign(np.sin(2 * np.pi * f * t)), 10, 2) * np.exp(-t * 3) * np.minimum(1, t * 300)

STYLES = {
    'intro':   dict(prog=[[50, 57, 62, 65], [46, 53, 58, 62]], drums=0, arp=0.5, bass=0),
    'groove':  dict(prog=[[50, 57, 62, 65], [46, 53, 58, 62], [48, 55, 60, 64], [45, 52, 57, 61]], drums=1, arp=1, bass=1),
    'mystery': dict(prog=[[50, 57, 60, 65], [49, 56, 59, 64], [46, 53, 57, 62], [45, 52, 55, 61]], drums=0.5, arp=0.6, bass=1),
    'drive':   dict(prog=[[50, 57, 62, 65], [46, 53, 58, 65], [43, 50, 58, 62], [45, 52, 57, 64]], drums=2, arp=2, bass=1),
    'resolve': dict(prog=[[46, 53, 58, 62], [48, 55, 60, 64], [50, 57, 62, 66]], drums=0, arp=0.5, bass=0),
}

def music(dur, sections, bpm=94):
    N = int(dur * SR) + SR; out = np.zeros((N, 2)); beat = 60 / bpm; bar = beat * 4
    def add(sig, at, g=1.0, pan=0.0):
        i = int(at * SR); j = min(N, i + len(sig))
        if i >= N or i < 0: return
        l, r = np.cos((pan + 1) * np.pi / 4), np.sin((pan + 1) * np.pi / 4)
        out[i:j, 0] += sig[:j - i] * g * l * 1.414; out[i:j, 1] += sig[:j - i] * g * r * 1.414
    secs = sections + [[dur, None]]
    for (s0, style), (s1, _) in zip(secs, secs[1:]):
        st = STYLES[style]; t = s0; k = 0
        while t < s1 - 0.05:
            L = min(bar, s1 - t); ch = st['prog'][k % len(st['prog'])]
            add(pad(ch, L + 0.6), t, 0.16)
            if st['bass']: add(bass(note(ch[0] - 12), min(beat * 2, L)), t, 0.18); add(bass(note(ch[0] - 12), min(beat * 2, max(0.05, L - beat * 2))), t + beat * 2, 0.14)
            steps = int(L / (beat / 2))
            for i in range(steps):
                tt = t + i * beat / 2
                if st['arp'] >= 1 or i % 2 == 0:
                    m = ch[1 + (i * 2 + k) % 3] + 12 + (12 if (st['arp'] >= 2 and i % 4 == 3) else 0)
                    add(pluck(note(m)), tt, 0.07 * min(1.5, st['arp']), 0.4 * np.sin(i * 1.3))
                if st['drums'] >= 1:
                    if i % 2 == 0: add(kick(), tt, 0.3 if st['drums'] < 2 else 0.4)
                    if i % 4 == 2 and st['drums'] >= 2: add(clap(), tt, 0.35)
                    add(hat(), tt + beat / 4, 0.6)
                elif st['drums'] > 0 and i % 8 == 0: add(kick(0.6), tt, 0.22)
            t += bar; k += 1
    out = np.tanh(out * 1.2); out /= np.abs(out).max() * 1.1
    fade = np.clip((dur - np.arange(N) / SR) / 2.5, 0, 1)[:, None]; out *= fade
    return out[:int(dur * SR)]

def ass_time(x):
    h = int(x // 3600); m = int(x % 3600 // 60); s = x % 60
    return f"{h}:{m:02d}:{s:05.2f}"

def captions(timeline, meta, path):
    head = """[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,Montserrat,60,&H00F9F5F1,&H00FFFFFF,&H90000000,&H90000000,-1,0,0,0,100,100,0,0,3,18,0,2,140,140,40,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    M = {m['id']: m for m in meta}; lines = []
    for ev in timeline:
        if ev['id'] not in M: continue
        m = M[ev['id']]; tot = sum(len(c) for c in m['captions']); acc = 0
        for c in m['captions']:
            a = ev['t0'] + acc / tot * m['dur']; acc += len(c); b = ev['t0'] + acc / tot * m['dur']
            lines.append(f"Dialogue: 0,{ass_time(a)},{ass_time(b - 0.02)},Cap,,0,0,0,,{c}")
    open(path, 'w').write(head + "\n".join(lines) + "\n")

if __name__ == "__main__":
    video, tl, vm, secf, outp = sys.argv[1:6]
    dur = float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", video]).decode())
    timeline = json.load(open(tl)); meta = json.load(open(vm)); secs = json.load(open(secf))
    mus = music(dur, secs)
    with wave.open('/tmp/_music.wav', 'wb') as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((mus * 32767).astype(np.int16).tobytes())
    captions(timeline, meta, '/tmp/_caps.ass')
    fc = ("[0:a]aformat=channel_layouts=stereo,volume=1.6,asplit=2[vo][sc];"
          "[1:a]volume=0.9[mu];[mu][sc]sidechaincompress=threshold=0.03:ratio=8:attack=20:release=400[duck];"
          "[vo][duck]amix=inputs=2:normalize=0,alimiter=limit=0.95[a];"
          "[0:v]subtitles=/tmp/_caps.ass:fontsdir=/root/.fonts[v]")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", video, "-i", "/tmp/_music.wav", "-filter_complex", fc,
                    "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-preset", "medium", "-crf", "18", "-pix_fmt", "yuv420p",
                    "-c:a", "aac", "-b:a", "256k", "-movflags", "+faststart", outp], check=True)
    print("done", outp, round(dur, 1))
