from dataclasses import dataclass
import re


@dataclass(frozen=True)
class MainCategoryCode:
    main_category_code: str

    def __post_init__(self):
        if not isinstance(self.main_category_code, str) or not self.main_category_code:
            raise ValueError("メインカテリーコードは必須入力項目です。")

        if len(self.main_category_code) != 4:
            raise ValueError("メインカテリーコードは4桁で入力してください。")

        if re.search(r'[!@#$%^&*()_+\-=\[\]{};\':"\\|,.<>/?]', self.main_category_code):
            raise ValueError("メインカテリーコードに禁則文字が含まれています。")

    def get_code(self):
        return self.main_category_code
