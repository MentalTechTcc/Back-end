from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Table, Enum as EnumDB
from sqlalchemy.orm import relationship
from enum import Enum
from database import Base
from pydantic import BaseModel


class ProfissionalPossuiEspecialidade(Base):
    '''Classe para estabelecer o modelo da tabela na DB'''
    __tablename__ = "profissionalPossuiEspecialidade"

    idEspecialidade: int =  Column("idEspecialidade", ForeignKey("especialidade.idEspecialidade", ondelete="CASCADE"), index=True,  primary_key=True)
    cpfProfissional: str = Column("cpfProfissional", ForeignKey("profissional.cpf", ondelete="CASCADE"), index=True,  primary_key=True)

class ProfissionalPossuiEspecialidadeBase(BaseModel):
    idEspecialidade:str
    cpfProfissional:str
    class Config:
        orm_mode = True

class ProfissionalPossuiEspecialidadeRequest(ProfissionalPossuiEspecialidadeBase):
    ...
    pass


class Especialidade(Base):
    '''Classe para estabelecer o modelo da tabela na DB'''
    __tablename__ = "especialidade"
    
    idEspecialidade: int = Column(Integer, nullable=False, primary_key=True)
    descricaoEspecialidade: str = Column(String(200), nullable=False)
    profissionais = relationship(
        "Profissional",
        secondary="profissionalPossuiEspecialidade",
        back_populates="especialidades",
    )

class EspecialidadeBase(BaseModel): 
    descricaoEspecialidade: str

class EspecialidadeRequest(EspecialidadeBase):
    '''...'''
    pass

class EspecialidadeRequestId(EspecialidadeBase):
    """Necessário para se fazer o update"""
    idEspecialidade : int

class EspecialidadeResponse(EspecialidadeBase):
    '''...'''
    idEspecialidade:int
    class Config:
        orm_mode = True