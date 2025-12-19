# Delaunay Triangulation Visualization

An elegant Manim animation that demonstrates the construction and properties of Delaunay triangulation, a fundamental algorithm in computational geometry.

## Overview

This visualization shows how to create an optimal mesh from a set of scattered points by connecting them into triangles that avoid skinny shapes and maximize minimum angles.

## What is Delaunay Triangulation?

**Delaunay triangulation** is a way to connect a set of points into triangles such that no point lies inside the circumcircle of any triangle. This property ensures high-quality triangles.

### The Delaunay Property

> **No point lies inside the circumcircle of any triangle**

This constraint guarantees:
- ✓ Maximizes minimum angle in triangles
- ✓ Avoids skinny, elongated triangles
- ✓ Unique solution for non-degenerate point sets

## Key Concepts

### Circumcircle
- A circle that passes through all three vertices of a triangle
- Has its center equidistant from all three vertices
- Used to verify the Delaunay property

### Voronoi Diagram Connection
- Delaunay triangulation is the dual graph of the Voronoi diagram
- Each edge in the triangulation connects two points whose Voronoi regions share a boundary

## Algorithm Visualization

### Step 1: Scatter Points
- Generate random points in the plane
- Include corner points to ensure complete coverage
- Display all points with visual markers

### Step 2: Build Triangulation
- Create triangles iteratively
- Show each triangle being formed
- Highlight the three vertices being connected
- Display circumcircle for early triangles

### Step 3: Verify Properties
- Check that no points lie inside circumcircles
- Ensure triangulation is complete
- Visualize the final mesh

## Implementation Details

### Point Generation
```python
- 4 corner points for boundary
- 8+ random interior points
- Seeded random generation for reproducibility
```

### Triangle Construction
- Uses `scipy.spatial.Delaunay` for computational geometry
- Iterative visualization of simplex formation
- Color-coded edges and fills

### Circumcircle Calculation
```python
def calculate_circumcircle(p1, p2, p3):
    # Computes center and radius
    # Returns circle passing through all 3 points
```

## Real-World Applications

### ✓ Terrain & Surface Modeling
- **Digital Elevation Models (DEM)**: Representing terrain height
- **3D Scanning**: Mesh generation from point clouds
- **Geographic Mapping**: Creating continuous surfaces from survey points

### ✓ Finite Element Analysis (FEM)
- **Engineering Simulations**: Structural analysis
- **Fluid Dynamics**: Computational fluid dynamics (CFD)
- **Heat Transfer**: Thermal analysis

### ✓ Computer Graphics & Games
- **Mesh Generation**: 3D model creation
- **Texture Mapping**: UV coordinate generation
- **Level of Detail (LOD)**: Adaptive mesh refinement

### ✓ Mesh Generation
- **CAD/CAM**: Computer-aided design
- **Medical Imaging**: 3D reconstruction
- **Scientific Visualization**: Data visualization

## Properties & Advantages

### Mathematical Properties
1. **Angle Optimization**: Maximizes the minimum angle
2. **Uniqueness**: Unique for non-collinear points
3. **Local Property**: Can be computed locally
4. **Stability**: Robust to point perturbations

### Practical Advantages
- **Quality Triangles**: Avoids long, thin triangles
- **Efficient**: O(n log n) expected time
- **Incremental**: Can add/remove points dynamically
- **Well-Conditioned**: Numerical stability

## 📦 Requirements

### System Requirements
- **Python 3.8+**
- **Manim Community Edition**
- **NumPy**
- **SciPy**

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

#### Step 3: Install Required Libraries
```bash
pip install numpy scipy
```

### Verify Installation
```bash
manim --version
python -c "import numpy, scipy; print('NumPy & SciPy installed successfully')"
```

## Running the Animation

### Basic Execution (Low Quality - Fast)
```bash
manim -pql delaunaytriangulation.py DelaunayTriangulation
```

### High Quality Render
```bash
manim -pqh delaunaytriangulation.py DelaunayTriangulation
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
- `DelaunayTriangulation(Scene)`: Primary scene class

### Configuration
```python
config = {
    'point_count': 12,
    'point_radius': 0.08,
    'colors': {
        'point': BLUE,
        'highlight': YELLOW,
        'triangle': TEAL,
        'circumcircle': RED,
        ...
    }
}
```

### Key Methods

#### Scene Methods
- `show_title()`: Introduction sequence
- `generate_points()`: Creates point set
- `display_points()`: Animates point appearance
- `explain_algorithm()`: Describes Delaunay property
- `build_triangulation_stepwise()`: Constructs mesh
- `show_final_properties()`: Summary and applications

#### Geometric Methods
- `calculate_circumcircle()`: Computes circumcircle parameters
- `show_circumcircle_brief()`: Visualizes circumcircle

## Animation Features

### Visual Elements
- Smooth point appearance with lag
- Triangle construction with edge animation
- Circumcircle visualization for selected triangles
- Color-coded highlights
- Progress counter during construction

### Text Elements
- Step-by-step explanations
- Property descriptions
- Application showcases
- Credits section

## Mathematical Details

### Circumcircle Formula
For triangle with vertices (ax, ay), (bx, by), (cx, cy):

```
Center (ux, uy) where:
d = 2(ax(by - cy) + bx(cy - ay) + cx(ay - by))
ux = ((ax² + ay²)(by - cy) + ...) / d
uy = ((ax² + ay²)(cx - bx) + ...) / d
radius = ||p1 - center||
```

## Educational Value

Perfect for:
- Computational geometry courses
- Computer graphics education
- Finite element method training
- Mesh generation learning
- Algorithm visualization

## Performance Characteristics

- **Time Complexity**: O(n log n) average case
- **Space Complexity**: O(n)
- **Triangle Count**: ~2n for n points (typical)
- **Edge Count**: ~3n for n points (typical)

## Tips for Customization

1. **Point Count**: Adjust `self.point_count`
2. **Animation Speed**: Modify `run_time` parameters
3. **Colors**: Update `self.colors` dictionary
4. **Region**: Change `y_range` in `generate_points()`

## Comparison to Other Triangulations

| Property | Delaunay | Arbitrary |
|----------|----------|-----------|
| Angle Quality | Optimal | Variable |
| Uniqueness | Yes* | No |
| Computation | O(n log n) | O(n²) |
| Applications | Many | Limited |

*For non-degenerate point sets

## Further Reading

- Delaunay, B. (1934). "Sur la sphère vide"
- "Computational Geometry" by de Berg et al.
- Fortune's algorithm for Voronoi diagrams

---

## 🤝 Support Algorithmic Education

Maintained with ❤️ by Omniacs.DAO – accelerating digital public goods through data.

🛠️ Keep public infrastructure thriving. Buy $IACS on Base — CA: 0x46e69Fa9059C3D5F8933CA5E993158568DC80EBf
