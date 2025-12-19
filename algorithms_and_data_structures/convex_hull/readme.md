# Convex Hull Visualization - The Rubber Band Problem

A beautiful Manim animation that explains the Convex Hull problem and Graham Scan algorithm through an intuitive rubber band analogy.

<img width="1362" height="702" alt="convexhull" src="https://github.com/user-attachments/assets/db4c5834-e571-4ddf-8f71-ec1d0f0ad727" />


## Overview

This visualization demonstrates how to find the smallest boundary that wraps around a set of points - like stretching a rubber band around nails on a board and letting it snap tight.

## What is a Convex Hull?

The **convex hull** of a set of points is the smallest convex polygon that contains all the points. Imagine:
- Nails scattered on a wooden board
- A rubber band stretched around ALL the nails
- Let go, and it snaps to form the tightest boundary

That boundary is the convex hull!

## The Graham Scan Algorithm

### How It Works

#### Step 1: Find the Lowest Point
- Locate the point with minimum y-coordinate
- This becomes the starting point (pivot)
- **Time**: O(n)

#### Step 2: Sort by Angle
- Sort all other points by polar angle from the pivot
- Creates a counter-clockwise sweep pattern
- Visual: Draw lines from pivot to all points
- **Time**: O(n log n)

#### Step 3: Build the Hull
- Connect points in sorted order
- Keep only "left turns" (stay on outer edge)
- Discard "right turns" (would go inside)
- **Time**: O(n)

### Why Only Left Turns?

- **Left Turn** ✓: Staying on the OUTER edge
- **Right Turn** ✗: Going INSIDE (discard!)

The algorithm checks the direction at each point to ensure we stay outside, creating the minimal boundary.

## Time Complexity

- **Overall**: **O(n log n)** (dominated by sorting step)
- **Space**: O(n) for storing hull points
- **Optimal**: Yes! Can't do better than O(n log n) in comparison-based model

## Real-World Applications

### 🎮 Video Games
- **Collision Detection**: Simplified bounding shapes for game objects
- **Physics Engines**: Efficient collision testing

### 🗺️ Geographic Information Systems (GIS)
- **Boundary Detection**: Finding borders of regions
- **Terrain Mapping**: Outlining geographic features

### 📦 Logistics & Routing
- **Delivery Optimization**: Finding efficient delivery zones
- **Warehouse Planning**: Space utilization

### 🤖 Robotics
- **Path Planning**: Navigation around obstacles
- **Workspace Analysis**: Determining reachable areas

### 📊 Data Analysis
- **Outlier Detection**: Finding boundary points in datasets
- **Pattern Recognition**: Shape analysis in machine learning

## Animation Features

### Scene Breakdown

1. **Introduction**: Title and concept introduction
2. **Real-World Analogy**: Nails and rubber band metaphor
3. **The Problem**: Visual demonstration with random points
4. **Rubber Band Demo**: Animated rubber band snapping
5. **Algorithm Visualization (Example 1)**: Step-by-step Graham Scan
6. **Algorithm Visualization (Example 2)**: Different point configuration
7. **Applications**: Real-world use cases
8. **Finale**: Summary and key takeaways

### Visual Elements

- Dynamic point generation with random seeds
- Animated bar growth and transformations
- Color-coded algorithm steps
- Angle visualization with numbered points
- Smooth transitions between scenes

## 📦 Requirements

### System Requirements
- **Python 3.8+**
- **Manim Community Edition**
- **NumPy**

### Installation

#### Step 1: Install Python
Ensure you have Python 3.8 or higher installed. Check your version:
```bash
python --version
```

#### Step 2: Install Manim Community Edition
```bash
pip install manim
```

Or using conda:
```bash
conda install -c conda-forge manim
```

#### Step 3: Install NumPy (if not already installed)
```bash
pip install numpy
```

### Verify Installation
```bash
manim --version
```

## Running the Animation

### Basic Execution (Low Quality - Fast)
```bash
manim -pql convexhull.py ConvexHull
```

### High Quality Render
```bash
manim -pqh convexhull.py ConvexHull
```

### Render Options
- `-pql`: Preview at low quality (480p)
- `-pqm`: Preview at medium quality (720p)
- `-pqh`: Preview at high quality (1080p)
- `-pqk`: Preview at 4K quality (2160p)
- `-p`: Preview after rendering
- `-f`: Show output file in file manager

## Code Structure

### Main Class
- `ConvexHull(Scene)`: Primary scene class

### Key Methods

#### Geometric Algorithms
- `find_lowest_point()`: Locates the pivot point
- `sort_by_angle()`: Sorts points by polar angle
- `cross_product()`: Determines turn direction
- `compute_convex_hull()`: Implements Graham Scan

#### Visualization Methods
- `generate_random_points()`: Creates point sets
- `create_app_card()`: Builds application cards
- `explain_left_turns_concept()`: Visual explanation

### Scene Methods
- `scene_intro()`: Title sequence
- `scene_real_world_analogy()`: Rubber band story
- `scene_the_problem()`: Problem definition
- `scene_rubber_band_demo()`: Animated demonstration
- `scene_algorithm_visualization()`: First example
- `scene_algorithm_visualization_second()`: Second example
- `scene_applications()`: Use cases
- `scene_finale()`: Summary and credits

## Mathematical Foundation

### Cross Product Test
```python
def cross_product(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
```

- **Positive**: Left turn (keep point)
- **Zero**: Collinear (edge case)
- **Negative**: Right turn (discard point)

## Educational Value

Perfect for:
- Computational geometry courses
- Algorithm design classes
- Computer graphics education
- Game development learning
- Data science visualization

## Tips for Customization

1. **Change Point Count**: Modify `generate_random_points(n)` parameter
2. **Adjust Speed**: Change `run_time` parameters in play() calls
3. **Color Themes**: Update the `colors` dictionary
4. **Add Examples**: Duplicate visualization scenes with different seeds

## Further Reading

- "Computational Geometry: Algorithms and Applications" by de Berg et al.
- Graham's original 1972 paper on the algorithm
- Applications in computer graphics and GIS

---

## 🤝 Support Algorithmic Education

Maintained with ❤️ by Omniacs.DAO – accelerating digital public goods through data.

🛠️ Keep public infrastructure thriving. Buy $IACS on Base — CA: 0x46e69Fa9059C3D5F8933CA5E993158568DC80EBf
