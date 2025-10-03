from dataclasses import dataclass
import re

@dataclass(frozen=True)
class Contents:
    contents: str

    def __post_init__(self):
        if not isinstance(self.contents, str) or not self.contents:
            raise ValueError("Contentsは必須入力となります。")

        # 禁則文字が入力されている場合はエラーを返す。
        if re.search(r'[!@#$%^&*()_+\-=\[\]{};\':"\\|,.<>/?]', self.contents):
            raise ValueError("Contentsに禁則文字が含まれています。")

    def get_contents(self)->str:
        return self.contents
