import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from logging import getLogger

logger = getLogger(__name__)


class DBAccess():
    def __init__(self):
        logger.info("DBAccess.init実行開始")
        load_dotenv()

        username = os.getenv("POSTGRES_USER")
        password = os.getenv("POSTGRES_PASSWORD")
        host = os.getenv("POSTGRES_HOST")
        port = os.getenv("POSTGRES_PORT")
        dbname = os.getenv("POSTGRES_DB")

        self.engine = create_engine(f"postgresql://{username}:{password}@{host}:{port}/{dbname}")
        logger.info("DBAccess.init実行完了")

    def get_engine(self):
        logger.info("DBAccess.get_engine実行完了")
        return self.engine

    def close_engine(self):
        logger.info("DBAccess.close_engine実行開始")
        self.engine.dispose()
        logger.info("DBAccess.close_engine実行完了")
