from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from database import Base

class ProductModel(Base): ## Gets the base from the orm
    __tablename__ = "products" ## tablename on the database

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    description = Column(String(250))
    price = Column(Float)
    category = Column(String(30))
    email_supplier = Column(String(250))
    created_at = Column(DateTime(timezone=True),default=func.now)
