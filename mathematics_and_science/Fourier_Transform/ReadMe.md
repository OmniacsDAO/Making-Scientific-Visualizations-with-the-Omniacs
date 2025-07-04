# 🎵 Fourier Transform in Motion | Animated Signal Decomposition with Manim

This project animates how complex signals are built from — and decomposed into — sine waves using the **Fourier Transform**. Created with [Manim](https://www.manim.community/), it shows how waveforms evolve in both the time and frequency domains.

![image](https://github.com/user-attachments/assets/b82bc8a0-6b09-46a0-81d1-a06d806166ab)

[Watdch here!](https://youtu.be/B6fGCMDI5Fw)
## 🔊 What It Shows

- 📈 **Composite Wave Construction**: Left panel shows a wave built from sine components
- 🎨 **Sine Component Display**: Right panel plots each sine wave by frequency and amplitude
- 📉 **Wave Breakdown**: Each sine is subtracted to break the wave down
- 📊 **Frequency Histogram**: A spectrum appears showing amplitude vs frequency

## 🧠 Educational Concepts

- Fourier series and signal composition
- Amplitude spectrum representation
- Time-domain ↔ Frequency-domain duality
- Signal decomposition and reconstruction

## 🎨 Visual Breakdown

| Panel            | Visualizes                                  |
|------------------|---------------------------------------------|
| Left             | Composite wave (time-domain)                |
| Right (initial)  | Individual sine waves added to the signal   |
| Right (final)    | Histogram of frequencies (spectrum)         |
| Color Coding     | Each sine wave has a unique color           |

## 📦 Requirements

- Python 3.8+
- Manim Community Edition
- NumPy

```bash
pip install manim numpy
```

▶️ How to Run

```
manim -pql Fourier_Transform.py FourierTransformVisualization
```

Use -qh for high-resolution rendering.
📁 Files

    Fourier_Transform.py — Main Manim animation script
    README.md — This documentation

🎓 Perfect For

    Signal processing education
    Understanding frequency decomposition
    STEM visual learning
    DSP, audio, and math teaching material

    
---
*Maintained with ❤️ by **Omniacs.DAO** – accelerating digital public goods through data.*

🛠️ Keep public infrastructure thriving. Buy [$IACS](http://dexscreener.com/base/0xd4d742cc8f54083f914a37e6b0c7b68c6005a024) on Base — CA: 0x46e69Fa9059C3D5F8933CA5E993158568DC80EBf
