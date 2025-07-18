# 🧠 Neural Network Visualization (Manim Animation)

This Manim animation illustrates how a simple **feedforward neural network** operates — from structure to learning. The scene walks the viewer through core steps in machine learning including forward passes, error correction via backpropagation, and prediction with updated weights. Each part of the animation is synced to clear visual motion, highlighting how data and gradients flow through an artificial neural network.

<img width="1869" height="1059" alt="image" src="https://github.com/user-attachments/assets/ad0e720f-d3cb-4a5f-8f40-f538c8628fdb" />

Watch the video [here](https://youtu.be/9QCifx4MIoQ).

---

## 🎬 Animation Breakdown

| Section                     | Duration | Description |
|----------------------------|----------|-------------|
| Network Structure Intro    | 0:05–0:20  | Shows 4-layer architecture (Input → Hidden → Hidden → Output) |
| Forward Pass               | 0:20–0:45  | Pulses data through layers, highlights output |
| Learning Process           | 0:45–1:10  | Shows error signals, backpropagation, and weight updates |
| Prediction Demo            | 1:10–1:25  | Demonstrates how network makes new prediction |
| Finale + Credits           | 1:25–1:30  | Network pulse, fadeout, and credit roll |

---

## 🧩 Key Features

- **Layered structure** with dynamic layout for [4, 6, 6, 3] neuron configuration  
- **Animated connections** with color/opacity reflecting weights and updates  
- **Forward signal propagation** using animated dots  
- **Backpropagation** showing error signal flow and weight adjustments  
- **Prediction highlight** with output victory animation  
- **Elegant finale** pulsing all network elements in sync  
- **Visual credit roll** with icons and attributions

---

## 🚀 How to Run

Make sure you have Manim Community Edition installed:

```bash
pip install manim

Then render the animation:

manim -pql neural_network.py NeuralNetworkVisualization

Use -qh instead of -pql for high-quality output.
```

💡 Educational Value

This animation is ideal for:

    Teaching the fundamentals of how neural networks work
    Visual learners grasping signal flow and backpropagation
    Supplementing lectures on machine learning or AI logic
    Creating explainers for YouTube, MOOCs, or interactive lessons

###
💸 Support Our Work

Did you find this repo useful? Support more open-source education by acquiring some $IACS on Base:
$IACS Token CA: 0x46e69Fa9059C3D5F8933CA5E993158568DC80EBf
