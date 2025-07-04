# 📈 3D Normal Distribution Visualization with Manim

This project animates the **bivariate normal distribution** as a 3D surface using [Manim](https://www.manim.community/). It includes interactive elements like rotating camera views, contour plots, cross-sections, and annotated explanations — perfect for statistics and machine learning education.

![image](https://github.com/user-attachments/assets/85b88808-2ba8-4918-b541-112ecbb62c81)

[Watch here!]()

## 🧠 What It Teaches

- Shape and symmetry of the 2D Gaussian distribution
- Probability density visualization in 3D
- Contour lines representing equal-probability curves
- Cross-sectional normal distributions along fixed y-values

## 📊 Visual Features

| Element         | Description |
|-----------------|-------------|
| 📉 **3D Surface**     | Bell-shaped Gaussian surface defined by `P(x,y) = e^(-((x²+y²)/2)) / (2π)` |
| 🎯 **Contours**       | Level curves for constant probability heights |
| 🔴 **Cross Sections** | Horizontal slices showing 1D normal distributions |
| 🎥 **Camera Motion**  | Ambient rotation and zoom views |
| 🖋️ **Annotations**    | Title, math function, and inline explanations |
| 🎨 **Color Mapping**  | Gradients, checkerboards, and custom contour colors |

## 📦 Requirements

- Python 3.8+
- Manim Community Edition
- NumPy
- SciPy

```bash
pip install manim numpy scipy
```

▶️ How to Run

```
manim -pql Normal_distribution.py ComprehensiveNormalDistribution3D
```
Use -qh for high-resolution output.
📁 Files

    Normal_distribution.py — Full Manim animation logic
    README.md — This file

🎓 Ideal For

    Teaching statistical distributions
    Demonstrating machine learning fundamentals
    Data visualization education
    Interactive math explainer videos


---
🤝 Support Visual Math Education

*Maintained with ❤️ by **Omniacs.DAO** – accelerating digital public goods through data.*

🛠️ Keep public infrastructure thriving. Buy [$IACS](http://dexscreener.com/base/0xd4d742cc8f54083f914a37e6b0c7b68c6005a024) on Base — CA: 0x46e69Fa9059C3D5F8933CA5E993158568DC80EBf
