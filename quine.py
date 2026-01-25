#!/usr/bin/env python3
"""
Quine Garden - Generation 2
Self-replicating code that evolves based on temporal entropy.
Lineage: 🌷🌷
# Drift: Stable replication
"""

import hashlib
import random
from datetime import datetime

# ASCII art mutations for visual evolution
# This list can be expanded to create more diversity in the lineage
MUTATIONS = ['🌱', '🌿', '🍀', '🌾', '🌳', '🌲', '🌴', '🌵', '🌷', '🌸', '🌹', '🥀', '🌺', '🌻', '🌼', '🌽', '🍄', '🌰', '🎋', '🎍']

# The Template (DNA): This string contains the blueprint for the entire program.
# It uses string formatting (%) to inject its own content back into itself.
template = '''#!/usr/bin/env python3
"""
Quine Garden - Generation %%d
Self-replicating code that evolves based on temporal entropy.
Lineage: %%s
%%s
"""

import hashlib
import random
from datetime import datetime

# ASCII art mutations for visual evolution
# This list can be expanded to create more diversity in the lineage
MUTATIONS = %%r

# The Template (DNA): This string contains the blueprint for the entire program.
template = %%r

# --- EVOLUTION LOGIC ---

# 1. Temporal DNA: Get current time to ensure deterministic yet changing mutations
date_str = datetime.now().strftime("%%%%Y-%%%%m-%%%%d %%%%H:%%%%M")
date_hash = hashlib.sha256(date_str.encode()).hexdigest()
mutation_index = int(date_hash[-2:], 16) %%%% len(MUTATIONS)

# 2. Progressing the Lineage
generation = %%d + 1
lineage = "%%s" + MUTATIONS[mutation_index]

# 3. Deterministic Randomness: Seed the random generator with the time hash
random.seed(date_hash)

# 4. Genetic Drift: Randomly select a descriptive comment for this generation
drift = random.choice([
    "# Drift: Stable replication",
    "# Drift: Minor adaptation", 
    "# Drift: Environmental pressure",
    "# Drift: Mutation success"
])

# 5. The REPRODUCTION: Print the template with all evolved values
# This is the "Magic Moment" where the program prints its own source code.
print(template %%%% (generation, lineage, drift, MUTATIONS, template, generation, lineage))
'''

# --- EVOLUTION LOGIC ---

# 1. Temporal DNA: Get current time to ensure deterministic yet changing mutations
date_str = datetime.now().strftime("%Y-%m-%d %H:%M")
date_hash = hashlib.sha256(date_str.encode()).hexdigest()
mutation_index = int(date_hash[-2:], 16) % len(MUTATIONS)

# 2. Progressing the Lineage
generation = 2
lineage = "🌷🌷"

# 3. Deterministic Randomness: Seed the random generator with the time hash
random.seed(date_hash)

# 4. Genetic Drift: Randomly select a descriptive comment for this generation
drift = random.choice([
    "# Drift: Stable replication",
    "# Drift: Minor adaptation",
    "# Drift: Environmental pressure", 
    "# Drift: Mutation success"
])

# 5. The REPRODUCTION: Print the template with all evolved values
print(template % (generation, lineage, drift, MUTATIONS, template, generation, lineage))
