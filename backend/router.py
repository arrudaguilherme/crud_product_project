from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, get_db
from schemas import ProductCreate, ProductResponse, ProductUpdate
from typing import List
from crud import get_products, get_product_by_id, create_product, update_product, delete_product_by_id

router = APIRouter()

@router.get("/")
def root():
    return ({"Hello" : "World"})

# route get items
@router.get("/products/",response_model=List[ProductResponse]) ## path and response
def get_all_products(db:Session = Depends(get_db)):
    products = get_products(db=db)
    return products

# route get item by id
@router.get("/products/{product_id}", response_model=ProductResponse)
def get_product(product_id: int, db:Session = Depends(get_db)):
    db_product = get_product_by_id(product_id, db=db)
    if db_product is None:
        raise HTTPException(status_code=404, detail= "Product not found")
    return db_product

# rout add item
@router.post("/products/", response_model = ProductResponse)
def insert_product(product:ProductCreate,db: Session = Depends(get_db)):
    return create_product(product=product,db=db)

# route to delete an item
@router.delete("/products/{product_id}",response_model=ProductResponse)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product_db = delete_product_by_id(product_id=product_id,db=db)
    if product_db is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product_db

# route to update an item
@router.put("/products/{product_id}",response_model=ProductResponse)
def update_item(product:ProductUpdate, product_id:int, db: Session = Depends(get_db)):
    product_db = update_product(product=product, product_id=product_id, db=db)
    if product_db is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product_db