from sqlalchemy import MetaData

from ..database import Base, engine

metadata_obj = MetaData(schema='sistema_medico')
metadata_obj.reflect(engine)
clinicas_tem_funcionarios = metadata_obj.tables[
    'sistema_medico.clinicas_tem_funcionarios'
]


class ClinicasTemFuncionarios(Base):
    __table__ = clinicas_tem_funcionarios
