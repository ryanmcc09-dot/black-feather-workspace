# Simple MD Indexer

## Purpose
Lightweight alternative to QMD for indexing and searching markdown files locally. No external dependencies.

## Installation
Already installed in `skills/simple-md-indexer/`

## Usage

### Index Your Workspace
```bash
python3 skills/simple-md-indexer/scripts/indexer.py add ~/.openclaw/workspace organization --mask "**/*.md"
```

### Search
```bash
python3 skills/simple-md-indexer/scripts/indexer.py search "mission revenue streams"
```

### Status
```bash
python3 skills/simple-md-indexer/scripts/indexer.py status
```

### With Collection Filter
```bash
python3 skills/simple-md-indexer/scripts/indexer.py search "architecture" --collection organization --top-k 5
```

## Features
- **No dependencies** - Pure Python, works immediately
- **BM25-style scoring** - Simple keyword matching with relevance ranking
- **Snippet extraction** - Shows context around matches
- **Collections** - Organize files into named collections
- **Cache** - Stores index in `~/.cache/simple-md/`

## Comparison with QMD

| Feature | QMD | Simple MD Indexer |
|---------|-----|-------------------|
| Dependencies | Ollama, native modules | None |
| Speed | Fast with caching | Instant |
| Accuracy | Vector-based (better) | Keyword-based |
| Setup | Complex (native compilation) | Plug-and-play |
| Use case | Production | Quick iteration |

## When to Use

**Simple MD Indexer:**
- Quick file search
- No external dependencies
- Immediate results
- Local workspace navigation

**QMD (when available):**
- Vector search accuracy
- Semantic understanding
- Production workloads
- Advanced reranking

---

*Created: 2026-03-16 as QMD alternative*
