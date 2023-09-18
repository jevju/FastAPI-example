from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declared_attr

from app.db.base_class import Base

class Item(Base):
    __name__: str
    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
