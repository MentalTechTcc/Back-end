from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, ForeignKey
from pydantic import BaseModel
from sqlalchemy import Integer, String, DateTime, func,Enum as EnumDB
from enum import Enum
from database import Base
from pydantic import BaseModel
from datetime import date



class Avaliacao(Base):
    '''Classe para estabelecer o modelo da tabela na DB'''
    __tablename__ = "avaliacao"

    idAvaliacao: int = Column(Integer, primary_key=True, nullable=False,  index= True)
    cpfProfissional: str = Column("cpfProfissional", ForeignKey("profissional.cpf", ondelete="CASCADE"), index=True)
    idPessoa: int = Column("idPessoa", ForeignKey("pessoa.idPessoa", ondelete="CASCADE"), index=True)
    notaGeral: int = Column(Integer, nullable=False)
    notaPontualidade: int = Column(Integer, nullable=True)
    notaAtendimento: int = Column(Integer, nullable=True)
    observacoes: str = Column(String(500), nullable=True)
    dataCadastro = Column(DateTime, server_default=func.now()) 



class AvaliacaoBase(BaseModel):
    cpfProfissional: str
    idPessoa: int 
    notaGeral: int 
    notaPontualidade: int 
    notaAtendimento: int 
    observacoes: str
    dataCadastro:date

class AvaliacaoRequest(AvaliacaoBase):
    '''...'''
    pass

class AvaliacaoRequestId(AvaliacaoBase):
    """Necessário para se fazer o update"""
    idAvaliacao: int

class AvaliacaoResponse(AvaliacaoBase):
    '''...'''
    idAvaliacao:int
    class Config:
        orm_mode = True