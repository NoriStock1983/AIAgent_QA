from domain.rag.entities.insertragdata import InsertRagData
from domain.rag.repositories.rag_repository_interface import RAGRepositoryInterface


class InsertRagUsecase:
    def __init__(self, repository: RAGRepositoryInterface):
        self.repository = repository

    def insert(self, insert_rag_data: InsertRagData):
        self.repository.insert(insert_rag_data)
