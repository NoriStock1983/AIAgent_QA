from domain.value_objects.main_category_code import MainCategoryCode
from usecases.rag.ask_question_uescase import AskQuestionUsecase


class RagSearchController:
    def __init__(self, usecase: AskQuestionUsecase):
        self.usecase = usecase
        self.main_category_code = MainCategoryCode(main_category_code="0002")

    def search(self, question: str) -> str:
        return self.usecase.execute(question, "0001", "0002")
