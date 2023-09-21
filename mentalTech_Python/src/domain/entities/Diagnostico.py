from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Boolean, Float, ForeignKey
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Enum as EnumDB
from enum import Enum
from database import Base
from pydantic import BaseModel



class Diagnostico(Base):
    '''Classe para estabelecer o modelo da tabela na DB'''
    __tablename__ = "diagnostico"

    idDiagnostico: int = Column(Integer, primary_key=True, nullable=False,  index= True)
    descricaoDiagnostico: str = Column(String(250), nullable=False)


class DiagnosticoBase(BaseModel):
    descricaoDiagnostico: str

class DiagnosticoRequest(DiagnosticoBase):
    '''...'''
    pass

class DiagnosticoRequestId(DiagnosticoBase):
    """Necessário para se fazer o update"""
    idDiagnostico: int

class DiagnosticoResponse(DiagnosticoBase):
    '''...'''
    idDiagnostico:int
    class Config:
        orm_mode = True