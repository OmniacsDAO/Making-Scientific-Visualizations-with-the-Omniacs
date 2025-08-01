# 🧠 Memory Management Visualization with Manim

<img width="1716" height="1004" alt="image" src="https://github.com/user-attachments/assets/44d9b258-73f1-4d3a-a35d-e7081d024cd1" />

Watch the video [here](https://youtu.be/TrI4p--Ztr8).

This animation illustrates **memory management strategies** used by operating systems to allocate and organize memory efficiently. Using clear visual metaphors and step-by-step examples, it explains allocation methods like **First Fit**, **Best Fit**, **Worst Fit**, and **Memory Compaction**.

Created with [Manim](https://www.manim.community/), this animation is perfect for students, teachers, and developers wanting to understand how OS memory allocators work under the hood.

## 📽️ Demo Output

![Memory Management Preview](preview.gif)  
*A visual explainer for memory allocation strategies and compaction.*

---

## 📦 Requirements

- Python 3.7+
- [Manim Community Edition](https://docs.manim.community/en/stable/)

Install via pip:

```bash
pip install manim
```

🚀 How to Run

```
manim -pql memory_management.py MemoryManagementSymphony

Use -pqh or -p4k for higher-quality output.
```

💡 Concepts Covered
📦 Allocation Strategies

    First Fit: Allocates memory in the first block large enough to fit the request.
    Best Fit: Finds the smallest block that fits the request, minimizing waste.
    Worst Fit: Uses the largest available block, leaving smaller gaps for later.
    Memory Compaction: Rearranges scattered allocations to create one large contiguous free space.

🧠 Educational Enhancements

    Animated request scanning and block coloring
    Beginner-friendly analogies (e.g., bookshelf metaphor)
    Explanations displayed alongside each step
    Color-coded strategies (Blue = First Fit, Green = Best Fit, Purple = Worst Fit)

📁 Files

    memory_management.py: Main Manim animation script
    preview.gif: (Optional) A looping preview of the animation

🎓 Ideal For

    Operating systems lectures
    Computer science students
    Visual learners exploring memory allocation
    EdTech creators making explainer content

📜 License

MIT License

---

Support open-source visual learning:
💸 Powered by $IACS on Base – Omniacs.DAO
CA: 0x46e69Fa9059C3D5F8933CA5E993158568DC80EBf
