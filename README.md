# Big numbers

A Python repository exploring three famous gargantuan mathematical bounds and fast-growing functions: **Graham's Number ($g_{64}$)**, the **Kirby-Paris Hydra Game ($Hydra_4$)**, and the **`TREE(n)` Sequence ($TREE_3$)**.

All three numbers are finite integers that are so astronomically large that they cannot be written out in standard base-10 notation, exponent towers, or computed on physical hardware.

---

# 📊 Comparative Scale & Growth Hierarchy

| Number / Sequence | Script | Ordinal Bound | Fast-Growing Hierarchy ($FGH$) | Proven In | Status on Physical Hardware |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Graham's Number ($g_{64}$)** | `graham.py` | $\omega + 1$ | $\approx f_{\omega + 1}(64)$ | Peano Arithmetic ($\text{PA}$) | Exceeds recursion depth limit almost immediately |
| **Kirby-Paris $Hydra(4)$** | `hydra.py` | $\varepsilon_0$ | $\approx f_{\varepsilon_0}(4)$ | Second-Order Arithmetic | Execution time exceeds the age of the universe |
| **Kruskal's $TREE(3)$** | `tree.py` | $\Gamma_0$ | $\approx f_{\Gamma_0}(1000)$ | $\text{ATR}_0$ (Transfinite Recursion) | Far transcends $Hydra(4)$ and $g_{64}$ |

---

# 📁 Repository Overview

## 1. Graham's Number (`graham.py`)
Formulated by Ronald Graham in Ramsey theory as an upper bound for hypercube colorings, $g_{64}$ is constructed using Knuth's up-arrow notation ($\uparrow$):

$$g_1 = 3 \uparrow\uparrow\uparrow\uparrow 3 = 3 \uparrow^4 3$$
$$g_n = 3 \uparrow^{g_{n-1}} 3$$
$$g_{64} = \text{Graham's Number}$$

**Usage:**
```bash
python graham.py
```
*Note: Executing `G(64)` will trigger Python's recursion limit due to the sheer depth of nested operations required for $g_1$.*

---

## 2. Kirby-Paris Hydra Game (`hydra.py`)
Introduced by Laurie Kirby and Jeff Paris in 1982, the Hydra Game is played on finite unlabelled rooted trees:
- Hercules chops off a leaf head $h$.
- If $h$'s parent is the root, no new heads grow.
- If $h$'s parent $p$ is not the root, its grandparent $g$ spawns $n$ duplicate copies of the modified parent subtree (where $n$ is the current step number).

Using the standard **`rightmost`** leaf strategy:
- $Hydra(1) = 1$ step
- $Hydra(2) = 3$ steps
- $Hydra(3) = 37$ steps
- **$Hydra(4) > f_{\omega \cdot 2 + 4}(5) \gg \text{Graham's Number}$**

**Usage:**
```bash
python hydra.py
```

---

## 3. Kruskal's `TREE(n)` Sequence (`tree.py`)
`TREE(n)` represents the maximum length of a sequence of $n$-colored rooted trees $T_1, T_2, \dots, T_k$ such that:
1. Each tree $T_i$ contains at most $i$ vertices ($|V(T_i)| \le i$).
2. No previous tree $T_i$ homeomorphically embeds into any subsequent tree $T_j$ ($T_i \le T_j$ for $i < j$) under Kruskal's Tree Theorem.

Known values:
- $TREE(1) = 1$
- $TREE(2) = 3$
- **$TREE(3) \gg Hydra(4) \gg \text{Graham's Number}$**

**Usage:**
```bash
python tree.py
```

---

# ⚡ Execution & Hardware Limitations

All implementations are mathematically exact and algorithmically complete. However, due to the laws of physics and theoretical computation bounds:

1. **`graham.py`**: Triggers a recursion limit when computing $g_1$.
2. **`hydra.py`**: $Hydra(4)$ execution will run indefinitely as step counts dwarf the number of elementary particles in the universe.
3. **`tree.py`**: $TREE(3)$ rapidly exceeds available RAM and stack depth due to the fast-growing size of non-embeddable search trees.

---

# 📚 References & Further Reading

- **Graham's Number**: Graham, R. L.; Rothschild, B. L. (1971). *Ramsey's Theorem for n-parameter sets*.
- **Hydra Game**: Kirby, L.; Paris, J. (1982). *Accessible independence results for Peano arithmetic*.
- **Kruskal's Tree Theorem**: Friedman, H. (1998). *Internal Finite Trees and $\text{TREE}(n)$*.
