from http import HTTPStatus

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..crud import funcionarios as crud_funcionarios
from ..database import get_db
from ..schemas.funcionarios import (
    FuncionarioPublic,
    FuncionarioSchema,
    Message,
)

router = APIRouter(prefix='/funcionarios', tags=['Funcionários'])


@router.post(
    '/criar_funcionario',
    response_model=FuncionarioPublic,
    status_code=HTTPStatus.CREATED,
)
def criar_funcionario(
    funcionario: FuncionarioSchema, session: Session = Depends(get_db)
):
    return crud_funcionarios.criar_funcionario(funcionario, session)


@router.get(
    '/listar_funcionarios',
    status_code=HTTPStatus.OK,
    response_model=list[FuncionarioPublic],
)
def listar_funcionarios(session: Session = Depends(get_db)):
    return crud_funcionarios.listar_funcionarios(session)


@router.get(
    'buscar_funcionario/{cpf}',
    status_code=HTTPStatus.OK,
    response_model=FuncionarioPublic,
)
def buscar_funcionario(cpf: str, session: Session = Depends(get_db)):
    return crud_funcionarios.buscar_funcionario(cpf, session)


@router.put(
    '/atualizar_funcionario/{cpf}',
    response_model=FuncionarioPublic,
    status_code=HTTPStatus.OK,
)
def atualizar_funcionario(
    cpf: str,
    funcionario: FuncionarioSchema,
    session: Session = Depends(get_db),
):
    return crud_funcionarios.atualizar_funcionario(cpf, funcionario, session)


@router.delete(
    '/deletar_funcionario/{cpf}',
    response_model=Message,
    status_code=HTTPStatus.NO_CONTENT,
)
def deletar_funcionario(cpf: str, session: Session = Depends(get_db)):
    return crud_funcionarios.deletar_funcionario(cpf, session)
