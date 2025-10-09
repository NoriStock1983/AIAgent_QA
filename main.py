from dotenv import load_dotenv
from adapters.controllers.llmAnswerController import LLMAnswerController
from adapters.controllers.ragSearchController import RagSearchController
from usecases.llmanswer.llmanswer_usecase import LLMAnswerUsecase
from usecases.rag.ask_question_uescase import AskQuestionUsecase
from infrastructures.repositories.rag_repository import RAGRepository
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()


def main():
    repository = RAGRepository()
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)
    usecase = AskQuestionUsecase(repository=repository, llm=llm)
    llmanswer_usecase = LLMAnswerUsecase(llm=llm)
    rag_controller = RagSearchController(usecase=usecase)
    llmanswer_controller = LLMAnswerController(usecase=llmanswer_usecase)
    result = rag_controller.search("WiFiに接続できません。")
    print(result)
    llm_answer = llmanswer_controller.answer(result)
    print(llm_answer)


if __name__ == "__main__":
    main()
