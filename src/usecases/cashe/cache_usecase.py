from infrastructures.redisaccess import RedisAccess


class CasheUsecase:
    def __init__(self):
        self.redis_access = RedisAccess()

    # insert
    def insert(self, question: str, answer: str):
        redis_client = self.redis_access.get_client()
        redis_client.set(question, answer)
        pass

    # select
    def select(self, question: str):
        redis_client = self.redis_access.get_client()
        answer = redis_client.get(question)
        return answer

    # delete
    def delete(self, question: str):
        redis_client = self.redis_access.get_client()
        redis_client.delete(question)
        pass

    # update
    def update(self, question: str, answer: str):
        redis_client = self.redis_access.get_client()
        redis_client.set(question, answer)
        pass
