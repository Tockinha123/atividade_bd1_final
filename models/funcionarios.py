from sqlalchemy import Table, MetaData
from ..database import engine

metadata = MetaData()
Funcionarios = Table(
    'funcionarios',
    metadata,
    schema='sistema_medico',
    autoload_with=engine,
)