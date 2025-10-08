from dataclasses import dataclass
from logging import getLogger

logger = getLogger(__name__)


@dataclass(frozen=True)
class SubCategoryCode:
    sub_category_code: str

    def __post_init__(self):
        if not isinstance(self.sub_category_code, str) or not self.sub_category_code:
            logger.error("サブカテリーコードは必須入力項目です。")
            raise ValueError("サブカテリーコードは必須入力項目です。")

        if not isinstance(self.sub_category_code, str) or len(self.sub_category_code) != 4:
            logger.error("サブカテリーコードは4桁で入力してください。")
            raise ValueError("サブカテリーコードは4桁で入力してください。")
