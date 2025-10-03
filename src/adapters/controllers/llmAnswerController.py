from langchain_core.language_models.chat_models import BaseChatModel
from usecases.llmanswer.llmanswer_usecase import LLMAnswerUsecase


class LLMAnswerController:
    def __init__(self, usecase: LLMAnswerUsecase):
        self.usecase = usecase

    def answer(self, question: str) -> str:
        return self.usecase.execute(question)
        