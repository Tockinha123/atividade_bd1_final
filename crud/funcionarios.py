from http import HTTPStatus

from fastapi import Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from ..database import get_db
from ..models.funcionarios import Funcionarios
from ..schemas.funcionarios import FuncionarioPublic, FuncionarioSchema


def criar_funcionario(
    funcionario: FuncionarioSchema, session: Session = Depends(get_db)
):
    db_funcionario = session.scalar(
        select(Funcionarios).where(Funcionarios.cpf == funcionario.cpf)
    )

    if db_funcionario:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Funcionário já cadastrado no sistema',
        )

    db_funcionario = Funcionarios(
        cpf=funcionario.cpf,
        primeiro_nome=funcionario.primeiro_nome,
        sobrenome=funcionario.sobrenome,
        cargo=funcionario.cargo,
        telefone=funcionario.telefone,
    )

    session.add(db_funcionario)
    session.commit()
    session.refresh(db_funcionario)

    return db_funcionario


def listar_funcionarios(session: Session = Depends(get_db)):
    return session.scalars(select(Funcionarios))


def buscar_funcionario(cpf: str, session: Session = Depends(get_db)):
    db_funcionario = session.scalar(
        select(Funcionarios).where(Funcionarios.cpf == cpf)
    )

    if not db_funcionario:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Funcionário não encontrado',
        )

    return db_funcionario


def atualizar_funcionario(
    cpf: str,
    funcionario: FuncionarioPublic,
    session: Session = Depends(get_db),
):
    db_funcionario = session.scalar(
        select(Funcionarios).where(Funcionarios.cpf == cpf)
    )

    if not db_funcionario:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Funcionário não encontrado',
        )

    db_funcionario.primeiro_nome = funcionario.primeiro_nome
    db_funcionario.sobrenome = funcionario.sobrenome
    db_funcionario.cargo = funcionario.cargo
    db_funcionario.telefone = funcionario.telefone

    session.commit()
    session.refresh(db_funcionario)

    return db_funcionario


def deletar_funcionario(cpf: str, session: Session = Depends(get_db)):
    db_funcionario = session.scalar(
        select(Funcionarios).where(Funcionarios.cpf == cpf)
    )

    if not db_funcionario:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Funcionário não encontrado',
        )

    session.delete(db_funcionario)
    session.commit()

    return {'message': 'Funcionário deletado com sucesso'}
