# reduced database table without the id, and created at
## Data validation
from pydantic import PositiveFloat, PositiveInt, BaseModel, EmailStr, field_validator, Field
from enum import Enum
from typing import Optional
from datetime import datetime

class ProductBase(BaseModel):
    name: str
    description: str
    price: PositiveFloat
    category: str
    email_supplier: EmailStr

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int
    created_at: datetime

    class config:
        from_attributes = True  # allows the dump when creating the product in the post function

class ProductUpdate(BaseModel):
    ## it's possible to change only one field
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[PositiveFloat] = None
    category: Optional[str] = None
    email_supplier: Optional[EmailStr] = None