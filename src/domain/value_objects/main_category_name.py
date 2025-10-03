from dataclasses import dataclass

@dataclass(frozen=True)
class MainCategoryName:
    main_category_name: str

    def __post_init__(self):
        if not isinstance(self.main_category_name, str) or not self.main_category_name:
            raise ValueError("メインカテリーコードは必須入力項目です。")

        if len(self.main_category_name) > 255:
            raise ValueError("メインカテリーコードは255文字以内で入力してください。")


    def get_name(self):
        return self.main_category_name