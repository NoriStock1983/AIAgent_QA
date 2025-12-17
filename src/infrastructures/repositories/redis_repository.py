from logging import getLogger
from domain.cache.entities.searchRedis import SearchRedis
from domain.cache.repositories.redis_repository_interface import RedisRepositoryInterface
from infrastructures.redisaccess import RedisAccess
from datetime import datetime

logger = getLogger(__name__)


class RedisRepository(RedisRepositoryInterface):
    def __init__(self):
        self.redis_access = RedisAccess()

    def insert(self, search_redis: SearchRedis) -> None:
        logger.info(f"RedisRepository.insert実行開始: query={search_redis.query}")
        client = self.redis_access.get_client()
        key = f"search:{search_redis.query}"
        client.set(key, search_redis.answer)
        logger.info("RedisRepository.insert実行完了")

    def search(self, query: str) -> SearchRedis | None:
        logger.info(f"RedisRepository.search実行開始: query={query}")
        client = self.redis_access.get_client()
        key = f"search:{query}"
        answer = client.get(key)

        if answer:
            logger.info("RedisRepository.search実行完了: データあり")
            return SearchRedis(query=query, answer=answer)
        else:
            logger.info("RedisRepository.search実行完了: データなし")
            return None

    def delete(self, updated_at: datetime) -> None:
        logger.info(f"RedisRepository.delete実行開始: updated_at={updated_at}")
        client = self.redis_access.get_client()
        key = f"search:{updated_at}"
        client.delete(key)
        logger.info("RedisRepository.delete実行完了")
