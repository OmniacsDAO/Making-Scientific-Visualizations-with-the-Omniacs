# Hopcroft-Karp Algorithm Visualization

A comprehensive Manim animation that demonstrates why greedy algorithms fail for maximum matching problems and how the Hopcroft-Karp algorithm succeeds using augmenting paths.

<img width="1215" height="745" alt="hopcroftkarp" src="https://github.com/user-attachments/assets/2231dec7-4857-4152-bd13-7e6ba2c109bc" />


## Overview

This visualization presents the maximum bipartite matching problem through a relatable job placement scenario, showing the limitations of greedy approaches and the power of the Hopcroft-Karp algorithm.

## The Problem: Maximum Bipartite Matching

### Setup
- **Two groups**: Job seekers and companies (or any two disjoint sets)
- **Connections**: Lines show valid pairings (qualifications)
- **Goal**: Match as many pairs as possible
- **Constraint**: Each person/company can only be in one match

### Example Scenario
```
5 Job Seekers: Alice, Bob, Carol, Dan, Eve
5 Companies: TechCo, StartUp, CorpInc, AILab, DesignCo

Qualifications:
- Alice → TechCo, CorpInc
- Bob → StartUp, AILab
- Carol → TechCo, DesignCo
- Dan → CorpInc, AILab
- Eve → StartUp, DesignCo
```

**Challenge**: Can we match ALL 5 people to jobs?

## Why Greedy Algorithms Fail

### The Greedy Approach
Process candidates in order, each taking their first available choice.

### Failure Example (Order: Carol → Dan → Bob → Alice → Eve)

1. **Carol** → TechCo ✓ (first choice)
2. **Dan** → CorpInc ✓ (first choice)
3. **Bob** → StartUp ✓ (first choice)
4. **Alice** → ??? ✗ (TechCo taken, CorpInc taken)
5. **Eve** → ??? ✗ (StartUp taken, DesignCo unavailable)

**Result**: Only 3 out of 5 matched! 😞

### Why It Fails
- **Order dependence**: Processing sequence matters
- **Myopic decisions**: No look-ahead or backtracking
- **Local optimum**: Gets stuck in suboptimal matching
- **No recovery**: Can't undo bad early choices

## Hopcroft-Karp to the Rescue!

### Key Innovation: Augmenting Paths

An **augmenting path** is a path from an unmatched node in one group to an unmatched node in the other group, alternating between matched and unmatched edges.

### How It Works

#### Step 1: Start with Any Matching
Begin with the greedy result (or empty matching).

#### Step 2: Find Augmenting Paths
Search for paths: `unmatched → ... → unmatched`

#### Step 3: Flip the Path
Swap matched/unmatched edges along the path:
- Unmatched edges → **Matched**
- Matched edges → **Unmatched**

#### Step 4: Repeat
Continue until no augmenting paths exist.

### Success Example

**Starting**: Carol→TechCo, Dan→CorpInc, Bob→StartUp (3/5)

**Augmenting Path 1**: Fix Alice
```
Alice → CorpInc ← Dan → AILab (free)
```
Flip: Alice→CorpInc, Dan→AILab (4/5)

**Augmenting Path 2**: Fix Eve
```
Eve → DesignCo (free company, direct match!)
```
Match: Eve→DesignCo (5/5) ✅

**Result**: **ALL 5 matched!** 🎉

### Final Matching
- Alice → CorpInc ✓
- Bob → StartUp ✓
- Carol → TechCo ✓
- Dan → AILab ✓
- Eve → DesignCo ✓

## Algorithm Properties

### Time Complexity
- **Hopcroft-Karp**: O(E × √V)
  - E = number of edges
  - V = number of vertices
- **Greedy**: O(E) but not optimal!

### Optimality
- ✅ **Guaranteed maximum matching**
- ✅ Always finds the optimal solution
- ✅ No dependence on processing order

### Advantages
1. **Optimal**: Finds maximum cardinality matching
2. **Efficient**: Fast for large graphs
3. **Deterministic**: Same result every time
4. **General**: Works for any bipartite graph

## Real-World Applications

### Job Placement
Match candidates to roles based on qualifications and preferences.

### Organ Donation
Match donors to recipients considering compatibility and medical factors.

### Dating Apps
Find compatible matches between users with mutual interests.

### Ride Sharing
Assign drivers to riders efficiently for optimal coverage.

### Task Assignment
Allocate workers to tasks based on skills and availability.

### School Admissions
Assign students to programs based on preferences and requirements.

## Animation Features

### Scene Breakdown

1. **Introduction**: Problem setup and motivation
2. **Real-World Problem**: Job placement scenario
3. **Setup Explanation**: Bipartite graph introduction
4. **Greedy Failure**: Demonstration of greedy approach failure
5. **Hopcroft-Karp Rescue**: Augmenting path demonstration
6. **Applications**: Real-world use cases
7. **Finale**: Summary and key learnings

### Visual Elements

- Bipartite graph with two colored groups
- Animated edge creation
- Color-coded matches (green = matched)
- Augmenting path highlighting
- Step-by-step explanations
- Progress tracking

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
manim -pql hopcroftkarp.py HopcroftKarp
```

### High Quality Render
```bash
manim -pqh hopcroftkarp.py HopcroftKarp
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
- `HopcroftKarp(Scene)`: Primary scene class

### Configuration
```python
colors = {
    'bg': "#0a0a0a",
    'group_a': "#3498db",     # First group (job seekers)
    'group_b': "#e74c3c",     # Second group (companies)
    'matched': "#2ecc71",     # Matched edges
    'path': "#f39c12",        # Augmenting path
    'highlight': "#f1c40f",   # Highlights
    'title': "#1abc9c"        # Titles
}
```

### Key Methods

#### Scene Methods
- `scene_intro()`: Title and introduction
- `scene_real_world_problem()`: Problem description
- `scene_setup_explanation()`: Graph explanation
- `scene_greedy_failure()`: Greedy algorithm demonstration
- `scene_hopcroft_karp_rescue()`: Algorithm demonstration
- `scene_applications()`: Use cases
- `scene_finale()`: Summary

#### Graph Methods
- `create_bipartite_graph()`: Creates visual representation
- `create_app_card()`: Application cards

## Key Learnings

### 1. Greedy Algorithms Can Fail
Processing order can trap us in suboptimal solutions.

### 2. Augmenting Paths
Paths from unmatched → unmatched nodes that improve the matching.

### 3. Path Flipping
Rearranging existing matches can increase total matches.

### 4. Guaranteed Optimality
Hopcroft-Karp always finds the maximum matching!

## Comparison Table

| Aspect | Greedy | Hopcroft-Karp |
|--------|--------|---------------|
| Optimality | ❌ No | ✅ Yes |
| Time Complexity | O(E) | O(E × √V) |
| Order Dependence | ❌ Yes | ✅ No |
| Backtracking | ❌ No | ✅ Yes |
| Use Case | Quick approximation | Guaranteed maximum |

## Educational Value

Perfect for:
- Algorithm design courses
- Graph theory education
- Optimization problem solving
- Computer science interviews
- Understanding maximum flow concepts

## Tips for Customization

1. **Change Scenario**: Modify `student_names` and `company_names`
2. **Adjust Connections**: Update the `connections` list
3. **Animation Speed**: Change `run_time` parameters
4. **Colors**: Update the `colors` dictionary

## Related Algorithms

- **Ford-Fulkerson**: Maximum flow algorithm
- **Hungarian Algorithm**: Assignment problem
- **Edmonds' Blossom**: General graph matching
- **Gale-Shapley**: Stable matching

## Further Reading

- Hopcroft & Karp (1973): "An n^(5/2) algorithm for maximum matchings in bipartite graphs"
- Network flow algorithms
- Combinatorial optimization

---

## 🤝 Support Algorithmic Education

Maintained with ❤️ by Omniacs.DAO – accelerating digital public goods through data.

🛠️ Keep public infrastructure thriving. Buy $IACS on Base — CA: 0x46e69Fa9059C3D5F8933CA5E993158568DC80EBf
