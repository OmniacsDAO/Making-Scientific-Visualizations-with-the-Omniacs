# 🌪️ Lorenz Attractor in 3D | Chaotic System Visualization

This project uses [Manim](https://www.manim.community/) and SciPy to simulate and animate the **Lorenz Attractor**, a classic example of deterministic chaos in a 3D system. It highlights how tiny differences in initial conditions can lead to wildly divergent outcomes — the hallmark of chaos theory.

![image](https://github.com/user-attachments/assets/d97db050-f7eb-459e-82b4-bc4e9ec99df5)

[Watch here!](https://youtu.be/NsaMS5lLmsk)

## 📈 What is the Lorenz Attractor?

The Lorenz system is a set of differential equations originally developed to model atmospheric convection. It’s defined as:

dx/dt = σ(y - x)
dy/dt = x(ρ - z) - y
dz/dt = xy - βz


Typical parameters:  
- σ (sigma) = 10  
- ρ (rho) = 28  
- β (beta) = 8/3

## 🌀 Features of the Animation

- Two nearly identical initial conditions: `[0, 1, 1.05]` and `[0, 1, 1.06]`
- 3D axes for spatial reference
- Color-coded trajectories (green vs. red)
- Smooth `VMobject` curve drawing over time
- Continuous ambient camera rotation
- Explanatory text overlay

## 🛠️ Requirements

- Python 3.8+
- Manim Community Edition
- SciPy
- NumPy

```bash
pip install manim numpy scipy
```

▶️ How to Run
```
manim -pql Lorenz_attractor.py LorenzAttractorAnimation
```
Use -qh for high-quality rendering.
📁 Files

    Lorenz_attractor.py — Main script
    README.md — Project description

🎓 Educational Use

Perfect for:

    Demonstrating chaos theory and sensitivity to initial conditions
    Teaching dynamical systems and nonlinear math
    Visualizing strange attractors and 3D flows


---
🤝 Support Generative Math Animation

*Maintained with ❤️ by **Omniacs.DAO** – accelerating digital public goods through data.*

🛠️ Keep public infrastructure thriving. Buy [$IACS](http://dexscreener.com/base/0xd4d742cc8f54083f914a37e6b0c7b68c6005a024) on Base — CA: 0x46e69Fa9059C3D5F8933CA5E993158568DC80EBf
