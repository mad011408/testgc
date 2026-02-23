"""File type module."""
from pathlib import Path


class FileType:
    def detect(self, path: str) -> str:
        return Path(path).suffix or "unknown"
