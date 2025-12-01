from dataclasses import dataclass, field
from typing import Dict, Any
import json
from logging import getLogger

logger = getLogger(__name__)


@dataclass(frozen=True)
class MetaData:
    value: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self):
        if not isinstance(self.value, dict):
            logger.error("MetaDataは辞書型で入力してください。")
            raise ValueError("MetaDataは辞書型で入力してください。")

        try:
            json.dumps(self.value)
        except TypeError as e:
            logger.error("MetaDataはJSONシリアライズ可能です。")
            raise ValueError("MetaDataはJSONシリアライズ可能です。") from e
