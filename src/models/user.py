from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from os import getenv
import psycopg2

DATABASE_URL = getenv("DATABASE_MYSQL_URL")


engine = create_engine(DATABASE_URL)
meta = MetaData()

users = Table(
    "users", meta,
    Column("id",Integer,primary_key=True,autoincrement=True),
    Column("name",String(255),nullable=False),
    Column("email",String(255),nullable=False,unique=True),
    Column("password",String(255),nullable=False),
        
)

meta.create_all(engine)