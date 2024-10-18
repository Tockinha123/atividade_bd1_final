from sqlalchemy.orm import Session
from fastapi import HTTPException, Depends
from sqlalchemy import select
from ..models.funcionarios import Funcionarios
from ..schemas.funcionarios import FuncionarioPublic, FuncionarioSchema
from ..database import get_db


def criar_funcionario(
    funcionario: FuncionarioSchema, session: Session = Depends(get_db)
):
    db_funcionario = session.scalar(
        select(Funcionarios).where(Funcionarios.cpf == funcionario.cpf)
    )

    if db_funcionario:
        raise HTTPException(
            status_code=404, detail="Funcionário já cadastrado no sistema"
        )

    novo_funcionario = Funcionarios(
        cpf=funcionario.cpf,
        primeiro_nome=funcionario.primeiro_nome,
        sobrenome=funcionario.sobrenome,
        cargo=funcionario.cargo,
        telefone=funcionario.telefone,
    )

    return novo_funcionario