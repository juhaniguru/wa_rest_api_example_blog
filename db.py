from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

engine = create_engine("sqlite:///blog.sqlite?check_same_thread=False")
session = sessionmaker(bind=engine, autocommit=False, autoflush=False)


def init_db():
    conn = None
    try:
        conn = session()
        yield conn
    finally:
        if conn is not None:
            conn.close()
