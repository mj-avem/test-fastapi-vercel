from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class RecenseadorModel(Base):
    __tablename__ = 'recenseadores'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    usuario = Column(String(50), nullable=False, unique=True)
    senha = Column(String(255), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    data_nascimento = Column(Date, nullable=False)
    ativo = Column(Boolean, nullable=False)
