from dataclasses import dataclass
from typing import List
from logging import getLogger

logger = getLogger(__name__)


@dataclass(frozen=True)
class Embedding:
    value: List[float]

    def __post_init__(self):
        if not isinstance(self.value, list) or not all(isinstance(i, float) for i in self.value):
            logger.error("Embeddingはリスト型で入力してください。")
            raise ValueError("Embeddingはリスト型で入力してください。")

        if len(self.value) != 768:
            logger.error("Embeddingは768次元で入力してください。")
            raise ValueError("Embeddingは768次元で入力してください。")
