"""
Least to Most - Least-to-most prompting for decomposition.
"""

from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class SubProblem:
    index: int
    problem: str
    solution: str
    depends_on: List[int]


class LeastToMost:
    """Least-to-most problem decomposition and solving."""

    def __init__(self, max_subproblems: int = 20):
        self.max_subproblems = max_subproblems

    def decompose(self, problem: str) -> List[SubProblem]:
        """Decompose problem from least to most complex (stub)."""
        return []
