from fastapi import FastAPI

from .routers import clinicas, funcionarios, clinicas_tem_funcionarios

app = FastAPI()

app.include_router(funcionarios.router)
app.include_router(clinicas.router)
app.include_router(clinicas_tem_funcionarios.router)