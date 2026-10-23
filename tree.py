from functools import lru_cache

class Tree:
    """Class representing a rooted, colored tree."""
    def __init__(self, color: int, children: list = None):
        self.color = color
        # Sort children into canonical order to handle tree isomorphism
        sorted_children = sorted(children or [], key=lambda t: t.to_tuple())
        self.children = tuple(sorted_children)
        self._size = 1 + sum(child.size for child in self.children)
        self._hash = hash((self.color, self.children))

    @property
    def size(self) -> int:
        return self._size

    def to_tuple(self):
        return (self.color, tuple(c.to_tuple() for c in self.children))

    def __eq__(self, other):
        return isinstance(other, Tree) and self.color == other.color and self.children == other.children

    def __hash__(self):
        return self._hash

    def __repr__(self):
        if not self.children:
            return f"T({self.color})"
        return f"T({self.color}, [{', '.join(repr(c) for c in self.children)}])"


@lru_cache(maxsize=None)
def is_embedded(t1: Tree, t2: Tree) -> bool:
    """
    Determines whether tree t1 homeomorphically embeds into tree t2 (Kruskal's Tree Theorem rule).
    t1 <= t2 holds if:
    1. t1 embeds into a subtree of one of t2's immediate children, OR
    2. The roots have matching colors and t1's children can be injectively embedded into t2's children.
    """
    # Case 1: t1 embeds into a lower subtree of t2
    for child2 in t2.children:
        if is_embedded(t1, child2):
            return True

    # Case 2: Root colors match and an injective matching exists among immediate children
    if t1.color == t2.color and len(t1.children) <= len(t2.children):
        if _can_match_children(t1.children, t2.children):
            return True

    return False


def _can_match_children(ch1: tuple, ch2: tuple) -> bool:
    """Maximum Bipartite Matching to verify injective child embedding."""
    adj = []
    for u in ch1:
        neighbors = [j for j, v in enumerate(ch2) if is_embedded(u, v)]
        adj.append(neighbors)

    match = [-1] * len(ch2)

    def dfs(u, visited):
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                if match[v] < 0 or dfs(match[v], visited):
                    match[v] = u
                    return True
        return False

    for u in range(len(ch1)):
        visited = [False] * len(ch2)
        if not dfs(u, visited):
            return False
    return True


@lru_cache(maxsize=None)
def get_trees_of_size(size: int, num_colors: int):
    """Generates all non-isomorphic colored trees of a given vertex count (size)."""
    if size <= 0:
        return []
    if size == 1:
        return [Tree(c) for c in range(num_colors)]

    all_smaller_trees = []
    for s in range(1, size):
        all_smaller_trees.extend(get_trees_of_size(s, num_colors))

    results = []

    def generate_child_combos(rem_size, start_idx):
        if rem_size == 0:
            yield []
            return
        for idx in range(start_idx, len(all_smaller_trees)):
            t = all_smaller_trees[idx]
            if t.size <= rem_size:
                for combo in generate_child_combos(rem_size - t.size, idx):
                    yield [t] + combo

    for c in range(num_colors):
        for children in generate_child_combos(size - 1, 0):
            results.append(Tree(c, children))

    return results


def tree_search(history: tuple, num_colors: int) -> int:
    """
    Recursive tree search: explores all valid candidate continuations at step i
    and returns the maximum remaining sequence length.
    """
    step = len(history) + 1
    candidates = []

    # At step i, the tree size satisfies |V(T_i)| <= step
    for sz in range(1, step + 1):
        for candidate in get_trees_of_size(sz, num_colors):
            # According to the rules, no previous T_j can be embedded into the new candidate
            valid = True
            for prev in history:
                if is_embedded(prev, candidate):
                    valid = False
                    break
            if valid:
                candidates.append(candidate)

    if not candidates:
        return 0  # No valid continuations; sequence terminates on this branch

    max_len = 0
    for candidate in candidates:
        length = tree_search(history + (candidate,), num_colors)
        if length > max_len:
            max_len = length

    return max_len + 1


def TREE(n: int) -> int:
    """Calculates TREE(n) assuming unlimited computational resources."""
    return tree_search((), n)

if __name__ == "__main__":
    # 1. Testing the homeomorphic embedding helper function
    t_single_red = Tree(color=0)                         # Single red vertex
    t_single_blue = Tree(color=1)                        # Single blue vertex
    t_path_blue = Tree(color=1, children=[Tree(color=1)]) # Blue-blue path (2 vertices)

    print("--- Embedding Helper Tests ---")
    print("Is Red embedded into Blue?:", is_embedded(t_single_red, t_single_blue))        # False
    print("Is Blue embedded into Blue-Blue path?:", is_embedded(t_single_blue, t_path_blue)) # True
    print("Is Blue-Blue path embedded into Blue?:", is_embedded(t_path_blue, t_single_blue)) # False

    # 2. Calculating small values of TREE(n)
    print("\n--- TREE Sequence Evaluation ---")
    print(f"TREE(1) = {TREE(1)}")
    print(f"TREE(2) = {TREE(2)}")
    
    # 3. Invoking TREE(3) (Theoretical call)
    # Running TREE(3) will hang indefinitely or exceed recursion limits/memory boundaries.
    print(f"TREE(3) = {TREE(3)}")
