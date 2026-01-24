# Drift: Environmental pressure
#!/usr/bin/env python3
"""
Quine Garden - Generation 1
Self-replicating code that evolves based on temporal entropy.
Lineage: 🥀
"""

import hashlib
import random
from datetime import datetime

# ASCII art mutations for visual evolution
MUTATIONS = ['🌱', '🌿', '🍀', '🌾', '🌳', '🌲', '🌴', '🌵', '🌷', '🌸', '🌹', '🥀', '🌺', '🌻', '🌼', '🌽', '🍄', '🌰', '🎋', '🎍']

template = '#!/usr/bin/env python3\n"""\nQuine Garden - Generation %d\nSelf-replicating code that evolves based on temporal entropy.\nLineage: %s\n"""\n\nimport hashlib\nimport random\nfrom datetime import datetime\n\n# ASCII art mutations for visual evolution\nMUTATIONS = %r\n\ntemplate = %r\n\n# Temporal DNA\ndate_str = datetime.now().strftime("%%Y-%%m-%%d")\ndate_hash = hashlib.sha256(date_str.encode()).hexdigest()\nmutation_index = int(date_hash[-2:], 16) %% len(MUTATIONS)\n\n# Evolution tracking\ngeneration = %d + 1\nlineage = "%s" + MUTATIONS[mutation_index]\n\n# Deterministic mutation seed\nrandom.seed(date_hash)\n\n# Genetic drift: small code variations\ndrift = random.choice([\n    "# Drift: Stable replication",\n    "# Drift: Minor adaptation", \n    "# Drift: Environmental pressure",\n    "# Drift: Mutation success"\n])\n\nprint(f"{{drift}}")\nprint(template %% (generation, lineage, MUTATIONS, template, generation, lineage))\n'

# Temporal DNA
date_str = datetime.now().strftime("%Y-%m-%d")
date_hash = hashlib.sha256(date_str.encode()).hexdigest()
mutation_index = int(date_hash[-2:], 16) % len(MUTATIONS)

# Evolution tracking
generation = 1 + 1
lineage = "🥀" + MUTATIONS[mutation_index]

# Deterministic mutation seed
random.seed(date_hash)

# Genetic drift: small code variations
drift = random.choice([
    "# Drift: Stable replication",
    "# Drift: Minor adaptation", 
    "# Drift: Environmental pressure",
    "# Drift: Mutation success"
])

print(f"{{drift}}")
print(template % (generation, lineage, MUTATIONS, template, generation, lineage))

