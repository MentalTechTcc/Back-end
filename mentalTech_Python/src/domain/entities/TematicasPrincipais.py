from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey,Enum as EnumDB
from sqlalchemy.orm import relationship
from enum import Enum
from database import Base
from pydantic import BaseModel

class ProfissionalTrataTematicas(Base):
    '''Classe para estabelecer o modelo da tabela na DB'''
    __tablename__ = "profissionalTrataTematicasPrincipais"

    idTematicasPrincipais: int =  Column("idTematicasPrincipais", ForeignKey("tematicasPrincipais.idTematicasPrincipais"), index=True,  primary_key=True)
    cpfProfissional: str = Column("cpfProfissional", ForeignKey("profissional.cpf"), index=True,  primary_key=True)

class ProfissionalTrataTematicasBase(BaseModel):
    idTematicasPrincipais:str
    cpfProfissional:str
    class Config:
        orm_mode = True

class ProfissionalTrataTematicasRequest(ProfissionalTrataTematicasBase):
    ...
    pass


class TematicasPrincipais(Base):
    '''Classe para estabelecer o modelo da tabela na DB'''
    __tablename__ = "tematicasPrincipais"

    idTematicasPrincipais: int = Column(Integer, primary_key=True, nullable=False,  index= True)
    nomeTematica: str = Column(String(250), nullable=False)
    profissionais = relationship(
        "Profissional",
        secondary="profissionalTrataTematicasPrincipais",
        back_populates="tematicasPrincipais",
    )
   


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