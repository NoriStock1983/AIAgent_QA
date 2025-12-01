from dataclasses import dataclass
from logging import getLogger

logger = getLogger(__name__)


@dataclass(frozen=True)
class Id:
    value: int

    def __post_init__(self):
        if not isinstance(self.value, int) or self.value <= 0:
            logger.error("Idは正の整数で入力してください。")
            raise ValueError("Idは正の整数で入力してください。")
