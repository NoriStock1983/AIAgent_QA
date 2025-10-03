from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class Embedding:
    value: List[float]

    def __post_init__(self):
        if not isinstance(self.value, list) or not all(isinstance(i, float) for i in self.value):
            raise ValueError("Embedding must be a list of floats.")
        if len(self.value) != 768:
            raise ValueError("Embedding vector must have 768 dimensions.")
