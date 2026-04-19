from sqlalchemy import Column, Integer
from database.database import Base

# class Stock(Base):
class Stock(Base):
    __tablename__ = "stock_cache"

    product_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    stock = Column(Integer, nullable=False)