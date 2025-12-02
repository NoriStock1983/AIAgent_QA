import sys
from pathlib import Path

# srcディレクトリをPythonパスに追加
sys.path.insert(0, str(Path(__file__).parent / "src"))

from dotenv import load_dotenv
from adapters.controllers.llmAnswerController import LLMAnswerController
from adapters.controllers.ragSearchController import RagSearchController
from usecases.llmanswer.llmanswer_usecase import LLMAnswerUsecase
from usecases.rag.ask_question_uescase import AskQuestionUsecase
from infrastructures.repositories.rag_repository import RAGRepository
from langchain_google_genai import ChatGoogleGenerativeAI
from infrastructures.redisaccess import RedisAccess

load_dotenv()


def main():

    question = "WiFiに接続できません。"
    repository = RAGRepository()
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)
    usecase = AskQuestionUsecase(repository=repository, llm=llm)
    llmanswer_usecase = LLMAnswerUsecase(llm=llm)
    rag_controller = RagSearchController(usecase=usecase)
    llmanswer_controller = LLMAnswerController(usecase=llmanswer_usecase)
    result = rag_controller.search(question)
    print(result)
    llm_answer = llmanswer_controller.answer(result)
    print(llm_answer)
    # Redis接続
    redis_access = RedisAccess()
    redis_client = redis_access.get_client()
    
    # Redisへデータ挿入
    redis_client.set(question, llm_answer)

    # Redisからデータ取得
    print("Redisからデータ取得")
    print(redis_client.get(question))

    # Redis接続解除
    redis_access.close()


if __name__ == "__main__":
    main()
