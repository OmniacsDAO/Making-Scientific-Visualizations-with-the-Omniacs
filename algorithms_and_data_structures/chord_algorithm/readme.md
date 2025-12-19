# Chord Algorithm Visualization - The Circular Library

An engaging Manim animation that explains the Chord distributed hash table (DHT) protocol through a creative library analogy.

<img width="1363" height="686" alt="chordalgorithmvisualization" src="https://github.com/user-attachments/assets/f55f4045-eb60-4ff9-bdf8-d02413ebcb72" />


## Overview

This visualization presents the Chord algorithm as a story about a circular library with librarians managing book sections. It makes complex distributed systems concepts accessible through relatable metaphors.

## The Story Concept

### The Library Analogy

- **Circular Library**: Represents the Chord ring (hash space)
- **Librarians**: Represent nodes (computers) in the network
- **Books with Numbers**: Represent data keys
- **Helper Lists**: Represent finger tables
- **Sections**: Represent ID ranges each node manages

### The Librarians' Story

The animation features "angry librarians" who are:
- Overworked and underpaid (relatable humor)
- Managing specific sections of books
- Helping each other find books efficiently
- Joining and leaving the network dynamically

## Chord Algorithm Fundamentals

### Key Concepts

1. **Circular Hash Space**: Nodes arranged in a logical ring
2. **Distributed Storage**: Data distributed across multiple nodes
3. **Finger Tables**: Each node maintains shortcuts to other nodes
4. **Successor/Predecessor**: Each node knows its neighbors

### Operations Demonstrated

#### 1. Lookup Operation
- Start at any node in the ring
- Follow finger table pointers
- Reach destination in **O(log N)** hops
- Example: Finding Book #10 in the library

#### 2. Node Join
- New librarian (node) joins the network
- Takes over a portion of existing node's data
- Neighbors update their finger tables
- Network self-adjusts automatically

#### 3. Node Departure
- Librarian leaves the network
- Data transferred to successor node
- Network stabilizes automatically
- Remaining nodes update their tables

## Performance Characteristics

- **Lookup Time**: O(log N) where N = number of nodes
- **Scalability**: Supports millions of nodes
- **Decentralization**: No central server required
- **Self-healing**: Automatic updates on node changes

## Real-World Applications

### 1. Peer-to-Peer File Sharing
- BitTorrent-like systems use DHT based on Chord
- Locate files across millions of computers

### 2. Distributed Storage Systems
- Cloud storage (Amazon Dynamo, Apache Cassandra)
- Chord-inspired protocols for reliable data storage

### 3. Content Delivery Networks (CDN)
- Finding nearest server for web content
- Efficient content distribution across networks

### 4. Blockchain & Cryptocurrencies
- Peer discovery in blockchain networks
- Data distribution using DHT principles

## Animation Scenes

1. **Introduction**: The Circular Library concept
2. **Librarian Meme Intro**: Humorous context setting
3. **Meet the Librarians**: Node introduction
4. **Find Book Journey**: Lookup demonstration
5. **New Librarian Joins**: Node join operation
6. **Librarian Leaves**: Node departure handling
7. **Finale Connection**: Mapping to real Chord algorithm
8. **Real-World Applications**: Practical uses

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
manim -pql chordalgorithmvisualization.py ChordLibraryStory
```

### High Quality Render
```bash
manim -pqh chordalgorithmvisualization.py ChordLibraryStory
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
- `ChordLibraryStory`: Primary scene orchestrator

### Key Methods
- `create_librarian()`: Creates node representations with faces
- `create_sections_table()`: Shows data distribution
- `create_books()`: Visual data representations
- `execute_journey_step_simple()`: Animates lookup steps

### Helper Methods
- `show_text()`: Displays explanatory text with auto-fade
- `show_helper_update()`: Visualizes finger table updates

## Educational Value

Perfect for:
- Distributed systems courses
- Computer networking classes
- Understanding P2P systems
- Learning about DHTs
- Algorithm visualization presentations

## Technical Details

- **Ring Size**: 16 positions (simplified for visualization)
- **Initial Nodes**: 4 librarians at positions 0, 4, 8, 12
- **Dynamic Operations**: Join (position 6) and Leave (position 4)

## Historical Context

The Chord protocol was developed at MIT in 2001 and has been powering decentralized internet applications since then. It remains one of the most influential DHT algorithms in distributed systems.

---

## 🤝 Support Algorithmic Education

Maintained with ❤️ by Omniacs.DAO – accelerating digital public goods through data.

🛠️ Keep public infrastructure thriving. Buy $IACS on Base — CA: 0x46e69Fa9059C3D5F8933CA5E993158568DC80EBf
