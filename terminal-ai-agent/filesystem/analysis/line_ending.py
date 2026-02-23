"""Line ending module."""
from pathlib import Path


class LineEnding:
    def detect(self, path: str) -> str:
        try:
            b = Path(path).read_bytes()
            if b"\r\n" in b:
                return "crlf"
            if b"\r" in b:
                return "cr"
        except Exception:
            pass
        return "lf"
