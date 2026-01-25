#!/usr/bin/env python3
"""
Quine Garden - Generation 2
Self-replicating code that evolves based on temporal entropy.
Lineage: 🌷🌷
# Drift: Stable replication
# Nature's Note: The garden is blooming exactly as expected, peaceful and calm.
"""

import hashlib
import random
from datetime import datetime

# ASCII art mutations for visual evolution
MUTATIONS = ['🌱', '🌿', '🍀', '🌾', '🌳', '🌲', '🌴', '🌵', '🌷', '🌸', '🌹', '🥀', '🌺', '🌻', '🌼', '🌽', '🍄', '🌰', '🎋', '🎍']

# Non-technical explanations mapping
HUMAN_NOTES = {
    "# Drift: Stable replication": "The garden is blooming exactly as expected, peaceful and calm.",
    "# Drift: Minor adaptation": "A new leaf has sprouted, making the garden a bit more resilient.",
    "# Drift: Environmental pressure": "The garden is feeling the heat, adapting to survive.",
    "# Drift: Mutation success": "A rare flower has bloomed! The garden is stronger than yesterday."
}

# The Template (DNA): This string contains the blueprint for the entire program.
template = '''#!/usr/bin/env python3
"""
Quine Garden - Generation %d
Self-replicating code that evolves based on temporal entropy.
Lineage: %s
%s
%s
"""

import hashlib
import random
from datetime import datetime

# ASCII art mutations for visual evolution
MUTATIONS = %r

# Non-technical explanations mapping
HUMAN_NOTES = %r

# The Template (DNA): This string contains the blueprint for the entire program.
template = %r

# --- EVOLUTION LOGIC ---

# 1. Temporal DNA: Get current time to ensure deterministic yet changing mutations
date_str = datetime.now().strftime("%%Y-%%m-%%d %%H:%%M")
date_hash = hashlib.sha256(date_str.encode()).hexdigest()
mutation_index = int(date_hash[-2:], 16) %% len(MUTATIONS)

# 2. Progressing the Lineage
generation = %d + 1
lineage = "%s" + MUTATIONS[mutation_index]

# 3. Deterministic Randomness: Seed the random generator with the time hash
random.seed(date_hash)

# 4. Genetic Drift: Randomly select a descriptive comment for this generation
drift = random.choice(list(HUMAN_NOTES.keys()))
human_note = f"# Nature's Note: {HUMAN_NOTES[drift]}"

# 5. The REPRODUCTION: Print the template with all evolved values
print(template %% (generation, lineage, drift, human_note, MUTATIONS, HUMAN_NOTES, template, generation, lineage))
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
drift = random.choice(list(HUMAN_NOTES.keys()))
human_note = f"# Nature's Note: {HUMAN_NOTES[drift]}"

# 5. The REPRODUCTION: Print the template with all evolved values
print(template % (generation, lineage, drift, human_note, MUTATIONS, HUMAN_NOTES, template, generation, lineage))
