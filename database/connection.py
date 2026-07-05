from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE = "sqlite:///finance.db"

engine = create_engine(url=DATABASE, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(bind=engine, autocommit=False)
