# Probability-First AI with Jev and Its Open Source Alternatives

**3:04 · 1920×1080 · 60fps · AI voiceover + music**

Voiced, layout-fixed version of the research-bundle explainer: the March 2025 SalesRLAgent paper, the September 2025 confidence-routing paper, and how they compare with what's publicly known about Jev.

## Files
- `JEV_Probability_First_AI.py` — the base Manim scene (with one panel narrowed so it stays inside the frame).
- `v1_fixed.py` + `common_fix.py` — subclass the base scene: all text auto-fits its box, font Montserrat, overflow checker, section times logged for voice sync.
- `vo_orig.py` — voices each section of `JEV_narration_and_timing.md` into its time window (Kokoro TTS, voice `am_michael`).
- `mix_orig.py` (uses `finish.py`) — music bed that ducks under the voice; video stream copied.

## Render
```
manim -qh v1_fixed.py ProbabilityFirstAIFixed
python3 vo_orig.py JEV_narration_and_timing.md "[0.3,19.5,41.2,67.3,90.3,116.4,152.5,172.8]" 183.7 vo_v1.wav am_michael 1.0
python3 mix_orig.py media/videos/v1_fixed/1080p60/ProbabilityFirstAIFixed.mp4 vo_v1.wav '[[0,"intro"],[19.5,"groove"],[90.3,"mystery"],[116.4,"drive"],[171,"resolve"]]' JEV_Probability_First_AI_Fixed.mp4
```
Needs: `manim` 0.21, `kokoro-onnx` (model files `kokoro-v1.0.onnx`, `voices-v1.0.bin` from github.com/thewh1teagle/kokoro-onnx releases), FFmpeg, fonts Montserrat + Space Mono.

**Accuracy note:** the video separates what TypeSafe has publicly claimed about Jev from what it has not published, and presents the 2025 papers and open-source projects as architecturally similar — not as proven sources of Jev.

Full narration: `Transcript.md`.

🌐 Powered By

Every visualization here is free and open-source — made possible by Omniacs.DAO and the $IACS token. If these projects spark curiosity or help your learning, consider supporting the token that funds public goods. Buy $IACS on Base. CA: 0x46e69Fa9059C3D5F8933CA5E993158568DC80EBf
