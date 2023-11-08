from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Boolean, ForeignKey, Float
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Enum as EnumDB, Date, Time
from enum import Enum
from database import Base
from pydantic import BaseModel
from datetime import date, time
from typing import Optional

class Modalidade(Enum):
    PRESENCIAL = 1
    ONLINE = 2


class Agenda(Base):
    __tablename__ = "agenda"

    idAgenda: int = Column(Integer, primary_key=True, nullable=False, index=True)
    data= Column(Date, nullable=False)
    hora = Column(Time, nullable=False)
    duracao: int = Column(Integer, nullable=False) 
    cpfProfissional: str = Column("cpfProfissional", ForeignKey("profissional.cpf", ondelete="CASCADE"), index=True)
    modalidadeAtendimento: Enum = Column(EnumDB(Modalidade), nullable=False)
    ocupado: bool = Column(Boolean, nullable=True, default=False)
    valorProposto: float = Column(Float, nullable=False)
    linkPagamento: str = Column(String(500), nullable=True)
    idEndereco: int = Column("idEndereco", ForeignKey("endereco.idEndereco"), index=True)



class AgendaBase(BaseModel):
    data: date
    hora: time
    duracao: int
    cpfProfissional: str
    modalidadeAtendimento: Modalidade 
    ocupado:bool
    valorProposto: float 
    linkPagamento: Optional[str]
    idEndereco: Optional[int]

class AgendaRequest(AgendaBase):
    '''...'''
    pass

class AgendaRequestId(AgendaBase):
    """Necessário para se fazer o update"""
    idAgenda: int

class AgendaResponse(AgendaBase):
    '''...'''
    idAgenda:int
    class Config:
        orm_mode = True