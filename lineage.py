#!/usr/bin/env python3
"""Track the ancestral lineage of the quine."""

import re
from pathlib import Path


def build_family_tree():
    """
    Build a family tree of quine generations.
    This script extracts the emoji lineage strings from every generation
    and builds an ASCII family tree in LINEAGE.md to visualize ancestry.
    """
    
    gen_dir = Path("generations")
    
    if not gen_dir.exists():
        return
    
    generations = sorted(gen_dir.glob("gen_*.py"))
    
    tree = []
    
    for gen_file in generations:
        with open(gen_file, "r") as f:
            content = f.read()
        
        # Extract info
        gen_match = re.search(r'Generation (\d+)', content)
        lineage_match = re.search(r'Lineage: (.+)', content)
        
        if gen_match:
            gen_num = int(gen_match.group(1))
            lineage = lineage_match.group(1) if lineage_match else ""
            
            tree.append((gen_num, lineage))
    
    # Create ASCII family tree
    with open("LINEAGE.md", "w") as f:
        f.write("# Quine Garden Lineage\n\n")
        f.write("```\n")
        f.write("Ancestor\n")
        f.write("   |\n")
        
        for i, (gen, lineage) in enumerate(tree):
            if i == 0:
                f.write(f"   └── Gen {gen:3d} {lineage}\n")
            else:
                f.write(f"       {'    ' * (i-1)}└── Gen {gen:3d} {lineage}\n")
        
        f.write("```\n\n")
        f.write(f"Total lineage depth: {len(tree)} generations\n")
    
    print(f"✅ Lineage tree saved to LINEAGE.md")


if __name__ == "__main__":
    build_family_tree()
