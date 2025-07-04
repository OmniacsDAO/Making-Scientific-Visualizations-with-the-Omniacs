# 🔄 Visualizing the Irrationality of Pi with Compound Rotations | Manim

This project uses [Manim](https://www.manim.community/) to illustrate the **irrationality of π** by animating two rotating vectors (arms) spinning at different rates. The resulting motion traces a non-repeating, beautifully tangled path.

![image](https://github.com/user-attachments/assets/eb174d6a-5a90-4a16-899a-e7f3920f9ef7)

[Watch here!](https://youtu.be/kH07SfMRzF0)

## 🔢 What It Demonstrates

- Two arms rotate from a common origin:
  - First rotates with angular velocity θ
  - Second rotates faster by √4×θ (i.e., 2×θ)
- Red arm is anchored to the end of the yellow arm
- The tip of the red arm traces a complex, **non-repeating** path
- Duration of rotation: 60 seconds → full π motion cycles

## 🧠 Conceptual Significance

- The traced path never overlaps perfectly
- This illustrates **incommensurable rotation periods**
- Demonstrates **π’s irrationality** via visual geometry

## 🎨 Visual Features

| Element        | Description |
|----------------|-------------|
| Yellow Line    | Primary rotating vector (θ) |
| Red Line       | Secondary rotating vector (2θ) |
| Blue Path      | Traced tip of red vector |
| Smooth Motion  | Controlled with `ValueTracker` |
| Frame Rate     | 60 fps for fluid tracing |

## 📦 Requirements

- Python 3.8+
- Manim Community Edition
- NumPy

```bash
pip install manim numpy
```

▶️ How to Run

```
manim -pql Pi_Irrational.py compass2
```
Use -qh for high-resolution render.
📁 Files

    Pi_Irrational.py — Animation script
    README.md — This file

🎓 Ideal For

    Teaching irrational numbers and π
    Visual demonstrations of compound rotations
    Math and physics education tools
    Visual art in generative math


---
🤝 Support Open-Source Math Animation
*Maintained with ❤️ by **Omniacs.DAO** – accelerating digital public goods through data.*

🛠️ Keep public infrastructure thriving. Buy [$IACS](http://dexscreener.com/base/0xd4d742cc8f54083f914a37e6b0c7b68c6005a024) on Base — CA: 0x46e69Fa9059C3D5F8933CA5E993158568DC80EBf
