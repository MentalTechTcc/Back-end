from sqlalchemy import Column, Integer, String, Boolean,func , DateTime, Enum as EnumDB
from sqlalchemy.orm import relationship
from typing import Optional
from enum import Enum
from database import Base
from domain.entities.Pessoa import PessoaBase, Sexo
from domain.entities.Diagnostico import PessoaPossuiDiagnostico
from datetime import date

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
    dataCadastro = Column(DateTime, server_default=func.now()) 
    pix: str = Column(String(500), nullable=False)
    imagem=Optional[bytes]
    enderecos = relationship(
        "Endereco",
        secondary="profissionalPossuiEndereco",
        back_populates="profissionais",
    )
    especialidades = relationship(
        "Especialidade",
        secondary="profissionalPossuiEspecialidade",
        back_populates="profissionais",
    )
    diagnosticos = relationship(
        "Diagnostico",
        secondary="pessoaPossuiDiagnostico",
        back_populates="profissionais",
        overlaps="pessoas, diagnosticos",
    )
    tematicasPrincipais = relationship(
        "TematicasPrincipais",
        secondary="profissionalTrataTematicasPrincipais",
        back_populates="profissionais",
    )

class ProfissionalBase(PessoaBase): 
    codigoProfissional: str
    descricaoProfissional: str
    cpf: str 
    pix: Optional[str]
    

class ProfissionalRequest(ProfissionalBase):
    '''...'''
    imagem: Optional[bytes]
    pass

class ProfissionalRequestId(ProfissionalBase):
    """Necessário para se fazer o update"""
    idPessoa : int

class ProfissionalResponse(ProfissionalBase):
    '''...'''
    idPessoa:int
    class Config:
        orm_mode = True