#!/usr/bin/env python3
"""
Simple MD Indexer - Alternative to QMD for local markdown file search.
Uses basic BM25-style ranking without external dependencies.
"""

import os
import re
import json
from pathlib import Path
from typing import List, Dict, Tuple


class SimpleMDIndexer:
    """Basic markdown file indexer with search capability."""

    def __init__(self, cache_dir: str = "~/.cache/simple-md"):
        self.cache_dir = Path(cache_dir).expanduser()
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.index_file = self.cache_dir / "index.json"
        self.collections = {}

    def add_collection(self, path: str, name: str, mask: str = "**/*.md") -> None:
        """Add files to collection."""
        path = Path(path).resolve()
        if not path.exists():
            raise FileNotFoundError(f"Path does not exist: {path}")

        # Find matching files
        files = []
        for root, dirs, filenames in os.walk(path):
            for filename in filenames:
                if re.match(mask.replace("**/", ".*"), filename, re.IGNORECASE):
                    files.append(Path(root) / filename)

        self.collections[name] = {
            "path": str(path),
            "mask": mask,
            "files": [str(f) for f in files]
        }
        self._save_index()
        print(f"✓ Added collection '{name}' with {len(files)} files")

    def search(self, query: str, collection: str = None, top_k: int = 10) -> List[Dict]:
        """Search query across files."""
        results = []

        target_collections = [collection] if collection else list(self.collections.keys())

        for coll_name in target_collections:
            if coll_name not in self.collections:
                continue

            coll = self.collections[coll_name]
            for file_path in coll["files"]:
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        
                    # Simple keyword matching with position
                    query_terms = query.lower().split()
                    score = 0
                    
                    for term in query_terms:
                        if term in content.lower():
                            score += 1
                    
                    if score > 0:
                        results.append({
                            "file": file_path,
                            "collection": coll_name,
                            "score": score,
                            "snippet": self._get_snippet(content, query, 100)
                        })
                except Exception as e:
                    print(f"Warning: Could not read {file_path}: {e}")

        # Sort by score (descending)
        results.sort(key=lambda x: x["score"], reverse=True)
        return results[:top_k]

    def _get_snippet(self, content: str, query: str, context: int = 100) -> str:
        """Extract context around query match."""
        pos = content.lower().find(query.lower())
        if pos == -1:
            return content[:context] + "..."
        
        start = max(0, pos - context)
        end = min(len(content), pos + len(query) + context)
        snippet = content[start:end]
        
        if start > 0:
            snippet = "..." + snippet
        if end < len(content):
            snippet = snippet + "..."
        
        return snippet.strip()

    def _save_index(self) -> None:
        """Save collections index."""
        with open(self.index_file, 'w') as f:
            json.dump(self.collections, f, indent=2)

    def load_index(self) -> None:
        """Load existing index."""
        if self.index_file.exists():
            with open(self.index_file, 'r') as f:
                self.collections = json.load(f)

    def status(self) -> str:
        """Show index status."""
        self.load_index()
        status_lines = ["Index Status:", "=" * 40]
        
        for name, coll in self.collections.items():
            status_lines.append(f"\nCollection: {name}")
            status_lines.append(f"  Path: {coll['path']}")
            status_lines.append(f"  Files: {len(coll['files'])}")
            status_lines.append(f"  Mask: {coll['mask']}")
        
        return "\n".join(status_lines)


def main():
    """CLI interface."""
    import sys
    
    indexer = SimpleMDIndexer()
    
    if len(sys.argv) < 2:
        print("Usage: simple_md_indexer.py <command> [args]")
        print("Commands:")
        print("  add <path> <name> [--mask '**/*.md']")
        print("  search <query> [--collection <name>] [--top-k <N>]")
        print("  status")
        sys.exit(1)
    
    command = sys.argv[1]
    
    if command == "add":
        path = sys.argv[2]
        name = sys.argv[3]
        mask = sys.argv[4] if len(sys.argv) > 4 else "**/*.md"
        indexer.add_collection(path, name, mask)
    
    elif command == "search":
        query = sys.argv[2]
        collection = None
        top_k = 10
        
        if "--collection" in sys.argv:
            idx = sys.argv.index("--collection")
            collection = sys.argv[idx + 1]
        
        if "--top-k" in sys.argv:
            idx = sys.argv.index("--top-k")
            top_k = int(sys.argv[idx + 1])
        
        results = indexer.search(query, collection, top_k)
        print(f"Found {len(results)} results:")
        print("-" * 40)
        for i, r in enumerate(results, 1):
            print(f"{i}. [{r['collection']}] {Path(r['file']).name}")
            print(f"   Score: {r['score']}")
            print(f"   {r['snippet'][:200]}...")
            print()
    
    elif command == "status":
        print(indexer.status())
    
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
