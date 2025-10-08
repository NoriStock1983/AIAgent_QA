from dataclasses import dataclass
from logging import getLogger

logger = getLogger(__name__)


@dataclass(frozen=True)
class SubCategoryName:
    value: str

    def __post_init__(self):
        if not isinstance(self.value, str) or not self.value:
            logger.error("サブカテリー名は必須入力項目です。")
            raise ValueError("サブカテゴリー名は必須入力項目です。")

        if len(self.value) > 255:
            logger.error("サブカテリー名は255文字以内で入力してください。")
            raise ValueError("サブカテリー名は255文字以内で入力してください。")
