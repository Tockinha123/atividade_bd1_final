from http import HTTPStatus

from fastapi import Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from ..database import get_db
from ..models.clinicas import Clinicas
from ..schemas.clinicas import ClinicaPublic, ClinicaSchema


def criar_clinica(clinica: ClinicaSchema, session: Session = Depends(get_db)):
    db_clinica = session.scalar(
        select(Clinicas).where(Clinicas.cnpj == clinica.cnpj)
    )

    if db_clinica:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Clinica já cadastrada no sistema',
        )

    db_clinica = Clinicas(**clinica.model_dump())

    session.add(db_clinica)
    session.commit()
    session.refresh(db_clinica)

    return db_clinica


def listar_clinicas(session: Session = Depends(get_db)):
    return session.scalars(select(Clinicas))


def buscar_clinica(cnpj: str, session: Session = Depends(get_db)):
    db_clinica = session.scalar(select(Clinicas).where(Clinicas.cnpj == cnpj))

    if not db_clinica:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Clinica não encontrada',
        )

    return db_clinica


def atualizar_clinica(
    cnpj: str,
    clinica: ClinicaPublic,
    session: Session = Depends(get_db),
):
    db_clinica = session.scalar(select(Clinicas).where(Clinicas.cnpj == cnpj))

    if not db_clinica:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Clinica não encontrada',
        )

    db_clinica.update(**clinica.model_dump())
    session.commit()
    session.refresh(db_clinica)

    return db_clinica


def deletar_clinica(cnpj: str, session: Session = Depends(get_db)):
    db_clinica = session.scalar(select(Clinicas).where(Clinicas.cnpj == cnpj))

    if not db_clinica:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Clinica não encontrada',
        )

    session.delete(db_clinica)
    session.commit()

    return {'message': 'Clinica deletada com sucesso'}
