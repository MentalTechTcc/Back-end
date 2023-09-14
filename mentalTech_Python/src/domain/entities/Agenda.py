from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Boolean, ForeignKey
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Enum as EnumDB
from enum import Enum
from database import Base
from pydantic import BaseModel

class Modalidade(Enum):
    PRESENCIAL = 1
    ONLINE = 2


class Agenda(Base):
    __tablename__ = "agenda"

    idAgenda: int = Column(Integer, primary_key=True, nullable=False, index=True)
    data: str = Column(String(8), nullable=False)
    hora: str = Column(String(8), nullable=False)
    duracao: str = Column(String(10), nullable=False) 
    cpfProfissional: str = Column("cpfProfissional", ForeignKey("profissional.cpf"), index=True)
    modalidadeAtendimento: Enum = Column(EnumDB(Modalidade), nullable=False)


class AgendaBase(BaseModel):
    idAgenda: int 
    data: str
    hora: str
    duracao: str
    cpfProfissional: str
    modalidadeAtendimento: Modalidade 

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