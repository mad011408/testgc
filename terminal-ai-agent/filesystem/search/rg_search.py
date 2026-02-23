"""RG search module."""
from pathlib import Path
from typing import List
import subprocess


class RgSearch:
    def search(self, path: str, pattern: str) -> List[str]:
        try:
            r = subprocess.run(["rg", "-l", pattern, path], capture_output=True, text=True)
            return r.stdout.strip().split("\n") if r.returncode in (0, 1) else []
        except Exception:
            return [str(p) for p in Path(path).rglob("*") if p.is_file()]
