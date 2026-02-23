"""Filename search module."""
from pathlib import Path
from typing import List


class FilenameSearch:
    def search(self, path: str, pattern: str) -> List[str]:
        return [str(p) for p in Path(path).rglob(pattern)]
