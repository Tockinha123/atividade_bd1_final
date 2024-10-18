from sqlalchemy import Table, MetaData
from ..database import engine

metadata = MetaData()
Clinicas_tem_funcionarios = Table('clinicas_tem_funcionarios', metadata, autoload_with=engine)

