from sqlalchemy import Table, MetaData
from ..database import engine

metadata = MetaData()
Clinicas = Table('clinicas', metadata, autoload_with=engine)
