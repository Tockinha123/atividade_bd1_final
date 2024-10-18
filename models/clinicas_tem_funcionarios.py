from sqlalchemy import Table, MetaData
from ..database import engine

metadata = MetaData()
clinicas_tem_funcionarios = Table('clinicas_tem_funcionarios', metadata, autoload_with=engine)

