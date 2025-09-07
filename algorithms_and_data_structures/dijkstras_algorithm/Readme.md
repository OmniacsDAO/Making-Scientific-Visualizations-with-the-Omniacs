# Dijkstra’s Algorithm — Shortest Path Visualization

<img width="1798" height="1375" alt="image" src="https://github.com/user-attachments/assets/e4e57bb6-d798-4da4-a3a0-1d5b3f8b4b1b" />

This project uses **Manim** to animate **Dijkstra’s Algorithm**, a classic graph algorithm for finding the shortest path between nodes. Through step-by-step visuals, it shows how distances are updated, nodes are processed, and the optimal path is discovered — culminating in real-world applications of the algorithm.

Watch [here](https://www.youtube.com/watch?v=Jkch7A9Qjew).
---

## 🎥 What the Visualization Covers

- **Introduction**  
  Presents the problem of finding the shortest path in a weighted graph.

- **Graph setup**  
  Nodes and weighted edges are dynamically drawn with initial distances (`0` for the source, `∞` for others):contentReference[oaicite:0]{index=0}.

- **Step-by-step execution**  
  - Highlights the current node being processed.  
  - Examines each edge and calculates tentative distances.  
  - Updates labels when shorter paths are found.  
  - Marks nodes as visited once complete.  

- **Shortest path reconstruction**  
  The final path (e.g., `A → C → E`) is traced and highlighted in **gold**, showing the result of the algorithm:contentReference[oaicite:1]{index=1}.

- **Applications**  
  Real-world examples are displayed, including:  
  - GPS navigation (finding the fastest routes)  
  - Network routing (efficient data transmission)  
  - Robotics (autonomous pathfinding):contentReference[oaicite:2]{index=2}  

---

## 🛠️ Built With
- **Python**  
- **[Manim Community Edition](https://www.manim.community/)**  

---

## ▶️ Running the Animation

To render the visualization locally:

```bash
# Install dependencies
pip install manim

# Render with preview (high quality)
manim -pqh dijkstra_algorithm.py DijkstraStepByStep
```

🌐 Powered By

Just like Dijkstra’s Algorithm finds the shortest path, the $IACS token helps us find the most efficient route to building public goods. Support Omniacs.DAO and join us in funding open knowledge.
CA: 0x46e69Fa9059C3D5F8933CA5E993158568DC80EBf (on Base)
