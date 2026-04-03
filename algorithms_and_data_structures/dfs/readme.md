# Depth-First Search Visualization
A complete visual explainer of the Depth-First Search graph traversal algorithm. Covers the rules, live traversal of a 7-node graph step by step with detailed captions, and four real-world use cases. Designed to be followed by anyone — no prior knowledge of algorithms required.

<img width="1134" height="727" alt="image" src="https://github.com/user-attachments/assets/bc82c9b5-4ea4-4761-ac96-e3997786f912" />

[Watch here!](https://www.youtube.com/watch?v=6yg5V2zDWy0)

---


---

## What's Inside the Video

| Part | Title | What you see |
|------|-------|-------------|
| 1 | Intro Slide | Title, one-liner definition, three rule pills |
| 2 | Live Graph Traversal | 7-node graph, step-by-step DFS with colour changes, backtrack arrows, dead-end markers, captions at every step |
| 3 | Use-Case Cards | 2×2 grid of application cards: Web Crawlers, Cycle Detection, Topological Sort, Game AI |

---

## Correct DFS Visit Order

```
A → B → D → G → E → C → F
```

**Edge list:**
```
A–B   A–C   B–D   B–F   D–G   E–G   E–C
```

**Dead ends in order:**
1. C — neighbours A (visited) and E (visited)
2. F — only neighbour B (visited)

---

## Graph Layout

Node positions verified at zero edge crossings:

```
A:  LEFT  5.0
B:  LEFT  3.0  + UP   1.5
C:  LEFT  3.0  + DOWN 1.5
D:  LEFT  1.0  + UP   2.5
F:  LEFT  1.0  + UP   0.5
G:  RIGHT 1.0  + UP   1.5
E:  RIGHT 1.0  + DOWN 1.5
```

B–D goes **upward** from B. B–F goes **downward** from B. They fan in opposite directions so neither line passes near the other node — no visual ambiguity.

The G–E edge is a **cross-connection** — it joins the right branch (B→D→G) to the left branch (A→C→E), which is why C gets visited from E's side rather than directly from A.

---

## Requirements

| Dependency | Version |
|-----------|---------|
| Python | 3.10 or higher |
| Manim Community | v0.18 or higher |
| FFmpeg | required for video export |

```bash
pip install manim
```

---

## Running the Animation

**Fast preview:**
```bash
manim -pql dfs_visualization.py DFSVisualization --disable_caching
```

**High quality (1080p 60fps):**
```bash
manim -pqh dfs_visualization.py DFSVisualization --disable_caching
```

Output: `media/videos/dfs_visualization/1080p60/DFSVisualization.mp4`

---

## Colour Palette

| Name | Hex | Used for |
|------|-----|---------|
| C_BG | `#0A0E1A` | Background |
| C_NODE | `#1A73E8` | Unvisited node fill |
| C_VISIT | `#1E8C45` | Visited node fill |
| C_ACTIVE | `#F4A61D` | Node being visited (pulse) |
| C_EDGE | `#2E3D55` | Untraversed edge |
| C_EVIS | `#56CCB2` | Traversed edge |
| C_WHITE | `#F0F4FF` | Node labels, caption text |
| C_GOLD | `#FFD166` | Section headers, START badge, final line |

---

## Key Concepts Covered

- **DFS rule** — always go deeper before going wider; use a stack to remember the path
- **Visited tracking** — never revisit a node already on the visited list
- **Dead end** — a node whose every neighbour is already visited; triggers backtracking
- **Backtracking** — return up the stack until a node with an unvisited neighbour is found
- **Cross-connection** — an edge joining two otherwise separate branches (G–E in this graph)
- **Sibling nodes** — D and F are both connected to B but not to each other; B–D and B–F are independent edges

---

## Notes for Developers

- The layout was mathematically verified: all 7 edges were tested for intersections using the cross-product segment test. Result: zero crossings.
- The caption bar uses a solid dark rectangle at the screen bottom with text swapping via `FadeOut(old, shift=UP) + FadeIn(new, shift=UP)` — this keeps the caption zone stable and avoids layout jumps.
- `dead_end()` draws a red ring + cross overlay, holds for 1.2 seconds, then removes it cleanly before the next caption fires.
- `backtrack()` draws an orange arrow from one node to the previous, holds for 0.5 seconds, then removes it — keeping the graph clean.
- Part 3 cards use a `shift LEFT` correction so the right column never clips the frame edge.

---

## License

Free to use for educational and non-commercial purposes. Attribution appreciated.

---
🤝 Support Visual Math Learning
*Maintained with ❤️ by **Omniacs.DAO** – accelerating digital public goods through data.*

🛠️ Keep public infrastructure thriving. Buy [$IACS](http://dexscreener.com/base/0xd4d742cc8f54083f914a37e6b0c7b68c6005a024) on Base — CA: 0x46e69Fa9059C3D5F8933CA5E993158568DC80EBf
