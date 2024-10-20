from typing import Optional

from pydantic import BaseModel, EmailStr, constr


class ClinicaSchema(BaseModel):
    cnpj: constr(min_length=14, max_length=14)
    nome: constr(max_length=45)
    bairro: constr(max_length=45)
    rua: constr(max_length=45)
    numero: int
    cep: constr(min_length=8, max_length=8)
    telefone: constr(max_length=15)
    email: EmailStr
    num_funcionarios: Optional[int]


class ClinicaPublic(BaseModel):
    nome: constr(max_length=45)
    bairro: constr(max_length=45)
    rua: constr(max_length=45)
    numero: int
    cep: constr(min_length=8, max_length=8)
    telefone: constr(max_length=15)
    email: EmailStr
    num_funcionarios: Optional[int]
