# Open Source JEV Alternatives

**6:09 · 1920×1080 · 60fps · AI voiceover + music**

Voiced, layout-fixed version of the research-bundle explainer: five families of open-source models that copy Jev's interface (state in, probabilities out) with very different machinery underneath, plus DiffusionGemma and the calibration trap.

## Files
- `Open_Source_JEV_Alternatives.py` — the base Manim scene (closing headline fitted; sections lengthened slightly so the full narration fits — 5:55 → 6:09).
- `v2_fixed.py` + `common_fix.py` — subclass the base scene: all text auto-fits its box, font Montserrat, overflow checker, section times logged.
- `vo_orig.py` — voices each section of `OPEN_SOURCE_JEV_NARRATION.md` into its time window (Kokoro TTS, voice `am_michael`). If a section is still too long at a brisk pace it trims the longest middle sentence — the 7 trimmed sentences are listed in `Transcript.md`.
- `mix_orig.py` (uses `finish.py`) — music bed that ducks under the voice.

## Render
```
manim -qh v2_fixed.py OpenSourceJevAlternativesFixed
python3 vo_orig.py OPEN_SOURCE_JEV_NARRATION.md "[0.3,34.1,64.2,116.3,166.5,216.5,259.7,286.7,309.9,346.1]" 369.0 vo_v2.wav am_michael 1.08
python3 mix_orig.py media/videos/v2_fixed/1080p60/OpenSourceJevAlternativesFixed.mp4 vo_v2.wav '[[0,"intro"],[34,"groove"],[64,"drive"],[259.7,"mystery"],[346,"resolve"]]' Open_Source_JEV_Alternatives_Fixed.mp4
```
Needs: `manim` 0.21, `kokoro-onnx` (model files `kokoro-v1.0.onnx`, `voices-v1.0.bin` from github.com/thewh1teagle/kokoro-onnx releases), FFmpeg, fonts Montserrat + Space Mono.

**Accuracy note:** the video separates what TypeSafe has publicly claimed about Jev from what it has not published, and presents the 2025 papers and open-source projects as architecturally similar — not as proven sources of Jev.

Full narration: `Transcript.md`.

🌐 Powered By

Every visualization here is free and open-source — made possible by Omniacs.DAO and the $IACS token. If these projects spark curiosity or help your learning, consider supporting the token that funds public goods. Buy $IACS on Base. CA: 0x46e69Fa9059C3D5F8933CA5E993158568DC80EBf
