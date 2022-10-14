from dataclasses import dataclass
from pathlib import Path

@dataclass
class Element:
    full_path: Path
    name: str