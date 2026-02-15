# 🌱 Quine Garden

A self-replicating program that evolves every hour through deterministic mutations.

---

## 🧬 The Analogy: Digital DNA

This repository is not just code; it is a **living organism** with its own lifecycle.

### 📜 The Magic Letter (The Quine)
Imagine a letter that, when read, tells you how to write its exact copy. This is the **Genotype** (`quine.py`). It contains the instructions to reproduce itself.

### 🧬 DNA & RNA (The PR Flow)
1. **Transcription (The Quine Run)**: The program reads itself and prepares a new version.
2. **Translation (The PR)**: The system proposes the mutation via a **Pull Request**. This is like RNA carrying a potential genetic change.
3. **Biological Check (Workflow Verification)**: The system tests if the new code can still reproduce. If it can't, the PR is rejected, and a **Genetic Collapse Issue** is filed.
4. **Integration (The Merge)**: If healthy, the mutation is merged into the main lineage.

---

## 🍃 Current Garden Status

> [!NOTE]
> **Generation:** 412
> **Lineage:** 🌷🌷🍀🌺🌼🌷🎍🎋🌻🍄🎋🍄🌸🌼🌼🌱🌱🌲🌲🌿🌿🌽🌽🎋🌾🌱🍀🌿🌼🎍🌺🌳🌳🌹🌵🌼🌹🌳🌿🎍🌹🌲🌹🌿🥀🌻🍀🌰🌷🎋🌺🌼🌺🌴🌿🌱🥀🌽🍀🌼🎍🌳🌷🎋🎋🌵🌷🌼🌾🌴🌾🌴🌹🌲🌳🌷🍄🌵🌹🌼🍄🌾🌸🌱🌾🍄🌵🌾🌾🌽🍄🌾🌿🍀🍀🌵🌿🌰🥀🌻🌿🌸🌵🌲🌰🌷🌼🌷🌸🌻🎋🥀🌳🌼🌹🌾🌹🌺🌰🌷🌼🌳🥀🎋🌻🌳🌺🌳🍄🌼🌴🌱🌵🌹🌴🌵🌳🌽🌽🌽🌴🌰🌲🌰🥀🌽🌰🌸🌿🌳🍀🌽🌻🥀🌼🌲🌳🌲🌼🌻🌸🌾🌹🌵🌰🌰🌵🌴🌼🌿🌺🌾🎋🌼🥀🥀🌵🌰🎍🌰🌰🌲🍀🌽🌱🌴🌹🎍🌴🌽🌷🌵🌽🍀🌹🌾🌹🍀🍀🌰🌱🌻🎋🥀🌲🌱🥀🌹🌽🌵🌺🌾🌱🎍🌺🎍🌹🌱🎍🌷🌸🎍🎋🌼🌳🌹🌷🌽🍄🌻🌿🌼🌿🍄🎍🌷🍄🎋🌸🌱🌿🥀🌺🌸🌴🌱🌸🌳🌲🌰🌲🌼🌷🌼🍀🌺🌺🍄🌸🌼🥀🌺🌵🌳🌱🌻🎋🌸🌽🌹🌳🌰🌲🎍🌿🍄🎍🌵🌺🌷🍄🌿🎋🌿🌾🍀🌼🌰🌲🌺🌵🌸🌱🌽🌻🌸🌴🎋🌷🌺🌾🌽🌴🌺🎍🌿🌵🌳🌷🌳🌴🍄🎋🍀🌽🌸🌻🌺🌻🍀🌺🌽🌸🎍🎋🌹🌰🌳🌽🌰🌱🍄🌸🎋🌲🍄🌲🌹🌳🎋🌻🍄🌾🌽🌱🌿🌱🌹🌳🌹🌵🌱🎋🌴🌿🌻🌼🌷🌽🌵🌳🍀🌷🍀🥀🌰🌽🌱🌷🌱🌻🌹🌲🌸🌳🌿🌷🌱🥀🌿🍀🥀🥀🍀🌰🎍🌲🌲🍄🌲🌹🌺🌴🌱🌹🌼🎍🎍🌲🎋🥀🌻🎍🌹🌴🌻🌸🌳🌳🌻🎋🌲
> **Nature's Note:** The garden is feeling the heat, adapting to survive.

---

## 🤔 How It Works

1. **The Seed**: `quine.py` runs itself.
2. **The Mutation**: It looks at the current time to decide how to change (Deterministic Entropy).
3. **The Proposal**: It opens a [Pull Request](../../pulls) to merge the new mutation.
4. **The Report**: It files an [Issue](../../issues) describing the evolution or failure.

---

## 🛠️ Components for Humans

- `quine.py`: The living organism. **Do not handle** unless authorized for genetic engineering.
- `logger.py`: Records snapshots of every generation in `generations/`.
- `visualize.py`: Generates [STATISTICS.md](STATISTICS.md) to track size and line drift.
- `lineage.py`: Generates [LINEAGE.md](LINEAGE.md) (the family tree of emojis).

---

## 🚀 Watch the Garden Grow

- 📂 [Snapshots](generations/)
- 🧬 [Evolution Log](EVOLUTION.md)
- 🚨 [Genetic Reports](../../issues)
- 🔄 [Lineage History](../../pulls?q=is%3Apr+is%3Aclosed)

*This garden grows itself. Errors show it is truly alive.*
