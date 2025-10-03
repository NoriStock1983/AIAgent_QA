from dataclasses import dataclass
from math import degrees

@dataclass(frozen=True)
class SubCategoryCode:
    sub_category_code: str

    def __post_init__(self):
        if not isinstance(self.sub_category_code, str) or not self.sub_category_code:
            raise ValueError("サブカテリーコードは必須入力項目です。")

        if not isinstance(self.sub_category_code, str) or len(self.sub_category_code) != 4:
            raise ValueError("サブカテリーコードは4桁で入力してください。")

    def get_code(self):
        return self.sub_category_code