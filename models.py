from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Items(Base):
    __tablename__ = 'items'
    id = Column(UUID(as_uuid=True), primary_key=True)
    name = Column(String)