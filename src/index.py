from fastapi import FastAPI
from src.route import router

app = FastAPI()

app.include_router(router)
