from dataclasses import dataclass
import re
from logging import getLogger

logger = getLogger(__name__)


@dataclass(frozen=True)
class Contents:
    contents: str

    def __post_init__(self):
        logger.info("Contents.__post_init__実行開始")
        if not isinstance(self.contents, str) or not self.contents:
            logger.error("Contentsは必須入力となります。")
            raise ValueError("Contentsは必須入力となります。")

        # 禁則文字が入力されている場合はエラーを返す。
        if re.search(r'[!@#$%^&*()_+\-=\[\]{};\':"\\|,.<>/?]', self.contents):
            logger.error("Contentsに禁則文字が含まれています。")
            raise ValueError("Contentsに禁則文字が含まれています。")

        logger.info("Contents.__post_init__実行完了")
