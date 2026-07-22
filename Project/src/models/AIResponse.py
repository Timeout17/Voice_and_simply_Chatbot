from dataclasses import dataclass
from typing import Any

@dataclass
class AIResponseClass():
    client: Any
    model: str
