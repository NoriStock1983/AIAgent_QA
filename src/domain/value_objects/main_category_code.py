from dataclasses import dataclass
import re
from logging import getLogger

logger = getLogger(__name__)


@dataclass(frozen=True)
class MainCategoryCode:
    main_category_code: str

    def __post_init__(self):
        if not isinstance(self.main_category_code, str) or not self.main_category_code:
            logger.error("メインカテリーコードは必須入力項目です。")
            raise ValueError("メインカテリーコードは必須入力項目です。")

        if len(self.main_category_code) != 4:
            logger.error("メインカテリーコードは4桁で入力してください。")
            raise ValueError("メインカテリーコードは4桁で入力してください。")

        if re.search(r'[!@#$%^&*()_+\-=\[\]{};\':"\\|,.<>/?]', self.main_category_code):
            logger.error("メインカテリーコードに禁則文字が含まれています。")
            raise ValueError("メインカテリーコードに禁則文字が含まれています。")
