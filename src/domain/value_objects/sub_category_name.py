from dataclasses import dataclass


@dataclass(frozen=True)
class SubCategoryName:
    value: str

    def __post_init__(self):
        if not isinstance(self.value, str) or not self.value:
            raise ValueError("SubCategoryName cannot be empty.")
