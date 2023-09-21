from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Table, Enum as EnumDB
from sqlalchemy.orm import relationship
from enum import Enum
from database import Base
from pydantic import BaseModel


profissional_possui_especialidade = Table(
    'profissional_possui_especialidade',
    Base.metadata,
    Column('profissional_id', Integer, ForeignKey('profissional.idPessoa')),
    Column('especialidade_id', Integer, ForeignKey('especialidade.idEspecialidade'))
)

class DescricaoEspecialidade(Enum):
    PSCICOLOGIA = 1
    PSIQUIATRIA = 2
    PSICANALISE = 3


class Especialidade(Base):
    '''Classe para estabelecer o modelo da tabela na DB'''
    __tablename__ = "especialidade"
    
    idEspecialidade: int = Column(Integer, nullable=False, primary_key=True)
    descricaoEspecialidade: Enum = Column(EnumDB(DescricaoEspecialidade), nullable=False)
    profissionais = relationship(
        "Profissional",
        secondary=profissional_possui_especialidade,
        back_populates="especialidades",
    )

class EspecialidadeBase(BaseModel): 
    idEspecialidade: int

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