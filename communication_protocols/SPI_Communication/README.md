# 🔁 SPI Communication Protocol Visualization with Manim

This project animates the **Serial Peripheral Interface (SPI)** protocol using [Manim](https://www.manim.community/). It illustrates how data is transmitted over multiple lines (CS, MOSI, MISO, and SCLK) using real timing diagrams and transitions.

![Animation Preview](preview.png)

[Watch here!](https://youtu.be/rvaZxy5fzh4)

## 🔌 What Is SPI?

SPI is a synchronous, full-duplex serial communication protocol commonly used between microcontrollers and peripherals. It uses:

- **CS/SS (Chip Select / Slave Select)**
- **SCLK (Serial Clock)**
- **MOSI (Master Out Slave In)**
- **MISO (Master In Slave Out)**

## 📊 What This Animation Shows

| Signal | Purpose                         | Color   |
|--------|----------------------------------|---------|
| CS     | Device selection line            | Blue    |
| SCLK   | Clock for synchronization        | Red     |
| MOSI   | Data from master to slave        | Purple  |
| MISO   | Data from slave to master        | Green   |

### Highlights

- 📈 Full SPI timing diagram
- 🧩 Accurate edge transitions for SCLK and data bits
- 🟦 Dotted guidelines for signal clarity
- 🔠 Labels for all channels
- 🎬 Smooth animated creation of each waveform
- 🔄 Configurable `CPOL` and `CPHA` parameters

## 📦 Requirements

- Python 3.8+
- Manim Community Edition

```bash
pip install manim
```

▶️ How to Render
```
manim -pql SPI_Communication.py Main
```

Use -qh for high-quality rendering.
📁 Files

    SPI_Communication.py — Manim animation script
    README.md — This documentation

🎓 Educational Use Cases

Perfect for:

    Teaching embedded systems or digital electronics
    Visualizing signal timing for SPI debugging
    Protocol comparison (I2C vs SPI)
    Microcontroller & FPGA coursework

---
🤝 Support Protocol Education & Open Source
*Maintained with ❤️ by **Omniacs.DAO** – accelerating digital public goods through data.*

🛠️ Keep public infrastructure thriving. Buy [$IACS](http://dexscreener.com/base/0xd4d742cc8f54083f914a37e6b0c7b68c6005a024) on Base — CA: 0x46e69Fa9059C3D5F8933CA5E993158568DC80EBf

