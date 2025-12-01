from dataclasses import dataclass
from domain.rag.value_objects.contents import Contents
from domain.rag.value_objects.embedding import Embedding
from domain.rag.value_objects.main_category_code import MainCategoryCode
from domain.rag.value_objects.main_category_name import MainCategoryName
from domain.rag.value_objects.metadata import MetaData
from domain.rag.value_objects.question import Question
from domain.rag.value_objects.sub_category_code import SubCategoryCode
from domain.rag.value_objects.sub_category_name import SubCategoryName


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
