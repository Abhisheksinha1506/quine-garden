# 🌱 Quine Garden

A self-replicating program that evolves every 15 minutes through deterministic mutations.

## What is this?

This repository contains a **quine** - a program that outputs its own source code.
Every day, the quine:
1. Runs itself
2. Mutates slightly based on the current time (every 15 minutes)
3. Replaces itself with the mutated version
4. The cycle continues

## Current Status

- **Generation:** Check `quine.py` header
- **Evolution Log:** See [EVOLUTION.md](EVOLUTION.md)
- **Snapshots:** Browse [generations/](generations/)

## How It Works

The quine uses the current date as a seed for deterministic mutations:
- Hash of date determines mutation type
- Generation counter tracks evolution
- Lineage emoji string shows ancestry
- Core self-replication stays intact

## Watch the Garden Grow

- 📊 [Evolution Log](EVOLUTION.md)
- 📂 [All Generations](generations/)
- 🔄 [Commit History](../../commits/main)

---

*This garden grows itself. No human intervention needed.*
