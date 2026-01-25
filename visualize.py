#!/usr/bin/env python3
"""Visualize the evolution of the quine garden."""

from pathlib import Path
import re


def analyze_evolution():
    """
    Analyze all generations and create visualization.
    This script combs through the 'generations' directory, calculates code drift
    (size and line count), and builds a bar chart in the terminal and STATISTICS.md.
    """
    
    gen_dir = Path("generations")
    
    if not gen_dir.exists():
        print("No generations found yet")
        return
    
    generations = sorted(gen_dir.glob("gen_*.py"))
    
    if not generations:
        print("No generation files found")
        return
    
    print(f"\n📊 Quine Garden Analysis")
    print(f"{'='*50}\n")
    
    stats = []
    
    for gen_file in generations:
        with open(gen_file, "r") as f:
            content = f.read()
        
        # Extract generation number
        match = re.search(r'Generation (\d+)', content)
        gen_num = int(match.group(1)) if match else 0
        
        # Extract lineage
        lineage_match = re.search(r'Lineage: (.+)', content)
        lineage = lineage_match.group(1) if lineage_match else ""
        
        stats.append({
            'generation': gen_num,
            'lines': len(content.split('\n')),
            'bytes': len(content),
            'lineage': lineage
        })
    
    # Display evolution
    for stat in stats:
        bar = '█' * (stat['lines'] // 5)
        print(f"Gen {stat['generation']:3d}: {bar} ({stat['lines']} lines) {stat['lineage']}")
    
    print(f"\n{'='*50}")
    print(f"Total Generations: {len(stats)}")
    print(f"Size Range: {min(s['bytes'] for s in stats)} - {max(s['bytes'] for s in stats)} bytes")
    
    # Create markdown visualization
    with open("STATISTICS.md", "w") as f:
        f.write("# Quine Garden Statistics\n\n")
        f.write(f"## Evolution Summary\n\n")
        f.write(f"- **Total Generations:** {len(stats)}\n")
        f.write(f"- **Code Size Range:** {min(s['bytes'] for s in stats)} - {max(s['bytes'] for s in stats)} bytes\n")
        f.write(f"- **Lineage Diversity:** {len(set(s['lineage'] for s in stats))} unique patterns\n\n")
        f.write(f"## Generation Timeline\n\n")
        f.write("| Generation | Lines | Size | Lineage |\n")
        f.write("|------------|-------|------|----------|\n")
        
        for stat in stats:
            f.write(f"| {stat['generation']} | {stat['lines']} | {stat['bytes']}B | {stat['lineage']} |\n")
    
    print("\n✅ Visualization saved to STATISTICS.md")


if __name__ == "__main__":
    analyze_evolution()
