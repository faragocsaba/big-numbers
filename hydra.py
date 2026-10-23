import copy

class HydraNode:
    """Represents a node in the Kirby-Paris Hydra tree."""
    def __init__(self, children=None):
        self.children = children if children is not None else []

    def is_leaf(self) -> bool:
        return len(self.children) == 0

    def copy(self) -> "HydraNode":
        return copy.deepcopy(self)

    def count_heads(self) -> int:
        """Returns the total number of heads (leaves attached above the root)."""
        if not self.children:
            return 0  # A root with no children has 0 heads (Hydra is dead)
        
        def _count(node):
            if node.is_leaf():
                return 1
            return sum(_count(child) for child in node.children)
            
        return sum(_count(child) for child in self.children)

    def count_nodes(self) -> int:
        """Returns total number of nodes including the root."""
        return 1 + sum(child.count_nodes() for child in self.children)

    def to_ordinal_str(self) -> str:
        """Maps the Hydra structure to its Cantor Normal Form ordinal notation (< ε₀)."""
        if not self.children:
            return "0"
            
        child_ordinals = sorted([c.to_ordinal_str() for c in self.children], reverse=True)
        if all(o == "0" for o in child_ordinals):
            return str(len(child_ordinals))
            
        parts = []
        ones_count = 0
        for o in child_ordinals:
            if o == "0":
                ones_count += 1
            else:
                parts.append(f"ω^({o})" if o != "1" else "ω")
                
        if ones_count > 0:
            parts.append(str(ones_count))
            
        return " + ".join(parts)

    def __repr__(self):
        if self.is_leaf():
            return "()"
        return f"({', '.join(repr(c) for c in self.children)})"


def chop_head(root: HydraNode, step: int, head_index: int = 0) -> bool:
    """
    Executes one step of the Hydra game at 1-based step `step`.
    Chops the `head_index`-th leaf and replicates its parent subtree `step` times
    onto the grandparent node (if parent is not the root).
    """
    if not root.children:
        return False  # Hydra is already dead

    paths = []
    
    def find_leaf_paths(node, current_path):
        if node.is_leaf():
            paths.append(current_path)
            return
        for idx, child in enumerate(node.children):
            find_leaf_paths(child, current_path + [idx])

    # Search leaf paths strictly under root's children
    for idx, child in enumerate(root.children):
        find_leaf_paths(child, [idx])
    
    if not paths:
        return False

    if head_index >= len(paths):
        head_index = 0

    target_path = paths[head_index]

    if len(target_path) == 1:
        # Head is a direct child of the root (parent is root) -> no growth
        del root.children[target_path[0]]
    else:
        # Traverse down to grandparent and parent
        gp = root
        for idx in target_path[:-2]:
            gp = gp.children[idx]
        
        parent_idx = target_path[-2]
        parent = gp.children[parent_idx]
        head_idx = target_path[-1]
        
        # 1. Chop head off from parent
        del parent.children[head_idx]
        
        # 2. Attach `step` copies of the modified parent to the grandparent
        for _ in range(step):
            gp.children.append(parent.copy())
            
    return True


def play_hydra(root: HydraNode, strategy: str = "rightmost", verbose: bool = True) -> int:
    """Simulates the Hydra game until defeat is reached."""
    hydra = root.copy()
    step = 1
    if verbose:
        print("--- Initial Hydra ---")
        print(f"Heads: {hydra.count_heads()} | Ordinal: {hydra.to_ordinal_str()} | Structure: {hydra}\n")

    while hydra.count_heads() > 0:
        # Canonical Hydra(n) selects the rightmost leaf (-1)
        head_idx = -1 if strategy == "rightmost" else 0
        chop_head(hydra, step=step, head_index=head_idx)
        if verbose:
            print(f"Step {step:2d} | Heads: {hydra.count_heads():4d} | Ordinal: {hydra.to_ordinal_str():<14} | Structure: {hydra}")
        step += 1

    if hydra.count_heads() == 0:
        if verbose:
            print(f"\nHydra defeated in {step - 1} steps!")
        return step - 1
    else:
        if verbose:
            print(f"\nSimulation stopped (Hydra still alive with {hydra.count_heads()} heads).")
        return -1


if __name__ == "__main__":
    # Example 1: Height 2 Hydra (Root -> Node -> Head) -> Defeated in 3 steps
    print("=== HYDRA 1: Height 2 ===")
    hydra_h2 = HydraNode([HydraNode([HydraNode()])])
    play_hydra(hydra_h2)

    # Example 2: Height 3 Hydra (Root -> Node -> Node -> Head) -> Rapid explosion
    print("\n=== HYDRA 2: Height 3 ===")
    hydra_h3 = HydraNode([HydraNode([HydraNode([HydraNode()])])])
    play_hydra(hydra_h3)

    # Example 3: Height 4 Hydra (Root -> Node -> Node -> Node -> Head) -> greater than Graham's number, so it won't stop
    print("\n=== HYDRA 3: Height 4 ===")
    hydra_h4 = HydraNode([HydraNode([HydraNode([HydraNode([HydraNode()])])])])
    play_hydra(hydra_h4, verbose=False)
