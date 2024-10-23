from http import HTTPStatus

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..crud import clinicas_tem_funcionarios as crud_clinicas_tem_funcionarios
from ..database import get_db
from ..schemas.clinicas_tem_funcionarios import (
    ClinicasDeUmFuncionario,
    ClinicasTemFuncionariosSchema,
    FuncionariosDeUmaClinica,
)

router = APIRouter(
    prefix='/relacao_clinica_funcionario', tags=['Relacionamento']
)


@router.post(
    '/criar_relacao',
    response_model=ClinicasTemFuncionariosSchema,
    status_code=HTTPStatus.CREATED,
)
def criar_clinicas_tem_funcionarios(
    clinica_tem_funcionario: ClinicasTemFuncionariosSchema,
    session: Session = Depends(get_db),
):
    return crud_clinicas_tem_funcionarios.criar_clinicas_tem_funcionarios(
        clinica_tem_funcionario, session
    )


@router.get(
    '/listar_relacoes',
    response_model=list[ClinicasTemFuncionariosSchema],
    status_code=HTTPStatus.OK,
)
def listar_clinicas_tem_funcionarios(session: Session = Depends(get_db)):
    return crud_clinicas_tem_funcionarios.listar_clinicas_tem_funcionarios(
        session
    )


@router.get(
    '/buscar_funcionarios_de_clinica/{cnpj}',
    response_model=list[FuncionariosDeUmaClinica],
    status_code=HTTPStatus.OK,
)
def buscar_funcionarios_de_clinica(
    cnpj: str, session: Session = Depends(get_db)
):
    return crud_clinicas_tem_funcionarios.buscar_funcionarios_de_clinica(
        cnpj, session
    )


@router.get(
    '/buscar_clinicas_de_funcionario/{cpf}',
    response_model=list[ClinicasDeUmFuncionario],
    status_code=HTTPStatus.OK,
)
def buscar_clinicas_de_funcionario(
    cpf: str, session: Session = Depends(get_db)
):
    return crud_clinicas_tem_funcionarios.buscar_clinicas_de_funcionario(
        cpf, session
    )


@router.put(
    '/atualizar_relacao/{clinica_cnpj}/{funcionario_cpf}',
    status_code=HTTPStatus.OK,
)
def atualizar_clinicas_tem_funcionarios(
    clinica_cnpj: str,
    funcionario_cpf: str,
    clinica_tem_funcionario: ClinicasTemFuncionariosSchema,
    session: Session = Depends(get_db),
):
    return crud_clinicas_tem_funcionarios.atualizar_clinicas_tem_funcionarios(
        clinica_cnpj, funcionario_cpf, clinica_tem_funcionario, session
    )


@router.delete(
    '/deletar_relacao/{clinica_cnpj}/{funcionario_cpf}',
    status_code=HTTPStatus.OK,
)
def deletar_clinicas_tem_funcionarios(
    clinica_cnpj: str, funcionario_cpf: str, session: Session = Depends(get_db)
):
    return crud_clinicas_tem_funcionarios.deletar_clinicas_tem_funcionarios(
        clinica_cnpj, funcionario_cpf, session
    )
