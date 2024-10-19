from enum import Enum

from pydantic import BaseModel, constr


class CargoFuncionario(str, Enum):
    recepcionista = 'recepcionista'
    medico = 'medico'


class FuncionarioSchema(BaseModel):
    cpf: constr(min_length=11, max_length=11)
    primeiro_nome: constr(max_length=45)
    sobrenome: constr(max_length=45)
    cargo: CargoFuncionario
    telefone: constr(min_length=11, max_length=11)


class FuncionarioPublic(BaseModel):
    primeiro_nome: constr(max_length=45)
    sobrenome: constr(max_length=45)
    cargo: CargoFuncionario
    telefone: constr(min_length=11, max_length=11)


class Message(BaseModel):
    message: str
