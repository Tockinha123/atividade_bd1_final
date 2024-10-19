from sqlalchemy import MetaData

from ..database import Base, engine

metadata_obj = MetaData(schema='sistema_medico')
metadata_obj.reflect(engine)
funcionarios = metadata_obj.tables['sistema_medico.funcionarios']


class Funcionarios(Base):
    __table__ = funcionarios
