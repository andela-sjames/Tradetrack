# Our SQLAlchemy models

from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Enum
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime
import enum

Base = declarative_base()

class TransactionType(enum.Enum):
    PURCHASE = "purchase"
    SALE = "sale"


class Product(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    sku = Column(String, unique=True, nullable=False)
    category = Column(String)
    purchase_price = Column(Float)
    
    transactions = relationship("Transaction", back_populates="product")


class Transaction(Base):
    __tablename__ = 'transactions'
    
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    type = Column(Enum(TransactionType), nullable=False)
    date = Column(DateTime, default=datetime.utcnow)
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Float, nullable=False)
    
    product = relationship("Product", back_populates="transactions")
