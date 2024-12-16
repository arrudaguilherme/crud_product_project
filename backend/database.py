from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine

POSTGRES_URL = 'postgresql://user:password@postgres/mydatabase'
engine = create_engine(url=POSTGRES_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=engine) ## Create database session
## autoflush uodates the db automatically, Set as False, User's choice
## Bind tells that this session refers to this respective engine

Base = declarative_base() ## ORM, heritage making the model, the actual orm is here

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()