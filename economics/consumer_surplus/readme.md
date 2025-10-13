# Consumer & Producer Surplus — *Animated Guide to Market Welfare* 📈💰

<img width="1468" height="1237" alt="image" src="https://github.com/user-attachments/assets/11e6eb2a-766b-49ac-8834-bf15177517fb" />


**Manim animation that builds equilibrium, shades individual surpluses, and shows how a tax creates dead-weight loss.**  
Perfect for Econ 101, AP/IB classes, and anyone curious about how markets generate (or destroy) welfare.

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
| 1 | **Title slide** “Consumer & Producer Surplus” + subtitle on market efficiency | |
| 2 | **Supply & Demand curves** with golden equilibrium \((P^*,Q^*) = (5.5,\;4.5)\) | |
| 3 | **Consumer Surplus** shaded green above price line | |
| 4 | **Producer Surplus** shaded purple below price line | } |
| 5 | **Tax impact:** \$2/unit wedge, split buyer/seller prices, DWL appears |  |

---

## Quick Start

```bash
# 1. Clone & enter
git clone https://github.com/OmniacsDAO/ConsumerProducerSurplus.git
cd ConsumerProducerSurplus

# 2. Create Python env & install deps
python -m venv venv && source venv/bin/activate       # Windows: .\venv\Scripts\activate
pip install manim==0.18.* numpy

# 3. Render (preview window, 1080 p, 60 fps)
manim -pqh consumerproducersurplus.py ConsumerProducerSurplus

    Need 4 K?
    manim -pqh --format=mp4 --resolution=3840,2160 consumerproducersurplus.py ConsumerProducerSurplus

```


## Requirements

    Python ≥ 3.9
    Manim CE  0.18+
    LaTeX distribution (for MathTex)

## License & Support

MIT — reuse freely in classrooms or your own YouTube channel!

💚 Support Digital Public Goods
If this helped you, grab some $IACS tokens on Base and fund more open-source econ visuals.
Contract: 0x46e69Fa9059C3D5F8933CA5E993158568DC80EBf

Made with 📊 by Omniacs.DAO
