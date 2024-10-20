from sqlalchemy import MetaData

from ..database import Base, engine

metadata_obj = MetaData(schema='sistema_medico')
metadata_obj.reflect(engine)
clinicas = metadata_obj.tables['sistema_medico.clinicas']


class Clinicas(Base):
    __table__ = clinicas
