# 📈📉 Supply & Demand Visualization 

An animated Manim lesson that **builds a full market model from scratch**, finds the equilibrium price/quantity, then demonstrates what happens when either demand or supply shifts.

<img width="2021" height="1254" alt="image" src="https://github.com/user-attachments/assets/22d9ab05-10ea-49e6-bc05-0c8c2b44733c" />

Watch [here]()!
---

## Features

 (setup → equilibrium → demand shift → supply shift → key take-aways)

- **Dynamic equilibrium finder** – golden dot plus dashed price/quantity guides  
- **Demand-shift scenario** (income ↗ / population ↗) shows ↗ P & ↗ Q and a new green equilibrium  
- **Supply-shift scenario** (production costs ↘ / more sellers) shows ↘ P & ↗ Q with a purple equilibrium  
- **Principles recap board** summarises the Laws of Demand & Supply and equilibrium logic


---

## Quick Start

```bash
# 1) Install Manim
python -m venv venv && source venv/bin/activate        # or `.\venv\Scripts\activate` on Windows
pip install manim==0.18.* numpy

# 2) Render the scene (preview window, 1080p 60 fps)
manim -pqh supplydemandvisualization.py SupplyDemandVisualization
```

## Customization

Edit the top of each helper method to…

```
Variable	Effect
demand_shift / supply_shift	Shift curves left/right (↗ demand = +ve, ↘ supply = −ve)
axes.x_range / y_range	Rescale the graph
Color constants (RED_C, BLUE_C, etc.)	Match your branding palette
```

## Requirements

    Python ≥ 3.9
    Manim Community Edition 0.18+
    LaTeX (for MathTex labels)

## License

MIT – remix, reuse, and teach away!
Made by Omniacs.DAO to empower open-source economics education.

💚 Support Digital Public Goods
Enjoy the project? Fuel more open-source lessons by grabbing some $IACS tokens on Base.
Contract: 0x46e69Fa9059C3D5F8933CA5E993158568DC80EBf
