#!/usr/bin/env python3
"""Log each generation of the quine."""

import subprocess
from datetime import datetime
from pathlib import Path


def log_generation():
    """
    Log current quine generation to history.
    This function reads the living quine, extracts its generation number,
    saves a snapshot for posterity, and updates the evolution log.
    Includes both technical details and non-technical explanations.
    """
    
    # Read current quine
    with open("quine.py", "r") as f:
        quine_code = f.read()
    
    # Extract generation number
    generation = 1
    drift = ""
    human_note = ""
    for line in quine_code.split('\n'):
        if "Generation" in line:
            try:
                parts = line.split("Generation")
                if len(parts) > 1:
                    generation = int(parts[1].strip().split()[0])
            except (ValueError, IndexError):
                pass
        if line.strip().startswith("# Drift:") and not drift:
            drift = line.strip()
        if line.strip().startswith("# Nature's Note:") and not human_note:
            human_note = line.split("Nature's Note:")[1].strip()
    
    # Create generations directory
    gen_dir = Path("generations")
    gen_dir.mkdir(exist_ok=True)
    
    # Save snapshot
    snapshot_file = gen_dir / f"gen_{generation:04d}.py"
    with open(snapshot_file, "w") as f:
        f.write(quine_code)
    
    # Update evolution log
    log_file = Path("EVOLUTION.md")
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
    
    entry = f"""
## Generation {generation}

- **Date:** {timestamp}
- **File:** `generations/gen_{generation:04d}.py`
- **Technical Status:** `{drift}`
- **Nature's Note:** *{human_note}*
- **Stats:** {len(quine_code.split(chr(10)))} lines, {len(quine_code)} bytes

```python
{quine_code[:200]}...
```

---
"""
    
    if log_file.exists():
        with open(log_file, "a") as f:
            f.write(entry)
    else:
        with open(log_file, "w") as f:
            f.write("# Quine Garden Evolution Log\n\n")
            f.write("Tracking the evolution of self-replicating code.\n\n")
            f.write(entry)
    
    print(f"✅ Logged generation {generation}")


if __name__ == "__main__":
    log_generation()
