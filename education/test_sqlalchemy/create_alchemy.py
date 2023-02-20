import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

current_folder = os.path.abspath(__file__)
database_url = r'sqlite://///Users/kot/Education/PycharmProjects/kek/education/test_sql/data/database.db'
engine = create_engine(database_url, connect_args={'check_same_thread': False})


Session = sessionmaker(engine, autocommit=False, autoflush=False)


def get_session() -> Session:
    session = Session()
    try:
        yield session
    finally:
        session.close()