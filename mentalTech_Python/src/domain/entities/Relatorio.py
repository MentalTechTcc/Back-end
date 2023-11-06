from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Boolean, Float, ForeignKey
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Date,func, DateTime, Enum as EnumDB
from enum import Enum
from database import Base
from pydantic import BaseModel
from datetime import date


class Relatorio(Base):
    '''Classe para estabelecer o modelo da tabela na DB'''
    __tablename__ = "relatorio"

    idRelatorio: int = Column(Integer, primary_key=True, nullable=False,  index= True)
    descricao: str = Column(String(500), nullable=False)
    idConsulta: int = Column("idConsulta", ForeignKey("consulta.idConsulta", ondelete="CASCADE"), index=True)
    dataCadastro = Column(DateTime, server_default=func.now())    


class RelatorioBase(BaseModel):
    descricao: str
    idConsulta: int 
    dataCadastro: date 

class RelatorioRequest(RelatorioBase):
    '''...'''
    pass

class RelatorioRequestId(RelatorioBase):
    """Necessário para se fazer o update"""
    idRelatorio: int

class RelatorioResponse(RelatorioBase):
    '''...'''
    idRelatorio:int
    class Config:
        orm_mode = True