from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Enum as EnumDB
from enum import Enum
from database import Base
from pydantic import BaseModel



class TematicasPrincipais(Base):
    '''Classe para estabelecer o modelo da tabela na DB'''
    __tablename__ = "tematicasPrincipais"

    idTematicasPrincipais: int = Column(Integer, primary_key=True, nullable=False,  index= True)
    nomeTematica: str = Column(String(250), nullable=False)
   


class TematicasPrincipaisBase(BaseModel):
    nomeTematica: str 

class TematicasPrincipaisRequest(TematicasPrincipaisBase):
    '''...'''
    pass

class TematicasPrincipaisRequestId(TematicasPrincipaisBase):
    """Necessário para se fazer o update"""
    idTematicasPrincipais: int

class TematicasPrincipaisResponse(TematicasPrincipaisBase):
    '''...'''
    idTematicasPrincipais:int
    class Config:
        orm_mode = True