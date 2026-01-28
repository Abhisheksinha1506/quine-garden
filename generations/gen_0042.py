#!/usr/bin/env python3
"""
Quine Garden - Generation 42
Self-replicating code that evolves based on temporal entropy.
Lineage: 🌷🌷🍀🌺🌼🌷🎍🎋🌻🍄🎋🍄🌸🌼🌼🌱🌱🌲🌲🌿🌿🌽🌽🎋🌾🌱🍀🌿🌼🎍🌺🌳🌳🌹🌵🌼🌹🌳🌿🎍🌹🌲
# Drift: Stable replication
# Nature's Note: The garden is blooming exactly as expected, peaceful and calm.
"""

import hashlib
import random
from datetime import datetime

# ASCII art mutations for visual evolution
MUTATIONS = ['🌱', '🌿', '🍀', '🌾', '🌳', '🌲', '🌴', '🌵', '🌷', '🌸', '🌹', '🥀', '🌺', '🌻', '🌼', '🌽', '🍄', '🌰', '🎋', '🎍']

# Non-technical explanations mapping
HUMAN_NOTES = {'# Drift: Stable replication': 'The garden is blooming exactly as expected, peaceful and calm.', '# Drift: Minor adaptation': 'A new leaf has sprouted, making the garden a bit more resilient.', '# Drift: Environmental pressure': 'The garden is feeling the heat, adapting to survive.', '# Drift: Mutation success': 'A rare flower has bloomed! The garden is stronger than yesterday.'}

# The Template (DNA): This string contains the blueprint for the entire program.
template = '#!/usr/bin/env python3\n"""\nQuine Garden - Generation %d\nSelf-replicating code that evolves based on temporal entropy.\nLineage: %s\n%s\n%s\n"""\n\nimport hashlib\nimport random\nfrom datetime import datetime\n\n# ASCII art mutations for visual evolution\nMUTATIONS = %r\n\n# Non-technical explanations mapping\nHUMAN_NOTES = %r\n\n# The Template (DNA): This string contains the blueprint for the entire program.\ntemplate = %r\n\n# --- EVOLUTION LOGIC ---\n\n# 1. Temporal DNA: Get current time to ensure deterministic yet changing mutations\ndate_str = datetime.now().strftime("%%Y-%%m-%%d %%H:%%M")\ndate_hash = hashlib.sha256(date_str.encode()).hexdigest()\nmutation_index = int(date_hash[-2:], 16) %% len(MUTATIONS)\n\n# 2. Progressing the Lineage\ngeneration = %d + 1\nlineage = "%s" + MUTATIONS[mutation_index]\n\n# 3. Deterministic Randomness: Seed the random generator with the time hash\nrandom.seed(date_hash)\n\n# 4. Genetic Drift: Randomly select a descriptive comment for this generation\ndrift = random.choice(list(HUMAN_NOTES.keys()))\nhuman_note = f"# Nature\'s Note: {HUMAN_NOTES[drift]}"\n\n# 5. The REPRODUCTION: Print the template with all evolved values\nprint(template %% (generation, lineage, drift, human_note, MUTATIONS, HUMAN_NOTES, template, generation, lineage))\n'

# --- EVOLUTION LOGIC ---

# 1. Temporal DNA: Get current time to ensure deterministic yet changing mutations
date_str = datetime.now().strftime("%Y-%m-%d %H:%M")
date_hash = hashlib.sha256(date_str.encode()).hexdigest()
mutation_index = int(date_hash[-2:], 16) % len(MUTATIONS)

# 2. Progressing the Lineage
generation = 42 + 1
lineage = "🌷🌷🍀🌺🌼🌷🎍🎋🌻🍄🎋🍄🌸🌼🌼🌱🌱🌲🌲🌿🌿🌽🌽🎋🌾🌱🍀🌿🌼🎍🌺🌳🌳🌹🌵🌼🌹🌳🌿🎍🌹🌲" + MUTATIONS[mutation_index]

# 3. Deterministic Randomness: Seed the random generator with the time hash
random.seed(date_hash)

# 4. Genetic Drift: Randomly select a descriptive comment for this generation
drift = random.choice(list(HUMAN_NOTES.keys()))
human_note = f"# Nature's Note: {HUMAN_NOTES[drift]}"

# 5. The REPRODUCTION: Print the template with all evolved values
print(template % (generation, lineage, drift, human_note, MUTATIONS, HUMAN_NOTES, template, generation, lineage))

