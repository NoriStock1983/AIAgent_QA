from dataclasses import dataclass, field
from typing import Dict, Any
import json


@dataclass(frozen=True)
class MetaData:
    value: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self):
        if not isinstance(self.value, dict):
            raise ValueError("MetaData must be a dictionary.")
        try:
            json.dumps(self.value)
        except TypeError as e:
            raise ValueError("MetaData must be JSON serializable.") from e
