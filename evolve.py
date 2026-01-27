#!/usr/bin/env python3
"""
Evolve script for Quine Garden.
Executes the quine, updates the files, and logs the process.
"""

import os
import subprocess
from pathlib import Path
from datetime import datetime

def main():
    print("🧬 Preparing evolution for Quine Garden...")
    
    # 1. Execute quine.py to get next generation code
    try:
        result = subprocess.run(["python3", "quine.py"], capture_output=True, text=True, check=True)
        next_gen_code = result.stdout
    except Exception as e:
        print(f"❌ Error running quine.py: {e}")
        return

    # 2. Extract generation number
    import re
    gen_match = re.search(r'Quine Garden - Generation (\d+)', next_gen_code)
    if not gen_match:
        print("❌ Could not determine generation number from quine output")
        return
    
    gen_num = int(gen_match.group(1))
    print(f"🌱 Evolution complete: Generation {gen_num}")

    # 3. Save new generation to generations/ folder
    gen_dir = Path("generations")
    gen_dir.mkdir(exist_ok=True)
    gen_file = gen_dir / f"gen_{gen_num:03d}.py"
    gen_file.write_text(next_gen_code)
    print(f"💾 Saved record to {gen_file}")

    # 4. Overwrite quine.py with itself (replication)
    Path("quine.py").write_text(next_gen_code)
    print("🔄 quine.py replicated")

    # 5. Run supplementary scripts
    if Path("visualize.py").exists():
        print("🎨 Updating visualizations...")
        subprocess.run(["python3", "visualize.py"])
        
    if Path("lineage.py").exists():
        print("🌳 Updating lineage tree...")
        subprocess.run(["python3", "lineage.py"])
        
    if Path("logger.py").exists():
        print("📝 Logging evolution...")
        subprocess.run(["python3", "logger.py"])

    print(f"✅ Quine Garden generation {gen_num} is now active.")

if __name__ == "__main__":
    main()
