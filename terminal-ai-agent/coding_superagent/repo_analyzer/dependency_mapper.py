"""
Dependency Mapper - Maps package and module dependencies.
"""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Set


@dataclass
class Dependency:
    name: str
    version: Optional[str] = None
    source: str = "pypi"
    direct: bool = True


@dataclass
class DependencyTree:
    root: str
    direct: List[Dependency] = field(default_factory=list)
    transitive: Dict[str, List[Dependency]] = field(default_factory=dict)
    conflicts: List[str] = field(default_factory=list)


class DependencyMapper:
    """Maps and analyzes dependencies."""

    def __init__(self):
        self._lock_files = ["Pipfile.lock", "poetry.lock", "requirements.txt"]

    def map_from_project(self, root: str = ".") -> DependencyTree:
        """Map dependencies from project root (stub - use pipdeptree/poetry)."""
        tree = DependencyTree(root=root)
        req_path = Path(root) / "requirements.txt"
        if req_path.exists():
            for line in req_path.read_text().splitlines():
                line = line.strip().split("#")[0]
                if line and "==" in line:
                    name, ver = line.split("==", 1)
                    tree.direct.append(Dependency(name=name.strip(), version=ver.strip()))
        return tree

    def find_circular(self, tree: DependencyTree) -> List[List[str]]:
        """Find circular dependencies (stub)."""
        return []
