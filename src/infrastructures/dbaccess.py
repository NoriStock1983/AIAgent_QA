
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine


class DBAccess(): 

    def __init__(self):
        load_dotenv()

        username = os.getenv("POSTGRES_USER")
        password = os.getenv("POSTGRES_PASSWORD")
        host = os.getenv("POSTGRES_HOST")
        port = os.getenv("POSTGRES_PORT")
        dbname = os.getenv("POSTGRES_DB")

        
        self.engine=create_engine(f"postgresql://{username}:{password}@{host}:{port}/{dbname}")

    def get_engine(self):
        return self.engine

    def close_engine(self):
        self.engine.dispose()