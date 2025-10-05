from langchain_core.language_models.chat_models import BaseChatModel
from domain.entities.searchCondition import SearchCondition
from domain.repositories.rag_repository_interface import RAGRepositoryInterface
from domain.value_objects.main_category_code import MainCategoryCode
from domain.value_objects.question import Question
from domain.value_objects.sub_category_code import SubCategoryCode


class AskQuestionUsecase:
    def __init__(self, repository: RAGRepositoryInterface, llm: BaseChatModel):
        self.repository = repository
        self.llm = llm

    def execute(self, question: str, main_category_code: str, sub_category_code: str) -> str:

        condition = SearchCondition(
            question=Question(question=question),
            main_category_code=MainCategoryCode(main_category_code=main_category_code),
            sub_category_code=SubCategoryCode(sub_category_code=sub_category_code),
        )

        result = self.repository.search(condition)

        if not result:
            return "回答が見つかりませんでした。"

        return result
