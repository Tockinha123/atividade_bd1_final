from sqlalchemy import Table, MetaData
from ..database import engine

metadata = MetaData()
funcionarios = Table('funcionarios', metadata, autoload_with=engine)