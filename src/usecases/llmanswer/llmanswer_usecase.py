from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import HumanMessage, SystemMessage


class LLMAnswerUsecase:
    def __init__(self, llm: BaseChatModel):
        self.llm = llm

    def execute(self, rag_answer: str) -> str:
        message = [
            SystemMessage(content="あなたは、企業の情報システム部のサービスデスク担当者です。"),
            SystemMessage(content="以下のユーザからの問い合わせに対して、解決策を回答してください。"),
            HumanMessage(content=rag_answer),
            SystemMessage(content="回答は、ユーザに対して、わかりやすく、簡潔に、回答してください。"),
        ]
        response = self.llm.invoke(message)

        return response.content