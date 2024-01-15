from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from helpers import get_env_vars

env_vars = get_env_vars.get_settings()

db_uri = f"mysql+pymysql://{env_vars.db_user}:{env_vars.db_password}@{env_vars.db_host}:{env_vars.db_port}/{env_vars.db_name}"

engine = create_engine(url=db_uri, pool_pre_ping=True)

Base = declarative_base()

Session = sessionmaker(bind=engine)


def get_db():
    try:
        db = Session()
        yield db
    finally:
        db.close()
