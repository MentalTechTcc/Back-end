from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Boolean, Float, ForeignKey
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Enum as EnumDB
from enum import Enum
from database import Base
from pydantic import BaseModel



class Consulta(Base):
    '''Classe para estabelecer o modelo da tabela na DB'''
    __tablename__ = "consulta"

    idConsulta: int = Column(Integer, primary_key=True, nullable=False,  index= True)
    valor: float = Column(Float, nullable=False)
    idAgenda: int = Column("idAgenda", ForeignKey("agenda.idAgenda"), index=True)
    idPessoa: int = Column("idPessoa", ForeignKey("pessoa.idPessoa"), index=True)
    permiteCompartilharConhecimento: bool = Column(Boolean, nullable=False)
    ocorreu: bool = Column(Boolean, nullable=False)


class ConsultaBase(BaseModel):
    valor: float
    idAgenda: int 
    idPessoa: int
    permiteCompartilharConhecimento: bool
    ocorreu: bool

class ConsultaRequest(ConsultaBase):
    '''...'''
    pass

class ConsultaRequestId(ConsultaBase):
    """Necessário para se fazer o update"""
    idConsulta: int

class ConsultaResponse(ConsultaBase):
    '''...'''
    idConsulta:int
    class Config:
        orm_mode = True