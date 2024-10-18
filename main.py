from fastapi import FastAPI
from .routers import funcionarios

app = FastAPI()

app.include_router(funcionarios.router)

