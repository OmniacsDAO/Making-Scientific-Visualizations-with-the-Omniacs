# 🔁 Bubble Sort Visualization with Manim

This project visualizes the **Bubble Sort** algorithm using [Manim](https://www.manim.community/) with side-by-side animation of bar swapping and Python code. It walks through the sorting logic step-by-step using color, movement, and transitions.

![Preview](preview.png)

[Watch here!](https://youtu.be/yBFVHNReUy0)

## ✨ Features

- ✅ Displays the full Python `bubble_sort()` function
- 📊 Animated bar graph representing array values
- 🔴 Highlights comparisons in red
- 🔁 Swaps bars using smooth transitions
- 🧠 Demonstrates sorting logic from start to finish

## 🧮 Algorithm Shown

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
```


The animation uses the input: [4, 3, 1, 5, 2] and performs swaps until fully sorted.

🎨 Visual Components
Element	Style
Code	Python code block on left
Bars	Vertical rectangles
Values	Numeric labels above bars
Highlighted Pair	Red fill during comparison
Swaps	Animated with Swap()

📦 Requirements

    Python 3.8+

    Manim Community Edition

Install via:

```bash
pip install manim
```

▶️ How to Run

Render with Manim:

```bash
manim -pql Bubble_sort_animation.py BubbleSortBarGraph
```

Use -qh instead of -pql for high quality rendering.

📁 File Overview

    Bubble_sort_animation.py — Manim animation script

    README.md — This file

🎓 Educational Value

Ideal for:

    Teaching sorting algorithms visually

    Introductory programming lessons

    Side-by-side animation and code tracing



---
🤝 Support Open Source Learning

*Maintained with ❤️ by **Omniacs.DAO** – accelerating digital public goods through data.*

🛠️ Keep public infrastructure thriving. Buy [$IACS](http://dexscreener.com/base/0xd4d742cc8f54083f914a37e6b0c7b68c6005a024) on Base — CA: 0x46e69Fa9059C3D5F8933CA5E993158568DC80EBf
