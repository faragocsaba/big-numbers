# 🌌 Big Numbers & Googology Repository

An interactive web application and Python library exploring physical magnitudes, googology, and fast-growing mathematical functions—from everyday numbers ($10^0$) up to power towers ($10^{10^{10^{100}}}$) and theoretical bounds like **Graham's Number ($g_{64}$)**, the **Kirby-Paris Hydra Game ($Hydra_4$)**, and **Kruskal's $TREE(3)$**.

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MathJax](https://img.shields.io/badge/MathJax-005A9C?style=for-the-badge&logo=math&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)

---

## 📁 Repository Contents

| Component | File | Description |
| :--- | :--- | :--- |
| **Interactive Cockpit** | `index.html` | Web-based visual explorer for orders of magnitude ($10^0$ to $10^{10^{10^{100}}}$) |
| **Graham's Number** | `graham.py` | Knuth's up-arrow notation implementation of $g_{64}$ |
| **Hydra Game** | `hydra.py` | Kirby-Paris tree reduction game and ordinal mapping |
| **Kruskal's TREE** | `tree.py` | Homeomorphic tree embedding algorithm for $TREE(n)$ |

---

## 🎛️ 1. Interactive Web Cockpit (`index.html`)

The interactive web application lets you step through orders of magnitude using an intuitive multi-gear control system.

### Key Features
- **Multi-Gear Navigation**:
  - **Gear 1 (Tower / Exponential Tier)**: Switch between 1-tier linear numbers ($x$), 2-tier exponents ($10^x$), 3-tier towers ($10^{10^x}$), and 4-tier super-towers ($10^{10^{10^x}}$).
  - **Gear 2 (Scale Multiplier)**: Fine-tune step scales ($\times 1$, $\times 10$, $\times 100$).
  - **Accelerator Slider ($x$)**: Adjust values smoothly from $1$ to $10$.
- **🌍 Full Bilingual Support**: Toggle instantly between **Hungarian (HU)** and **English (EN)** in the top bar.
- **📚 Curated Illustration Library**: Examples calibrated strictly to $[A, B)$ order-of-magnitude ranges:
  - **Micro & Macro Physics**: Dust grains, human cell counts, atoms in a sand grain, stars in the Milky Way, observable universe particle counts.
  - **Games & State Spaces**: Complete Rubik's cube series ($1\times1\times1$ to $49\times49\times49$), Chess legal positions, Go game-tree complexity.
  - **Cryptography & Informatics**: IPv4/IPv6 address spaces, MAC addresses, UUIDs, AES-128/256, RSA-512 up to RSA-4096, $32\times32$ icon image spaces.
  - **Thermodynamics & Probability**: Quantum tunneling, Boltzmann brains, atmospheric fluctuations, coffee black hole collapses.
  - **Googology**: Googol, Googolplex, Skewes' number, Poincaré recurrence time.
  - **Historical Inflation**: Hungarian (1946), Yugoslav (1994), and Zimbabwean (2008) hyperinflation figures.

### Web Shortcuts
| Shortcut | Action |
| :--- | :--- |
| <kbd>←</kbd> / <kbd>→</kbd> | Step backward / forward through valid non-overlapping magnitude states |
| <kbd>Home</kbd> | Jump immediately to the base unit ($10^0$) |
| <kbd>End</kbd> | Jump directly to the largest supported magnitude ($10^{10^{10^{100}}}$) |

### Hosting `index.html` Online
Because `index.html` is a standalone, client-side application with zero build requirements, you can host it for free in seconds:
- **GitHub Pages**: Go to **Settings** $\rightarrow$ **Pages** in this repository, select `main` branch, and click **Save**.
- **Netlify Drop**: Drag `index.html` directly onto [Netlify Drop](https://app.netlify.com/drop).
- **Vercel / Cloudflare Pages**: Connect this repository for continuous static hosting.

---

## 🐍 2. Python Fast-Growing Functions

The Python scripts in this repository model three gargantuan mathematical bounds and fast-growing functions that transcend standard notation.

### Comparative Growth Hierarchy

| Number / Sequence | Script | Ordinal Bound | Fast-Growing Hierarchy ($FGH$) | Proven In |
| :--- | :--- | :--- | :--- | :--- |
| **Graham's Number ($g_{64}$)** | `graham.py` | $\omega + 1$ | $\approx f_{\omega + 1}(64)$ | Peano Arithmetic ($\text{PA}$) |
| **Kirby-Paris $Hydra(4)$** | `hydra.py` | $\varepsilon_0$ | $\approx f_{\varepsilon_0}(4)$ | Second-Order Arithmetic |
| **Kruskal's $TREE(3)$** | `tree.py` | $\Gamma_0$ | $\approx f_{\Gamma_0}(1000)$ | $\text{ATR}_0$ (Transfinite Recursion) |

### Usage & Execution

1. **Graham's Number (`graham.py`)**:
   Formulated using Knuth's up-arrow notation ($\uparrow$):
   $$g_1 = 3 \uparrow\uparrow\uparrow\uparrow 3 = 3 \uparrow^4 3$$
   $$g_n = 3 \uparrow^{g_{n-1}} 3$$
   ```bash
   python graham.py
   ```
   *Note: Executing $g_1$ triggers Python's recursion limit due to nested call depth.*

2. **Kirby-Paris Hydra Game (`hydra.py`)**:
   Played on finite unlabelled rooted trees where chopped heads replicate subtrees $n$ times at step $n$:
   - $Hydra(1) = 1$ step
   - $Hydra(2) = 3$ steps
   - $Hydra(3) = 37$ steps
   - **$Hydra(4) > f_{\omega \cdot 2 + 4}(5) \gg \text{Graham's Number}$**
   ```bash
   python hydra.py
   ```

3. **Kruskal's `TREE(n)` Sequence (`tree.py`)**:
   Calculates the maximum length of $n$-colored rooted trees under Kruskal's Tree Theorem:
   - $TREE(1) = 1$
   - $TREE(2) = 3$
   - **$TREE(3) \gg Hydra(4) \gg \text{Graham's Number}$**
   ```bash
   python tree.py
   ```

---

## ⚡ Hardware & Computational Limitations

All Python implementations are mathematically exact and algorithmically complete. However, due to theoretical computational bounds:
1. `graham.py` hits call stack limits when evaluating deep up-arrow recursion.
2. `hydra.py` step count for $Hydra(4)$ far exceeds the number of elementary particles in the observable universe.
3. `tree.py` search for $TREE(3)$ rapidly exceeds physical RAM limits due to exponential non-embeddable tree generation.

---

## 📜 License

This repository is open-source and available under the [MIT License](LICENSE).