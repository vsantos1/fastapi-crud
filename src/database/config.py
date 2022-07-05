from sqlalchemy import create_engine,MetaData
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_MYSQL_URL")


engine = create_engine(DATABASE_URL)
meta = MetaData()
connect = engine.connect()
