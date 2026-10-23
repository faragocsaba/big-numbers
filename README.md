# TREE(n) Sequence Evaluator in Python

An exact algorithmic implementation of the **`TREE(n)`** fast-growing mathematical sequence in Python, powered by **Kruskal's Tree Theorem** and homeomorphic tree embedding.

---

## 📌 Overview

The `TREE(n)` sequence stems from finite combinatorics and graph theory. It represents the maximum length of a sequence of rooted, colored trees $T_1, T_2, \dots, T_k$ built from $n$ available colors such that:

1. Each tree $T_i$ has at most $i$ vertices (i.e., $|V(T_i)| \le i$).
2. No tree $T_j$ ($j < i$) homeomorphically embeds into a later tree $T_i$ ($T_j \le T_i$).

By Kruskal's Tree Theorem, every such sequence must terminate. However, the sequence grows at an unimaginably fast rate:
* $TREE(1) = 1$
* $TREE(2) = 3$
* $TREE(3)$ is an astronomically large number that vastly exceeds Graham's number or $TREE(2)^{TREE(2)}$.

This repository provides an algorithmic solver that computes $TREE(1)$ and $TREE(2)$ and contains the complete recursive logic required to evaluate $TREE(n)$ given unbounded computational time and memory.

---

## 🛠️ Features

* **Tree Representation (`Tree`):** Immutable, hashable class for rooted trees with color annotations and canonical child ordering to handle graph isomorphism.
* **Homeomorphic Embedding Detector (`is_embedded`):** Tests if $T_1 \le T_2$ using recursive subtree matching and maximum bipartite matching for sibling subtrees.
* **Non-Isomorphic Tree Generator (`get_trees_of_size`):** Generates all unique rooted colored trees up to size $k$.
* **Recursive Search Engine (`tree_search`):** Explores all valid tree continuations at step $i$ to compute the exact maximum sequence length.

---

## 🚀 Getting Started

### Prerequisites

* Python 3.8 or higher.
* No external third-party dependencies required (uses standard library utilities like `functools.lru_cache`).

### Usage

Clone the repository and run the script directly:

```bash
git clone https://github.com/your-username/tree-n-python.git
cd tree-n-python
python tree_n.py
```

### Sample Output

```text
--- Embedding Helper Tests ---
Is Red embedded into Blue?: False
Is Blue embedded into Blue-Blue path?: True
Is Blue-Blue path embedded into Blue?: False

--- TREE Sequence Evaluation ---
TREE(1) = 1
TREE(2) = 3
```

> **Note on $TREE(3)$:** Calling `TREE(3)` in the code will not complete on physical hardware due to recursion depth and memory limitations. The algorithm is theoretically correct, but physical execution exceeds the lifespan of the universe.

---

## 🔬 How the Embedding Works

The homeomorphic embedding condition $T_1 \le T_2$ is evaluated as follows:

1. **Subtree Match:** $T_1$ embeds into $T_2$ if $T_1$ embeds into any child subtree of $T_2$.
2. **Root Match:** If the root colors of $T_1$ and $T_2$ are identical, $T_1$ embeds into $T_2$ if the children of $T_1$ can be injectively mapped into the children of $T_2$ such that each child of $T_1$ embeds into its corresponding matched child in $T_2$.

Maximum Bipartite Matching (via Depth-First Search) is used to verify injective child mappings efficiently.

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.