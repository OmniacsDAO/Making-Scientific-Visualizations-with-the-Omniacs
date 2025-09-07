# Master’s Theorem — Algorithm Complexity Visualization

<img width="2354" height="1437" alt="image" src="https://github.com/user-attachments/assets/4bed4ef8-56ed-4a9e-a5fb-b921968e6a4a" />

This visualization uses **Manim** to explain the **Master’s Theorem**, a fundamental tool for analyzing divide-and-conquer algorithms. Through animated breakdowns, we illustrate how recursive subproblems, division factors, and combining work interact to determine runtime complexity.


Watch [here](https://www.youtube.com/watch?v=KfzLefMWymA).
---

## 🎥 What the Visualization Covers

- **Formula breakdown**:  
  The recurrence relation `T(n) = aT(n/b) + f(n)` is introduced, with highlights on each parameter (`a`, `b`, and `f(n)`).

- **Problem decomposition**:  
  A large problem splits into progressively smaller subproblems, raising the key question: *which dominates runtime—the recursive calls or the combining work?*

- **The 3 Cases of Master’s Theorem**:  
  - Case 1: Subproblem work dominates.  
  - Case 2: Balanced work at all levels (e.g., Merge Sort).  
  - Case 3: Combining work dominates (e.g., naive matrix multiplication).  

- **Concrete algorithm examples**:  
  - *Binary Search*: shows Case 1 with logarithmic runtime.  
  - *Merge Sort*: Case 2, producing `O(n log n)`.  
  - *Naive Matrix Multiplication*: Case 3, resulting in `O(n³)` complexity.  

- **Final visual summary**:  
  Animated recursion trees, balance scales, and formula simplifications provide an intuitive wrap-up.

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
manim -pqh master_theorem_visualization.py MastersTheoremVisualization
```

🌐 Powered By

Omniacs.DAO — building public goods through open-source media and the $IACS token.
CA: 0x46e69Fa9059C3D5F8933CA5E993158568DC80EBf (on Base)
