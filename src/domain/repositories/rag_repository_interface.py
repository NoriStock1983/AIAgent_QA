
# repositoryのいたーフェース
from abc import ABCMeta, abstractmethod
from domain.entities.insertragdata import InsertRagData
from domain.entities.searchCondition import SearchCondition


class RAGRepositoryInterface(metaclass=ABCMeta):

    @abstractmethod
    def search(self, condition: SearchCondition) -> str:
        """
        指定された質問に基づいてRAGデータを検索します。
        """
        pass

    @abstractmethod
    def insert(self, insert_rag_data: InsertRagData) -> None:
        """
        指定された質問と内容をRAGデータとして挿入します。
        """
        pass
