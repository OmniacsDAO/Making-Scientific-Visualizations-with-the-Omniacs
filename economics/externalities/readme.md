# Externalities — *Visualizing Market Failures & Pigouvian Solutions* 🌍⚖️

<img width="1707" height="1230" alt="image" src="https://github.com/user-attachments/assets/392b97b9-42f7-4345-9b4a-6cfb5b96b061" />


**Manim animation that illustrates negative and positive externalities, dead-weight loss, and government remedies.**  
A clear, colorful walk-through of how private and social costs diverge — and how taxes or subsidies can restore efficiency.

Watch [here]().
---

## Table of Contents  
1. [Demo](#demo)  •  2. [Features](#features)  •  3. [Quick Start](#quick-start)  
4. [Scene Index](#scene-index)  •  5. [Customization](#customization)  •  6. [Requirements](#requirements)  
7. [License & Support](#license--support)

---

## Features

| # | What you’ll see | Code reference |
|:-:|-----------------|----------------|
| 1 | **Title slide:** “Externalities — When Private Markets Miss the Mark” |   |
| 2 | **Negative externality** example — pollution; shows gap between MPC & MSC |   |
| 3 | **Positive externality** example — education; gap between MPB & MSB |   |
| 4 | **Deadweight loss** area shaded red for over/underproduction |   |
| 5 | **Pigouvian tax** shifts supply to correct overproduction; new efficient Q |   |
| 6 | **Pigouvian subsidy** for positive externalities restores efficient output |   |
| 7 | **Summary board:** real-world examples & recap of policies |   |

---

## Quick Start

```bash
# 1. Clone & enter
git clone https://github.com/OmniacsDAO/Externalities.git
cd Externalities

# 2. Set up Python environment
python -m venv venv && source venv/bin/activate        # Windows: .\venv\Scripts\activate
pip install manim==0.18.* numpy

# 3. Render (preview window, 1080p)
manim -pqh externalities.py Externalities

    4K export:
    manim -pqh --format=mp4 --resolution=3840,2160 externalities.py Externalities
```

## Requirements

    Python ≥ 3.9
    Manim CE 0.18+
    LaTeX distribution (for MathTex)

## License & Support

MIT — reuse freely for education, remixes, or your own econ videos.

💚 Support Digital Public Goods
Made with 🌍 by Omniacs.DAO
If this project helps you, grab some $IACS tokens on Base to fund more open-source econ visualizations.
Contract: 0x46e69Fa9059C3D5F8933CA5E993158568DC80EBf

