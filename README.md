# Making-Scientific-Visualizations-with-the-Omniacs
Making Scientific Visualizations with the Omniacs


The following tools are fundamental for the creation process of the animations: The animations are exculsively rendered using manim library, the code is written in python and ffmpeg. Other important python libraries include Plotly, Seaborn, and Matplotlib

# Python

Python is a powerful, modern tool, easy-to-learn, and versatile programming language widely used for web development, data analysis, automation, artificial intelligence, scientific computing, and more. Its clear syntax and large ecosystem of libraries like [Manim](https://www.manim.community/), [Plotly](https://plotly.com/python/), [Seaborn](https://seaborn.pydata.org/#), and [Matplotlib](https://matplotlib.org/) make it a popular choice for beginners and professionals alike.

---

## Install Python

### Install on Windows

1. Go to the [official Python download page](https://www.python.org/downloads/windows/).
2. Download the latest Python installer for Windows.
3. Run the installer.
   - **Important:** Check the "Add Python to PATH" box before clicking "Install Now."
4. Follow the prompts to complete installation.

---

### Install on Linux

- **Debian/Ubuntu:**
    ```bash
    sudo apt update
    sudo apt install python3 python3-pip
    ```
- **Fedora:**
    ```bash
    sudo dnf install python3 python3-pip
    ```
- **Other distros:**  
  Use your package manager or refer to your distribution’s documentation.

---

### Install on macOS

1. Install [Homebrew](https://brew.sh/) if not already installed.
2. Open Terminal and run:
    ```bash
    brew install python
    ```
3. Alternatively, download the official installer from [python.org](https://www.python.org/downloads/macos/).


# Manim

[Manim](https://www.manim.community/) (Mathematical Animation Engine) is a robust Python-based library designed for crafting accurate, high-resolution mathematical and scientific animations. Although it gained popularity through *3Blue1Brown’s* educational YouTube channel, Manim is also a versatile tool for illustrating complex ideas in physics, computer science, engineering, and data science.

Creating animations for technical topics can often be time-consuming and difficult, especially when precision is essential. Manim addresses this by allowing developers to generate animations programmatically using Python, enabling fine-grained control over each visual element. This precision helps educators and content creators deliver clear, visually engaging explanations of abstract or complex subjects.

---

## Why Use Manim?

- **Precision**: Built with mathematical accuracy in mind.
- **Customization**: Scriptable in Python, so you can control every aspect.
- **Open-source**: Actively maintained and community-driven.
- **Educational Power**: Helps learners grasp abstract or complex ideas through visual storytelling.

---

## How to Set Up Manim

### Prerequisites

- Python 3.8 or higher  
- Pip (Python’s package installer)  
- Git (Optional but helpful)  
- FFMPEG (For rendering videos)  
- LaTeX (For rendering mathematical expressions)

---

## Installation by OS

### Windows

1. **Install FFMPEG**  
   - Easiest via Chocolatey (if installed):
     ```bash
     choco install ffmpeg
     ```
   - Or download manually: [FFmpeg download](https://ffmpeg.org/download.html)

2. **Create a Virtual Environment (recommended)**  
   ```bash
   python -m venv manim_env
   manim_env\Scripts\activate


3  **Install Manim**

Install via pip

```bash
pip install manim
```

## Test Installation

```bash
manim -h
```

---

### macOS

1. **Install Homebrew (if not already)**

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

2. **Install FFMPEG**

```bash
brew install ffmpeg
```

4 **Install Manim**

```bash
pip install manim
```

---

### Linux (Ubuntu/Debian)

1. **Install dependencies**

```bash
sudo apt update
sudo apt install ffmpeg python3-pip python3-venv
```

2.  **Create and activate virtual environment**

```bash
python3 -m venv manim_env
source manim_env/bin/activate
```

3. **Install Manim**

```bash
pip install manim
```
#  Visualizations

In this sections, a list of animations and how they are created are outlined with links to the slides detailing every step needed for a fully created animation
The animations are grouped into different categories including algorithms and data structures, ........
## Algorithms and Data Structures

Algorithms are step-by-step procedures for solving problems or performing tasks. Key categories include:

- Sorting (QuickSort, MergeSort): Arrange data in order.

- Searching (Binary Search): Find elements in data.

- Traversal (DFS, BFS): Navigate structures like trees or graphs.

- Dynamic Programming & Greedy: Optimize solutions to complex problems.


On the other hand, data structures are ways to organize and store data so it can be accessed and modified efficiently. Common types include:

- Arrays & Lists: Store elements in order.

- Stacks & Queues: Follow specific access rules (LIFO/FIFO).

- Trees & Graphs: Represent hierarchical and networked data.

- Hash Tables: Offer fast lookup using key-value pairs.

This sections will cover the common algorithms and how they are implmented and visualized. 

- A* Pathfinding Algorithm [Link](algorithms_and_data_structures/A_pathfinding_algo/slides.html)





















# How to Run the File to Generate the Animations.

##  1. Ensure Your System Is Up to Date and manim and python are installed successfully. 

###  Windows
Open **Command Prompt** or **PowerShell** and run:
```bash
winget upgrade --all
```

### Ubuntu/Linux
Open Terminal and run:
```bash
sudo apt update && sudo apt upgrade
```

### macOS
Open Terminal and run:
```bash
softwareupdate --all --install --force
```


---

## 💾 3. Save the Script

Save your animation script in a file, for example:
```
filename.py
```
Ensure your class inside the script is named `write your animation name here` (Manim uses this name to render the scene).

---

##  4. Render the Animation

Use the Manim CLI to render the animation:
```bash
manim -pq<quality> filename.py 
```
Replace `<quality>` with your preferred rendering level.

---

### Rendering Quality Options

| Flag  | Quality | Resolution | Speed   | Best For                   |
|-------|---------|------------|---------|----------------------------|
| -pql  | Low     | 480p       | Fast    | Quick development previews |
| -pqm  | Medium  | 720p       | Moderate| Presentations              |
| -pqh  | High    | 1080p      | Slower  | Final output               |

**Example – High Quality Render:**
```bash
manim -pqh bfs.py BFSVisualization
```
- `-p` = preview after render
- `-q` = quality 
- `l, m, h` = low, medium, high respectively

---

##  Output Location

The rendered video will be saved in a directory like:
```
media/videos/bfs/1080p60/
```
You can copy or move the output `.mp4` file as per your need.

---

##  Tips & Customization

- Use `-pql` during development for faster rendering and to safe time.
- Tweak colors, labels, and layout to visualize different algorithms.
- You can also render in 4K with:
    ```bash
    manim -p --format=mp4 --resolution=3840,2160 filename.py
    ```
