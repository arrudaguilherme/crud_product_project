from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine
import models
from router import router

models.Base.metadata.create_all(bind=engine) ## create the tables

app = FastAPI()
app.include_router(router=router)

origins = [
    "http://localhost:8501",  # Porta do Streamlit
    "http://127.0.0.1:8501"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Permitir apenas esses domínios
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos os métodos HTTP (GET, POST, DELETE, etc.)
    allow_headers=["*"],  # Permitir todos os cabeçalhos
)