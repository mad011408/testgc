"""MIME detector module."""
from pathlib import Path


class MimeDetector:
    def detect(self, path: str) -> str:
        ext = Path(path).suffix.lower()
        m = {".txt": "text/plain", ".json": "application/json", ".py": "text/x-python"}
        return m.get(ext, "application/octet-stream")
