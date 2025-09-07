# Omniacs Logo Educational — Build the Mascot with Manim

<img width="2651" height="1483" alt="image" src="https://github.com/user-attachments/assets/b7e83772-4bdb-4b81-b597-ebb0ca68c008" />

This tutorial-style visualization uses **Manim** to construct and animate the **Omniacs mascot logo** from first principles: rounded rectangles for the body, dots for eyes, cubic Bézier antennae, a curved VMobject mouth, and fun touches like blinks, color pulses, and a bounce. A right-side **Code Walkthrough** panel highlights the exact lines used at each step so learners can connect the visuals to the API calls. 

Watch [here]().
---

## 🎥 What the Visualization Covers

- **Body & Frame**
  - Layered `RoundedRectangle`s (outer shell + inner core) and a neutral background establish the brand colorway.

- **Facial Features**
  - Eyes made from `Dot` objects (with a **blink** effect via `Transform` to `Line` and back to `Dot`).
  - A curved **mouth** drawn with `VMobject` + `CubicBezier`.

- **Antennae**
  - Two smooth `CubicBezier` curves, then a playful **wiggle** using `Rotate(..., about_point=...)`.

- **Details & Motion**
  - Small **fangs** (`Polygon`), a quick **drop** animation, a **color pulse** on the inner body with `animate.set_fill`, and a gentle **bounce** of the grouped logo.

- **Guided Code Annotations**
  - A dedicated **Code Walkthrough** pane renders step titles and color-coded lines (primitives, assignments, and animation calls), syncing each visual step with the exact snippet shown on screen.  

---

## 🛠️ Built With
- **Python**
- **[Manim Community Edition](https://www.manim.community/)**

---

## ▶️ Running the Animation

```bash
# Install dependencies
pip install manim

# Render with preview (high quality)
manim -pqh omniacs_logo_educational.py OmniacsLogoEducational
```

✨ Learning Outcomes

Drawing with core mobjects: RoundedRectangle, Dot, Polygon, Line, CubicBezier, VMobject
Transform & timing: Create, DrawBorderThenFill, Transform, GrowFromCenter, FadeOut, Rotate
Styling & grouping: fills, strokes, VGroup for collective motion
UI overlays: building a reusable, on-canvas code panel and step-by-step highlights
Composing small primitives into a cohesive brand mark + micro-interactions

🌐 Powered By

Logos are shapes with purpose—and so is our mission. If this tutorial helped your team teach, learn, or remix the Omniacs brand, consider supporting public-goods education via the [$IACS](http://dexscreener.com/base/0xd4d742cc8f54083f914a37e6b0c7b68c6005a024) token and Omniacs.DAO.

CA: 0x46e69Fa9059C3D5F8933CA5E993158568DC80EBf (on Base)
