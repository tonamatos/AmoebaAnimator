# 🎬 AmoebaAnimator

This project uses [Manim Community Edition](https://docs.manim.community/) to animate algebraic structures from a custom Python module called `FerGroup`. It is intended as an educational and exploratory tool for visualizing group-theoretic and combinatorial concepts.

The `FerGroup` module is included as a Git submodule and provides all the algebraic objects and logic.

---

## 📦 Setup Instructions

### 1. Clone the Repo (with Submodules)

Make sure you include the `--recurse-submodules` flag:

```bash
git clone --recurse-submodules https://github.com/tonamatos/AmoebaAnimator.git
cd AmoebaAnimator
```

### 2. Create a Virtual Environment

On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

Install the required packages for animation:

```bash
pip install -r requirements.txt`
```

Then install the internal `FerGroup` module in editable mode:

```bash
`pip install -e FerGroup`
```

This lets you edit FerGroup directly without reinstalling.

### 4. Test the Setup
Run a Python session and try importing:

```python
from FerGroup import FerGroup
from manim import *

print(FerGroup)
```

If no error appears, you're good to go!

## 🎞️ How to Render Animations

CLI Usage
From the root folder:

```bash
manim -pql main.py Amoeba_scene
```

`-p`: Open video after rendering
`-ql`: Quick low-quality render

Use `-qm` or `-qh` for higher quality

VS Code Sidepanel (Optional):
1. Install the Manim Sideview extension

2. Open your scene file

3. Select the class to render

4. Click "Render" in the side panel

## 🛠 Updating the FerGroup Submodule

If the `FerGroup` module is updated upstream, pull the changes and update your local copy:

```bash
git submodule update --remote
pip install -e FerGroup
```

## 📁 Project Structure

```java
AmoebaAnimator/
├── FerGroup/            ← Git submodule
│   └── FerGroup/        ← Actual package
├── scenes/              ← Manim scene files
├── requirements.txt     ← Animation dependencies
├── .venv/               ← Virtual environment (not versioned)
└── README.md            ← This file
```

## ✨ Credits
Created by Tonatiuh Matos-[Wiederhold.dev](https://wiederhold.dev) as part of the 2025 Directed Reading Program at the University of Toronto.

Powered by ManimCE and custom algebraic tooling.
