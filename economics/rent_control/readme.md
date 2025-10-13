# Price Elasticity Visualization — *Understanding Price Controls & Market Reactions* 💸⚖️

<img width="989" height="915" alt="image" src="https://github.com/user-attachments/assets/5d7414be-0b31-4d0a-b15f-84d4fed08f84" />

 **Manim animation that visualizes the effects of price ceilings and floors.**  
 See what happens when governments set prices above or below equilibrium — and how shortages or surpluses emerge.

Watch [here]().
---

## Table of Contents  
1. [Demo](#demo)  •  2. [Features](#features)  •  3. [Quick Start](#quick-start)  
4. [Scene Index](#scene-index)  •  5. [Customization](#customization)  •  6. [Requirements](#requirements)  
7. [License & Support](#license--support)

---

## Features

| # | What you’ll see | Highlights |
|:-:|-----------------|-------------|
| 1 | **Title card:** “Price Elasticity Visualization” | Introduces price controls in free markets |
| 2 | **Equilibrium setup:** Supply & demand intersect at P\*, Q\* | Establishes the natural price mechanism |
| 3 | **Price ceiling** (e.g., rent control) below equilibrium | Shortage visualized — demand exceeds supply |
| 4 | **Price floor** (e.g., minimum wage) above equilibrium | Surplus visualized — supply exceeds demand |
| 5 | **Elasticity comparison:** Steep vs flat curves → magnitude of DWL | Shows how elasticities change the market’s reaction |
| 6 | **Summary board:** key takeaways + policy reflections | Concludes with “Iron Law of Price Controls” message |

---

## Quick Start

```bash
# 1. Clone & enter
git clone https://github.com/OmniacsDAO/PriceElasticityVisualization.git
cd PriceElasticityVisualization

# 2. Set up environment
python -m venv venv && source venv/bin/activate     # Windows: .\venv\Scripts\activate
pip install manim==0.18.* numpy

# 3. Render (preview, 1080p)
manim -pqh priceelasticityvisualization.py PriceElasticityVisualization

    4K export:
    manim -pqh --format=mp4 --resolution=3840,2160 priceelasticityvisualization.py PriceElasticityVisualization
```


## Requirements

    Python ≥ 3.9
    Manim CE 0.18+
    LaTeX distribution (for MathTex)

## License & Support

MIT — reuse freely for classrooms, YouTube channels, or workshops.

💚 Support Digital Public Goods
Made with 💸 by Omniacs.DAO
If this project helps you, consider grabbing some $IACS tokens on Base to help fund more open-source educational visuals.
Contract: 0x46e69Fa9059C3D5F8933CA5E993158568DC80EBf

