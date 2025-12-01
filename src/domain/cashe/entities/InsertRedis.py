from datetime import datetime

class InsertRedis:
    def __init__(self, question: str, contents: str):
        self.question = question
        self.contents = contents
        self.created_at = datetime.now()
        self.updated_at = datetime.now()        