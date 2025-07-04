# 🔌 I2C Communication Protocol Visualization with Manim

This project provides a step-by-step animated explanation of the **I²C (Inter-Integrated Circuit)** communication protocol using [Manim](https://www.manim.community/). It visually represents SDA (data) and SCL (clock) signal lines along with bits, ACK/NACK, and clock transitions.

![Animation Preview](preview.png)

[Watch here!](https://youtu.be/Z47vjVMND_E)

## 🧠 What is I2C?

I²C is a serial protocol used for short-distance, low-speed communication between chips. It uses:
- **SDA (Serial Data Line)**
- **SCL (Serial Clock Line)**

This animation simulates:
- Start/Stop conditions
- Address + Read/Write bits
- Clock pulses
- Data transfer
- ACK/NACK responses

## 📽️ What’s Included

- 📊 Coordinate axes to represent digital signals
- 🔁 Clock signal generation (square waves)
- 📉 Step function for data line
- 🎨 Bit-wise color coding for address, R/W, data, and ACK
- ✏️ Text labels for interpretation (SDA, SCL, ACK, etc.)

## 🧩 Bit Breakdown

| Segment        | Bits | Color     |
|----------------|------|-----------|
| Address        | 7    | Green     |
| R/W            | 1    | Red       |
| ACK            | 1    | Blue      |
| Data           | 8    | Orange    |
| Final ACK/NACK | 1    | Blue      |

## 📦 Requirements

- Python 3.8+
- Manim Community Edition

```bash
pip install manim
```

▶️ How to Render
```
manim -pql I2C_Communication.py Main
```

Use -qh for high quality.
📁 File Structure

    I2C_Communication.py — Manim animation script
    README.md — This documentation

📚 Educational Use Cases

    Explaining embedded systems communication
    Teaching protocol timing & logic levels
    Debugging logic analyzers or signal traces



---
🤝 Support Visual Protocol Education
*Maintained with ❤️ by **Omniacs.DAO** – accelerating digital public goods through data.*

🛠️ Keep public infrastructure thriving. Buy [$IACS](http://dexscreener.com/base/0xd4d742cc8f54083f914a37e6b0c7b68c6005a024) on Base — CA: 0x46e69Fa9059C3D5F8933CA5E993158568DC80EBf
