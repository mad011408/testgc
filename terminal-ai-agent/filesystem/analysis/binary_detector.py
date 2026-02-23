"""Binary detector module."""
from pathlib import Path


class BinaryDetector:
    def is_binary(self, path: str) -> bool:
        try:
            data = Path(path).read_bytes()[:8192]
            n = len(data)
            printable = sum(1 for b in data if 32 <= b < 127 or b in (9, 10, 13))
            return b"\x00" in data or (n > 0 and printable / n < 0.9)
        except Exception:
            return False
