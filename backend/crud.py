from sqlalchemy.orm import Session
from schemas import ProductUpdate, ProductResponse, ProductBase, ProductCreate
from models import ProductModel

# get all
def get_products(db: Session):
    return db.query(ProductModel).all() ## selects all items on this table

# get by id
def get_product_by_id(product_id: int, db: Session):
    return db.query(ProductModel).filter(ProductModel.id == product_id).first()
# post / create

def create_product(product:ProductCreate, db: Session):
    db_product = ProductModel(**product.model_dump()) # transform my schema into ORM
    # ADD into the table
    db.add(db_product)
    # commit into table
    db.commit()
    # refresh DB
    db.refresh(db_product)
    # return item to user 
    return db_product

# update by id

def update_product(product: ProductUpdate, product_id: int, db: Session):
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    if db_product is None:
        return None
    
    if product.name is not None:
        db_product.name = product.name

    if product.description is not None:
        db_product.description = product.description

    if product.price is not None:
        db_product.price = product.price

    if product.category is not None:
        db_product.category = product.category
    
    if product.email_supplier is not None:
        db_product.email_supplier = product.email_supplier

    db.commit()
    db.refresh()
    return db_product


# delete by id
def delete_product_by_id(product_id: int, db: Session):
    # filter de product by id
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    # delete the product using the session
    db.delete(db_product)
    # db commit
    db.commit()
    # return to user
    return db_product
