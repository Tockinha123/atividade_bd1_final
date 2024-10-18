from sqlalchemy import Table, MetaData
from ..database import engine

metadata = MetaData()
clinicas = Table('clinicas', metadata, autoload_with=engine)
