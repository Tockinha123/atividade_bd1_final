from pydantic import BaseModel, constr
from typing import Optional
from datetime import date

class ClinicasTemFuncionariosSchema(BaseModel):
    clinica_cnpj: constr(min_length=14, max_length=14)
    funcionario_cpf: constr(min_length=11, max_length=11)
    data_inicio: date
    data_fim: Optional[date]  = None