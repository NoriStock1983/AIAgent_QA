from abc import ABC, abstractmethod
from src.domain.cashe.entities.searchRedis import SearchRedis

class RedisRepositoryInterface(ABC):
    @abstractmethod
    def insert(self, search_redis: SearchRedis) -> None:
        pass

    @abstractmethod
    def search(self, query: str) -> SearchRedis | None:
        pass
