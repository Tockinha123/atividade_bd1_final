from sqlalchemy import MetaData, Table

from ..database import engine

metadata = MetaData()
Clinicas = Table('clinicas', metadata, autoload_with=engine)
