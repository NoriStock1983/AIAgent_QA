from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings  # 変更
from sqlalchemy import text
from domain.entities.insertragdata import InsertRagData
from domain.entities.searchCondition import SearchCondition
from domain.repositories.rag_repository_interface import RAGRepositoryInterface
from infrastructures.dbaccess import DBAccess
from logging import getLogger

logger = getLogger(__name__)


class RAGRepository(RAGRepositoryInterface):
    def __init__(self):
        # .envファイルを読み込む
        load_dotenv()
        # 埋め込みモデルをインスタンス変数として初期化
        self.embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")

    def search(self, search_condition: SearchCondition) -> str:
        logger.info("RAGRepository.search実行開始")
        dbaccess = DBAccess()
        engine = dbaccess.get_engine()

        query_vector = self.create_embedding(search_condition.question.question)  # メソッド名を規約に合わせて変更

        with engine.connect() as conn:
            result = ""
            result = conn.execute(text("SELECT id,question,contents,embedding <=> :query_vector FROM qa_order where embedding <=> :query_vector < 0.05 ORDER BY embedding <=> :query_vector DESC LIMIT 1"), {"query_vector": str(query_vector)})

            dbaccess.close_engine()
            logger.info("RAGRepository.search実行完了")

            # SQLで取得した内容の中から、Contentsの内容を抜き出し、それを戻り値として返す。
            return str(result.fetchall()[0][2])

    def insert(self, insert_rag_data: InsertRagData):
        logger.info("RAGRepository.insert実行開始")
        main_category_code = insert_rag_data.main_category_code
        main_category_name = insert_rag_data.main_category_name
        sub_category_code = insert_rag_data.sub_category_code
        sub_category_name = insert_rag_data.sub_category_name
        question = insert_rag_data.question
        contents = insert_rag_data.contents
        metadata = insert_rag_data.metadata.value
        embedding = self.create_embedding(str(question))  # メソッド名を規約に合わせて変更

        dbaccess = DBAccess()
        engine = dbaccess.get_engine()

        with engine.connect() as conn:
            conn.execute(text("INSERT INTO qa_order (main_category_code,main_category_name,sub_category_code,sub_category_name,question, contents, embedding,metadata) VALUES (:main_category_code,:main_category_name,:sub_category_code,:sub_category_name,:question, :contents, :embedding,:metadata)"), {"main_category_code": main_category_code, "main_category_name": main_category_name, "sub_category_code": sub_category_code, "sub_category_name": sub_category_name, "question": question, "contents": contents, "embedding": embedding, "metadata": metadata})
            conn.commit()
            logger.info("RAGRepository.insert実行完了")
        # ここにデータベースへの挿入処理を記述します

    def create_embedding(self, data: str):  # メソッド名を規約に合わせて変更
        logger.info("RAGRepository.create_embedding実行開始")
        # embed_queryメソッドを使って単一テキストの埋め込みを生成
        embedding = self.embeddings.embed_query(data)
        logger.info("RAGRepository.create_embedding実行完了")
        return embedding
