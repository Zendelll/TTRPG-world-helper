import os
from fastapi import FastAPI
from app.routers import entities
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(entities.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Pf2E knowledge base!"}
