# Frequency Count Algorithm — Animated Visualization with Manim

<img width="2390" height="1472" alt="image" src="https://github.com/user-attachments/assets/bf372144-0c90-44be-88d3-b00cee594cd1" />

This project uses **Manim** to animate a **frequency count** over a list of integers: initializing counters, scanning the dataset once, updating counts in real time, and finishing with a clean bar-chart distribution and summary stats. The scene is structured as a teaching aid: clear steps, progress indicators, and a final complexity recap. :contentReference[oaicite:0]{index=0}

Watch [here](https://www.youtube.com/watch?v=-e0VG-8eEwQ).
---

## 🎥 What the Visualization Covers

- **Step 1 — Our Dataset**  
  Displays a grid of values and introduces the task: “count occurrences of each value in the list.”

- **Step 2 — Initialize Counters**  
  Creates labeled counters (one per unique value) with color-coding for clarity.

- **Step 3 — Counting Process**  
  Iterates through the dataset **once**, highlighting the current element, incrementing its counter, and updating a **live progress %**.

- **Step 4 — Results & Visualization**  
  Builds a custom **bar chart** (axes, dashed grid lines, tick labels) and renders:  
  - Bars per value  
  - A count badge + **percentage** above each bar  
  - A **summary panel** (total items, unique values, most frequent value, max frequency)

- **Algorithm Summary & Complexity**  
  Concludes with a recap and complexity: **Time O(n)**, **Space O(k)** where *k* = number of unique values.

---

## 🛠️ Built With
- **Python**  
- **[Manim Community Edition](https://www.manim.community/)**

---

## ▶️ Running the Animation

```bash
# Install dependencies
pip install manim

# Render with preview (high quality)
manim -pqh frequency_count.py MathematicalFrequencyCount
```

✨ Learning Outcomes

How to design an algorithm animation with clear didactic stages
Building HUD elements (titles, labels, progress) that guide attention
Constructing primitive charting in Manim (axes, grid, ticks, bars)
Communicating complexity and key stats alongside visuals

🌐 Powered By

Counting what matters is the first step to improving public goods. The [$IACS](http://dexscreener.com/base/0xd4d742cc8f54083f914a37e6b0c7b68c6005a024) token funds open-source education like this—so if this visualization helped your teaching or learning, consider supporting Omniacs.DAO.
CA: 0x46e69Fa9059C3D5F8933CA5E993158568DC80EBf (on Base)
