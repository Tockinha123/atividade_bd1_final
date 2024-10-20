from http import HTTPStatus

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..crud import clinicas as crud_clinicas
from ..database import get_db
from ..schemas.clinicas import ClinicaPublic, ClinicaSchema
from ..schemas.funcionarios import Message

router = APIRouter(prefix='/clinicas', tags=['Clinicas'])

@router.post(
    '/criar_clinica',
    response_model=ClinicaSchema,
    status_code=HTTPStatus.CREATED,
)
def criar_clinica(
    clinica: ClinicaSchema, session: Session = Depends(get_db)
):
    return crud_clinicas.criar_clinica(clinica, session)


@router.get(
    '/listar_clinicas',
    response_model=list[ClinicaSchema],
    status_code=HTTPStatus.OK,
)
def listar_clinicas(session: Session = Depends(get_db)):
    return crud_clinicas.listar_clinicas(session)

@router.get(
    '/buscar_clinica',
    response_model=ClinicaSchema,
    status_code=HTTPStatus.OK,
)
def buscar_clinica(cnpj: str, session: Session = Depends(get_db)):
    return crud_clinicas.buscar_clinica(cnpj, session)

@router.put(
    '/atualizar_clinica',
    response_model=ClinicaSchema,
    status_code=HTTPStatus.OK,
)
def atualizar_clinica(
    cnpj: str,
    clinica: ClinicaPublic,
    session: Session = Depends(get_db),
):
    return crud_clinicas.atualizar_clinica(cnpj, clinica, session)

def deletar_clinica(cnpj: str, session: Session = Depends(get_db)):
    return crud_clinicas.deletar_clinica(cnpj, session)