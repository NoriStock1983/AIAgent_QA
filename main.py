import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from dotenv import load_dotenv
from adapters.controllers.llmAnswerController import LLMAnswerController
from adapters.controllers.SearchRagData.ragSearchController import RagSearchController
from usecases.llmanswer.llmanswer_usecase import LLMAnswerUsecase
from usecases.rag.ask_question_uescase import AskQuestionUsecase
from infrastructures.repositories.rag_repository import RAGRepository
from langchain_google_genai import ChatGoogleGenerativeAI
from usecases.cashe.cache_usecase import CasheUsecase

load_dotenv()


def main():

    question = "WiFiに接続できません。"
    repository = RAGRepository()
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)
    ask_question_usecase = AskQuestionUsecase(repository=repository, llm=llm)
    llmanswer_usecase = LLMAnswerUsecase(llm=llm)
    rag_controller = RagSearchController(usecase=ask_question_usecase)
    llmanswer_controller = LLMAnswerController(usecase=llmanswer_usecase)

    # Redis接続
    cache_usecase = CasheUsecase()

    # Redisからデータ取得
    answer = cache_usecase.select(question)

    # もしredisからデータが取得できない場合、RAG内のデータを検索する。
    if not answer:
        result = rag_controller.search(question)
        print("RAG内のデータを検索しました。")
        print(result)
        # LLMに回答を渡し、回答を取得
        llm_answer = llmanswer_controller.answer(result)
        print(llm_answer)

        # Redisにデータを保存
        cache_usecase.insert(question, llm_answer)

    else:
        print("Redisからデータを取得しました。")
        print(answer)

if __name__ == "__main__":
    main()
