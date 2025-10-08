from dataclasses import dataclass
from logging import getLogger

logger = getLogger(__name__)


@dataclass(frozen=True)
class MainCategoryName:
    main_category_name: str

    def __post_init__(self):
        if not isinstance(self.main_category_name, str) or not self.main_category_name:
            logger.error("メインカテリーコードは必須入力項目です。")
            raise ValueError("メインカテリーコードは必須入力項目です。")

        if len(self.main_category_name) > 255:
            logger.error("メインカテリーコードは255文字以内で入力してください。")
            raise ValueError("メインカテリーコードは255文字以内で入力してください。")
