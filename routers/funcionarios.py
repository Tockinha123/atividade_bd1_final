from http import HTTPStatus

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..crud import funcionarios as crud_funcionarios
from ..database import get_db
from ..schemas.funcionarios import FuncionarioPublic, FuncionarioSchema

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
