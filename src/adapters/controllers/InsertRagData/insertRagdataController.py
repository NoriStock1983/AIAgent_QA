from domain.entities.insertragdata import InsertRagData
from usecases.rag.insert_rag_usecase import InsertRagUsecase


class InsertRagdataController:
    def __init__(self, usecase: InsertRagUsecase):
        self.usecase = usecase

    def insert(self, insert_rag_data: InsertRagData):
        self.usecase.insert(insert_rag_data)
