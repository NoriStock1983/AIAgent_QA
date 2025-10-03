from dataclasses import dataclass
import re

@dataclass(frozen=True)
class Question:
    question: str

    def __post_init__(self):
        if not isinstance(self.question, str) or not self.question:
            raise ValueError("質問事項は必須入力となります。")

        if len(self.question) > 255:
            raise ValueError("質問事項は255文字以内で入力してください。")

        # 禁則文字が入力された場合、エラーとする。
        if re.search(r'[!@#$%^&*()_+\-=\[\]{};\':"\\|,.<>/?]', self.question):
            raise ValueError("質問事項に禁則文字が含まれています。")

    def get_question(self)->str:
        return self.question
