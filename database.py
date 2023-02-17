from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from models import Items, declarative_base


engine = create_engine("sqlite:///item.db", echo=True)
Base = declarative_base()
session_local = sessionmaker(bind=engine, expire_on_commit=False)
