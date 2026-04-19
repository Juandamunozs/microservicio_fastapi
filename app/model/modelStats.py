from sqlalchemy import Column, Integer
from database.database import Base

# class Stats(Base):
class Stats(Base):
    __tablename__ = "stats"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    metric = Column(Integer, nullable=False)