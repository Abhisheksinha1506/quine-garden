# 🌱 Quine Garden

A self-replicating program that evolves every hour through deterministic mutations.

---

## 📖 The Analogy: The Magic Letter

Imagine a **magic letter** that, when you read it out loud, **tells you how to write an identical copy of itself**.

Now imagine that letter **slowly mutates** each hour - changing one word here, one emoji there - but it **still knows how to copy itself** even after mutating.

That is exactly what this repository is: **Living Code**.

---

## 🤔 What's a Quine?

A **Quine** is a computer program which takes no input and produces a copy of its own source code as its only output. 

### In this Garden:
1. **The Seed**: `quine.py` runs itself.
2. **The Mutation**: It looks at the current time to decide how to change.
3. **The Growth**: It overwrites itself with a new, slightly different version.
4. **The Fruit**: It creates a snapshot, updates logs, and even **files an Issue** to report its drift.

---

##  Current Status

- **Generation:** Check `quine.py` header
- **Evolution Log:** See [EVOLUTION.md](EVOLUTION.md)
- **Snapshots:** Browse [generations/](generations/)
- **Reports:** Check the [Issues](../../issues) tab for "Evolution Reports"!

## 🛠️ Components for Humans

- `quine.py`: The actual living organism. **Do not edit manually** unless you want to interfere with evolution!
- `logger.py`: The gardener that records snapshots of every generation.
- `visualize.py`: Generates [STATISTICS.md](STATISTICS.md) to show how the code is drifting over time.
- `lineage.py`: Generates [LINEAGE.md](LINEAGE.md) (the family tree of emojis).

---

## 🚀 How to Setup Your Own

1. Fork this repo.
2. Go to **Actions** -> **Genesis - Plant the Seed** -> **Run workflow**.
3. Watch the garden grow every hour!

*This garden grows itself. We are just the observers.*
