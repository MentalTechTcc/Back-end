from sqlalchemy import Column, Integer, String, Boolean, Enum as EnumDB
from sqlalchemy.orm import relationship
from enum import Enum
from database import Base
from domain.entities.Pessoa import PessoaBase, Sexo
from domain.entities.Especialidade import profissional_possui_especialidade
from domain.entities.Diagnostico import PessoaPossuiDiagnostico


class Profissional(Base):
    '''Classe para estabelecer o modelo da tabela na DB'''
    __tablename__ = "profissional"
    

    nome: str = Column(String(100), nullable=False)
    idPessoa: int = Column(Integer, primary_key=True, nullable=False,  index= True)
    senha: str = Column(String(100), nullable=False)
    dataNascimento: str = Column(String(10), nullable=False)    
    telefone: str = Column(String(11), nullable=False)
    email: str = Column(String(100), nullable=False, unique=True)
    sexo: Enum = Column(EnumDB(Sexo), nullable=False)
    administrador: bool = Column(Boolean, nullable=False)
    cpf: str = Column(String(11), nullable=False, unique=True)
    codigoProfissional: str = Column(String(100), nullable=False)
    descricaoProfissional: str = Column(String(500), nullable=False)
    enderecos = relationship(
        "Endereco",
        secondary="profissionalPossuiEndereco",
        back_populates="profissionais",
    )
    especialidades = relationship(
        "Especialidade",
        secondary=profissional_possui_especialidade,
        back_populates="profissionais",
    )
    diagnosticos = relationship(
        "Diagnostico",
        secondary="pessoaPossuiDiagnostico",
        back_populates="profissionais",
        overlaps="pessoas, diagnosticos",
    )

class ProfissionalBase(PessoaBase): 
    codigoProfissional: str
    descricaoProfissional: str
    cpf: str 

class ProfissionalRequest(ProfissionalBase):
    '''...'''
    pass

class ProfissionalRequestId(ProfissionalBase):
    """Necessário para se fazer o update"""
    idPessoa : int

class ProfissionalResponse(ProfissionalBase):
    '''...'''
    idPessoa:int
    class Config:
        orm_mode = True