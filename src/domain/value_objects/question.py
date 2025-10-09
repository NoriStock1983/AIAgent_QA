from dataclasses import dataclass
import re
from logging import getLogger

logger = getLogger(__name__)


@dataclass(frozen=True)
class Question:
    question: str

    def __post_init__(self):
        if not isinstance(self.question, str) or not self.question:
            logger.error("質問事項は必須入力となります。")
            raise ValueError("質問事項は必須入力となります。")

        if len(self.question) > 255:
            logger.error("質問事項は255文字以内で入力してください。")
            raise ValueError("質問事項は255文字以内で入力してください。")

        # 禁則文字が入力された場合、エラーとする。
        if re.search(r'[!@#$%^&*()_+\-=\[\]{};\':"\\|,.<>/?]', self.question):
            logger.error("質問事項に禁則文字が含まれています。")
            raise ValueError("質問事項に禁則文字が含まれています。")
