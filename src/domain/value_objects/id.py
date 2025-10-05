from dataclasses import dataclass


@dataclass(frozen=True)
class Id:
    value: int

    def __post_init__(self):
        if not isinstance(self.value, int) or self.value <= 0:
            raise ValueError("Id must be a positive integer.")
