"""
Code Graph Builder - Builds dependency and call graphs for codebases.
"""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Set


@dataclass
class Node:
    id: str
    type: str  # module, class, function
    name: str
    file_path: str
    line: int
    metadata: Dict[str, Any] = field(default_factory=dict)


@dataclass
class Edge:
    source: str
    target: str
    edge_type: str  # imports, calls, inherits
    metadata: Dict[str, Any] = field(default_factory=dict)


class CodeGraph:
    """Represents code structure as a graph."""

    def __init__(self):
        self.nodes: Dict[str, Node] = {}
        self.edges: List[Edge] = []
        self._incoming: Dict[str, Set[str]] = {}
        self._outgoing: Dict[str, Set[str]] = {}

    def add_node(self, node: Node) -> None:
        self.nodes[node.id] = node

    def add_edge(self, edge: Edge) -> None:
        self.edges.append(edge)
        self._outgoing.setdefault(edge.source, set()).add(edge.target)
        self._incoming.setdefault(edge.target, set()).add(edge.source)

    def get_dependents(self, node_id: str) -> List[str]:
        return list(self._incoming.get(node_id, set()))

    def get_dependencies(self, node_id: str) -> List[str]:
        return list(self._outgoing.get(node_id, set()))


class CodeGraphBuilder:
    """Builds code graph from source files."""

    def __init__(self):
        self._extensions = {".py", ".js", ".ts", ".go"}

    def build_from_path(self, root: str) -> CodeGraph:
        """Build graph from repository root (stub - requires ast/tree-sitter)."""
        graph = CodeGraph()
        root_path = Path(root)
        for f in root_path.rglob("*"):
            if f.suffix in self._extensions:
                node_id = str(f.relative_to(root_path))
                graph.add_node(Node(id=node_id, type="module", name=f.stem, file_path=str(f), line=0))
        return graph
