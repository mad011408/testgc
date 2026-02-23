"""Content search module."""
from pathlib import Path
from typing import List


class ContentSearch:
    def search(self, path: str, text: str) -> List[str]:
        results = []
        try:
            for p in Path(path).rglob("*"):
                if p.is_file():
                    if text in p.read_text(errors="ignore"):
                        results.append(str(p))
        except Exception:
            pass
        return results
