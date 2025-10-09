from dataclasses import dataclass
from typing import Optional
from domain.value_objects.main_category_code import MainCategoryCode
from domain.value_objects.question import Question
from domain.value_objects.sub_category_code import SubCategoryCode


@dataclass(frozen=True)
class SearchCondition:

    question: Question
    main_category_code: Optional[MainCategoryCode]
    sub_category_code: Optional[SubCategoryCode]
