# Tree-sitter SPARQL

Python bindings for the tree-sitter SPARQL grammar.

This is based on the original repo here: https://github.com/GordianDziwis/tree-sitter-sparql - but updated to work with more recent versions of tree-sitter.

## Installation

Install from source:

```bash
git clone https://github.com/yourusername/tree_sitter_sparql
cd tree_sitter_sparql
pip install .
```

## Usage (tree-sitter 0.21.0+)

If you're using tree-sitter version 0.21.0 or later:

```python
import tree_sitter_sparql
from tree_sitter import Language, Parser

# Initialize the language
SPARQL_LANGUAGE = Language(tree_sitter_sparql.language())

# Create parser
parser = Parser(SPARQL_LANGUAGE)

# Parse SPARQL query
query = b"""
SELECT ?subject ?predicate ?object
WHERE {
  ?subject ?predicate ?object .
}
LIMIT 10
"""

tree = parser.parse(query)

# Walk the syntax tree
cursor = tree.walk()

def walk_tree(cursor, depth=0):
    node = cursor.node
    print("  " * depth + f"{node.type}: {node.text.decode('utf8')[:50]}")

    if cursor.goto_first_child():
        walk_tree(cursor, depth + 1)
        cursor.goto_parent()

    if cursor.goto_next_sibling():
        walk_tree(cursor, depth)

walk_tree(cursor)
```

## Requirements

- Python 3.8+
- tree-sitter

## Development

To build from source:

```bash
# Install in development mode
pip install -e .

# Run tests (if available)
pytest
```

## License

MIT
