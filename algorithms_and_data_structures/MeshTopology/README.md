# 🖧 Mesh Topology Network Animation in 3D | Manim Visualization

This Manim project visualizes a **Mesh Network Topology** in an animated 3D scene. It features PCs, routers, a main server, and animated data flow — complete with labeled components, bandwidth-colored connections, and dynamic camera motion.

![Animation Preview](preview.png)

[Watch here!](https://youtu.be/FUSwohtw9iA)

## 🔌 What’s Shown

- 💻 **10 PCs** arranged in a circular layout
- 🔴 **2 Routers** raised above the PCs
- 🟩 **Main Server** represented as a 3D pyramid
- 🔗 **Bandwidth connections** between PCs, routers, and server
- ✉️ **Data packets** animate from PC → Router → Server
- 🎥 Smooth camera orbit and transitions

## 🧩 Visual Elements

| Component | Description |
|-----------|-------------|
| **PCs**   | Blue cubes labeled PC1–PC10 |
| **Routers** | Red spheres labeled R1 & R2 |
| **Server** | Green pyramid labeled "Main Server" |
| **Connections** | Lines with color/thickness representing bandwidth:  
  - High (Orange, thick)  
  - Medium (Yellow, medium)  
  - Low (Light Blue, thin)|


|  |  |
|-----------|-------------|
| **Packets** | White spheres that simulate data moving through the network |
| **Camera** | Ambient and directed 3D rotations to showcase all angles |

## 🎓 What You’ll Learn

- Basic mesh networking structure
- Node relationships: end devices, routers, and servers
- Bandwidth-aware visual representation
- Coordinated 3D animation in educational visualization

## 📦 Requirements

- Python 3.8+
- Manim Community Edition
- NumPy

```bash
pip install manim numpy
```

▶️ How to Run

```bash
manim -pql MeshTopology.py MeshTopologyAnimation
```
Use -qh for high-resolution output.
📁 Files

    MeshTopology.py — Main animation logic

    README.md — This documentation



---
🤝 Support Network Visualization & Open Source Education
*Maintained with ❤️ by **Omniacs.DAO** – accelerating digital public goods through data.*

🛠️ Keep public infrastructure thriving. Buy [$IACS](http://dexscreener.com/base/0xd4d742cc8f54083f914a37e6b0c7b68c6005a024) on Base — CA: 0x46e69Fa9059C3D5F8933CA5E993158568DC80EBf

