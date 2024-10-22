from http import HTTPStatus

from fastapi import Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from ..database import get_db
from ..models.clinicas_tem_funcionarios import ClinicasTemFuncionarios
from ..schemas.clinicas_tem_funcionarios import ClinicasTemFuncionariosSchema

def criar_clinicas_tem_funcionarios(
    clinica_tem_funcionario: ClinicasTemFuncionariosSchema,
    session: Session = Depends(get_db)
):
    db_clinica_funcionarios = session.scalar(
        select(ClinicasTemFuncionarios).where(
            (ClinicasTemFuncionarios.clinica_cnpj == 
             clinica_tem_funcionario.clinica_cnpj) & 
            (ClinicasTemFuncionarios.funcionario_cpf == 
             clinica_tem_funcionario.funcionario_cpf)
        )
    )

    if db_clinica_funcionarios:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Relação já cadastrada no sistema',
        )

    db_clinica_funcionarios = ClinicasTemFuncionarios(
        **clinica_tem_funcionario.model_dump()
    )

    session.add(db_clinica_funcionarios)
    session.commit()
    session.refresh(db_clinica_funcionarios)

    return db_clinica_funcionarios

def listar_clinicas_tem_funcionarios(session: Session = Depends(get_db)):
    return session.scalars(select(ClinicasTemFuncionarios))

def buscar_funcionarios_de_clinica(
    cnpj: str,
    session: Session = Depends(get_db)
):
    db_clinica_funcionarios = session.scalars(
        select(ClinicasTemFuncionarios).where(
            ClinicasTemFuncionarios.clinica_cnpj == cnpj
        )
    )

    if not db_clinica_funcionarios:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Clinica não encontrada',
        )

    return db_clinica_funcionarios

def buscar_clinicas_de_funcionario(
    cpf: str,
    session: Session = Depends(get_db)
):
    db_clinica_funcionarios = session.scalars(
        select(ClinicasTemFuncionarios).where(
            ClinicasTemFuncionarios.funcionario_cpf == cpf
        )
    )

    if not db_clinica_funcionarios:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Funcionário não encontrado',
        )

    return db_clinica_funcionarios

def atualizar_clinicas_tem_funcionarios(
    cnpj: str,
    cpf: str,
    clinica_tem_funcionario: ClinicasTemFuncionariosSchema,
    session: Session = Depends(get_db)
):
    db_clinica_funcionarios = session.scalar(
        select(ClinicasTemFuncionarios).where(
            (ClinicasTemFuncionarios.clinica_cnpj == 
             cnpj) & 
            (ClinicasTemFuncionarios.funcionario_cpf == 
             cpf)
        )
    )

    if not db_clinica_funcionarios:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Relação não encontrada',
        )

    db_clinica_funcionarios.clinica_cnpj = (
        clinica_tem_funcionario.clinica_cnpj
    )
    db_clinica_funcionarios.funcionario_cpf = (
        clinica_tem_funcionario.funcionario_cpf
    )
    db_clinica_funcionarios.data_inicio = (
        clinica_tem_funcionario.data_inicio
    )
    db_clinica_funcionarios.data_fim = (
        clinica_tem_funcionario.data_fim
    )

    session.commit()
    session.refresh(db_clinica_funcionarios)

    return db_clinica_funcionarios

def deletar_clinicas_tem_funcionarios(
    cnpj: str,
    cpf: str,
    session: Session = Depends(get_db)
):
    db_clinica_funcionarios = session.scalar(
        select(ClinicasTemFuncionarios).where(
            (ClinicasTemFuncionarios.clinica_cnpj == 
             cnpj) & 
            (ClinicasTemFuncionarios.funcionario_cpf == 
             cpf)
        )
    )

    if not db_clinica_funcionarios:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Relação não encontrada',
        )

    session.delete(db_clinica_funcionarios)
    session.commit()

    return db_clinica_funcionarios

