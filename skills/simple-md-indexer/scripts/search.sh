#!/bin/bash
# Quick search wrapper for markdown files in workspace

CACHE_DIR="$HOME/.cache/simple-md"
INDEX_FILE="$CACHE_DIR/index.json"

if [ ! -f "$INDEX_FILE" ]; then
    echo "Index not found. Run: python3 skills/simple-md-indexer/scripts/indexer.py add <path> <name>"
    exit 1
fi

QUERY="$1"
TOP_K="${2:-10}"

echo "Searching for: '$QUERY'"
echo "========================"

# Use grep to search across all indexed files
python3 -c "
import json
from pathlib import Path

with open('$INDEX_FILE', 'r') as f:
    collections = json.load(f)

files = []
for coll in collections.values():
    files.extend(coll['files'])

# Search each file
query = '''$QUERY'''.lower()
results = []

for file_path in files:
    try:
        with open(file_path, 'r') as f:
            content = f.read().lower()
        
        if query in content:
            score = content.count(query)
            results.append((file_path, score))
    except:
        pass

# Sort by score
results.sort(key=lambda x: x[1], reverse=True)

# Show results
for file_path, score in results[:$TOP_K]:
    print(f'✓ {file_path}')
    print(f'  Matches: {score}')
    print()
"
