from dataclasses import dataclass
from domain.value_objects.contents import Contents
from domain.value_objects.embedding import Embedding
from domain.value_objects.main_category_code import MainCategoryCode
from domain.value_objects.main_category_name import MainCategoryName
from domain.value_objects.metadata import MetaData
from domain.value_objects.question import Question
from domain.value_objects.sub_category_code import SubCategoryCode
from domain.value_objects.sub_category_name import SubCategoryName


@dataclass(frozen=True)
class InsertRagData:
    question: Question
    main_category_code: MainCategoryCode
    main_category_name: MainCategoryName
    sub_category_code: SubCategoryCode
    sub_category_name: SubCategoryName
    contents: Contents
    metadata: MetaData
    embedding: Embedding
    created_at: str
    updated_at: str
