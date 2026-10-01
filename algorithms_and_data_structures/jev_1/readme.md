# JEV and Open Decision-like Models Explained

<img width="1565" height="766" alt="image" src="https://github.com/user-attachments/assets/04b83f48-cdcb-4d49-a861-155389dc32c3" />

**4:10 · 1920×1080 · 60fps · AI voiceover + music · burned-in captions**

A code-rendered Manim explainer on Jev: what TypeSafe claims, why a decision model beats reading a chatbot's "yes", calibration, the two 2025 research papers, the five families of open-source Jev alternatives, and the shift from AI that *writes* to AI that *decides*.

## Files
- `vo.py` — the narration script; generates one voice clip per segment (Kokoro TTS, voice `am_michael`) and `vo_meta.json`.
- `jev_flagship.py` — Manim scene `JevExplained`. Each segment's voice length drives its animation timing; every label auto-fits its box; an overflow checker logs anything outside the safe frame; `timeline.json` records segment start times.
- `finish.py` — chapter-aware music bed, ducking under the voice, burned-in captions (`sections_hq.json` = music sections).

## Render
```
python3 vo.py am_michael
manim -qh jev_flagship.py JevExplained
python3 finish.py media/videos/jev_flagship/1080p60/JevExplained.mp4 timeline.json vo_meta.json sections_hq.json JEV_Explained_Flagship.mp4
```
Needs: `manim` 0.21, `kokoro-onnx` (model files `kokoro-v1.0.onnx`, `voices-v1.0.bin` from github.com/thewh1teagle/kokoro-onnx releases), FFmpeg, fonts Montserrat + Space Mono.

**Accuracy note:** the video separates what TypeSafe has publicly claimed about Jev from what it has not published, and presents the 2025 papers and open-source projects as architecturally similar — not as proven sources of Jev.

Full narration: `Transcript.md`.

🌐 Powered By

Every visualization here is free and open-source — made possible by Omniacs.DAO and the $IACS token. If these projects spark curiosity or help your learning, consider supporting the token that funds public goods. Buy $IACS on Base. CA: 0x46e69Fa9059C3D5F8933CA5E993158568DC80EBf
