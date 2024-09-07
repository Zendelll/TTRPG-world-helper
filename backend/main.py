import os
from fastapi import FastAPI
from app.routers import entities
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.include_router(entities.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Pf2E knowledge base!"}
