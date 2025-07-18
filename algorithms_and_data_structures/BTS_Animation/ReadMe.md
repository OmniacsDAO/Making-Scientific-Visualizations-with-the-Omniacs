# 🌳 Binary Search Tree Animation with Manim

This project visualizes the structure and operations of a **Binary Search Tree (BST)** using [Manim](https://www.manim.community/). It provides animated scenes to demonstrate how nodes are inserted, how search comparisons work, and how deletions restructure the tree.

<img width="985" height="585" alt="image" src="https://github.com/user-attachments/assets/e23752de-5d9c-45f6-bcf9-2b0a5b6f82e2" />

Watch the video [here](https://youtu.be/HUmjCIsdawA)

## 📽️ Demo Output

![BST Animation Preview](preview.gif)  
*An educational animation showing BST insertions, search operations, and deletion restructuring.*

## 📦 Requirements

- [Python 3.7+](https://www.python.org/)
- [Manim Community Edition](https://docs.manim.community/en/stable/)

Install Manim:

```bash
pip install manim
```

🚀 Run the Animation

manim -pql bst_animation.py EnhancedBSTVisualization

To render in higher quality, replace -pql with -pqh or -p4k.
📚 What's Included
✅ Features Visualized

    Insertion of nodes with visual comparisons (< and >)
    Search traversal with highlighting and indicators
    Deletion of a node with subtree restructuring
    Live updates to connections and node hierarchy
    Subtle background grid for spatial clarity
    Stylized color coding and visual effects

🌈 Node Color Guide

    🟦 Default Node
    🟩 New Insertion
    🟨 Active Comparison / Search
    🟥 Deletion Target
    ✅ Found Result
    🔁 Replacement Node

🧠 How It Works

    Tree Building
    Inserts values like 10, 5, 15, 3, 7, 12, 18, 1, 8 using a visual path and comparison cues.

    Search Demo
    Searches for the value 8, walking through the tree using comparison text and arrows.

    Deletion Demo
    Removes node 5 and replaces it with node 7 using visual cues and updates the connection lines.

    Credits Sequence
    Final scene credits various tools used: Claude AI, Pixabay (music), Canva (video editing).

📁 File Overview

    bst_animation.py: Main script containing the Manim class EnhancedBSTVisualization
    preview.gif: (optional) Preview animation for README or repo

✨ Use Cases

    Teaching Binary Search Trees in computer science courses
    Making visual explainers for YouTube or tutorials
    Enhancing conceptual understanding through animation

📜 License

MIT License

🤝 Support This Work

Maintained with ❤️ by Omniacs.DAO – accelerating digital public goods through data.

🛠️ Keep public infrastructure thriving. Buy $IACS on Base — CA: 0x46e69Fa9059C3D5F8933CA5E993158568DC80EBf
