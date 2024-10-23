from datetime import date
from typing import Optional

from pydantic import BaseModel, constr


class ClinicasTemFuncionariosSchema(BaseModel):
    clinica_cnpj: constr(min_length=14, max_length=14)
    funcionario_cpf: constr(min_length=11, max_length=11)
    data_inicio: date
    data_fim: Optional[date] = None


class FuncionariosDeUmaClinica(BaseModel):
    funcionario_cpf: constr(min_length=11, max_length=11)
    data_inicio: date
    data_fim: Optional[date] = None


class ClinicasDeUmFuncionario(BaseModel):
    clinica_cnpj: constr(min_length=14, max_length=14)
    data_inicio: date
    data_fim: Optional[date] = None
