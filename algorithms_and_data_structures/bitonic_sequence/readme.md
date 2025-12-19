# Bitonic Sequence Search Visualization

A comprehensive Manim animation that explains the Bitonic Sequence Search algorithm through visual demonstrations.

## Overview

This animation explores the concept of bitonic sequences and demonstrates how to efficiently search within them using binary search techniques. The visualization breaks down the algorithm step-by-step, making it accessible for educational purposes.

## What is a Bitonic Sequence?

A **bitonic sequence** is an array that:
1. First **increases** monotonically to a peak element
2. Then **decreases** monotonically after the peak

Example: `[1, 3, 5, 8, 12, 15, 10, 6, 4, 2]` - increases to 15, then decreases

## Algorithm Explained

The Bitonic Search Algorithm works in these key steps:

### Step 1: Find the Peak
- Use binary search to locate the maximum element in O(log n) time
- The peak divides the array into two monotonic subarrays

### Step 2: Partition into Subarrays
- Left subarray: Ascending order (before peak)
- Right subarray: Descending order (after peak)

### Step 3: Check Peak Value
- If target equals peak, search complete!

### Step 4: Validate Search Space
- If target > peak, element doesn't exist
- If target < peak, continue searching

### Step 5 & 6: Search Subarrays
- Binary search in ascending subarray: O(log n)
- If not found, binary search in descending subarray: O(log n)

## Time Complexity

- **Find Peak**: O(log n)
- **Search Subarrays**: O(log n)
- **Total Time**: **O(log n)** ✨

## Real-World Applications

1. **Parallel Computing & GPUs**
   - GPU sorting algorithms for graphics rendering
   - Machine learning computations
   - High-performance scientific computing

2. **Hardware Sorting Networks**
   - FPGA and ASIC implementations
   - High-speed packet routing
   - Real-time data processing

3. **Database & Big Data Systems**
   - Parallel query processing
   - Distributed sorting operations
   - Large-scale indexing

## Animation Features

The visualization includes:
- Introduction to bitonic sequences
- Step-by-step algorithm walkthrough
- Visual representation with color-coded bars
- Detailed explanations of each operation
- Real-world application examples
- Credits section

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
manim -pql bitonicsequence_search.py BitonicVisualization
```

### High Quality Render
```bash
manim -pqh bitonicsequence_search.py BitonicVisualization
```

### Render Options
- `-pql`: Preview at low quality (480p)
- `-pqm`: Preview at medium quality (720p)
- `-pqh`: Preview at high quality (1080p)
- `-pqk`: Preview at 4K quality (2160p)
- `-p`: Preview after rendering
- `-f`: Show output file in file manager

## Code Structure

- `BitonicVisualization`: Main scene class
- `create_bars()`: Creates visual bar chart representations
- `update_text()`: Helper for text transitions

## Educational Value

This animation is perfect for:
- Computer science students learning search algorithms
- Algorithm visualization presentations
- Understanding parallel computing concepts
- Teaching divide-and-conquer strategies

---

## 🤝 Support Algorithmic Education

Maintained with ❤️ by Omniacs.DAO – accelerating digital public goods through data.

🛠️ Keep public infrastructure thriving. Buy $IACS on Base — CA: 0x46e69Fa9059C3D5F8933CA5E993158568DC80EBf
