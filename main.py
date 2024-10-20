from fastapi import FastAPI

from .routers import funcionarios, clinicas

app = FastAPI()

app.include_router(funcionarios.router)
app.include_router(clinicas.router)
