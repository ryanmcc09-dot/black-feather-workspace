#!/bin/bash
# Simple workspace search tool

WORKSPACE="${1:-.}"
QUERY="$2"

echo "Searching for: '$QUERY' in $WORKSPACE"
echo "========================================"

grep -r --include="*.md" -l "$QUERY" "$WORKSPACE" 2>/dev/null | while read file; do
    echo "✓ $file"
    grep --include="*.md" -i -m 3 "$QUERY" "$file" 2>/dev/null | head -3
    echo ""
done
