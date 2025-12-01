import os
import redis
from dotenv import load_dotenv
from logging import getLogger

logger = getLogger(__name__)

class RedisAccess:
    def __init__(self):
        logger.info("RedisAccess.init実行開始")
        load_dotenv()

        self.host = os.getenv("REDIS_HOST")
        self.port = int(os.getenv("REDIS_PORT"))
        self.password = os.getenv("REDIS_PASSWORD")
        
        # Docker Compose service name might be used as host if running inside container,
        # but for local development it might be localhost.
        # The docker-compose.yml maps 6379:6379, so localhost:6379 should work from host.

        try:
            self.client = redis.Redis(
                host=self.host,
                port=self.port,
                password=self.password,
                decode_responses=True # Returns strings instead of bytes
            )
            # Connection check
            self.client.ping()
            logger.info("RedisAccess.init実行完了: 接続成功")
        except redis.ConnectionError as e:
            logger.error(f"RedisAccess.init接続失敗: {e}")
            raise e

    def get_client(self):
        logger.info("RedisAccess.get_client実行")
        return self.client

    def close(self):
        logger.info("RedisAccess.close実行")
        self.client.close()
