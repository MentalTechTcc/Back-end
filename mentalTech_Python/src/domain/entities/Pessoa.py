from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Boolean
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Enum as EnumDB
from enum import Enum
from database import Base
from pydantic import BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String,func, DateTime, Date
from datetime import date
from domain.entities.Diagnostico import PessoaPossuiDiagnostico

class Sexo(Enum):
    F = 1
    M = 2


class Pessoa(Base):
    '''Classe para estabelecer o modelo da tabela na DB'''
    __tablename__ = "pessoa"
    

    nome: str = Column(String(100), nullable=False)
    idPessoa: int = Column(Integer, primary_key=True, nullable=False,  index= True)
    senha: str = Column(String(100), nullable=False)
    dataNascimento =Column(Date, nullable=False)    
    telefone: str = Column(String(11), nullable=False)
    email: str = Column(String(100), nullable=False, unique=True)
    sexo: Enum = Column(EnumDB(Sexo), nullable=False)
    administrador: bool = Column(Boolean, nullable=False)
    dataCadastro = Column(DateTime, server_default=func.now()) 
    diagnosticos = relationship(
        "Diagnostico",
        secondary="pessoaPossuiDiagnostico",
        back_populates="pessoas",
        overlaps="profissionais",
    )


class PessoaBase(BaseModel):
    nome: str
    senha: str
    dataNascimento: date
    telefone: str
    email: str
    administrador: bool
    sexo: Sexo
    dataCadastro: date 


class PessoaRequest(PessoaBase):
    '''...'''
    pass

class PessoaRequestId(PessoaBase):
    """Necessário para se fazer o update"""
    idPessoa : int

class PessoaResponse(PessoaBase):
    '''...'''
    idPessoa:int
    class Config:
        orm_mode = True