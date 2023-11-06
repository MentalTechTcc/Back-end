from sqlalchemy import Column, String, Boolean, ForeignKey, Table
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Enum as EnumDB
from enum import Enum
from database import Base
from pydantic import BaseModel

class ProfissionalPossuiEndereco(Base):
    '''Classe para estabelecer o modelo da tabela na DB'''
    __tablename__ = "profissionalPossuiEndereco"

    idEndereco: int = Column("idEndereco", ForeignKey("endereco.idEndereco"), index=True,  primary_key=True)
    cpfProfissional: str =  Column("cpfProfissional", ForeignKey("profissional.cpf", ondelete="CASCADE"), index=True,  primary_key=True)
 
class ProfissionalPossuiEnderecoBase(BaseModel):
    idEndereco:int
    cpfProfissional:str
    class Config:
        orm_mode = True

class ProfissionalPossuiEnderecoRequest(ProfissionalPossuiEnderecoBase):
    ...
    pass


class Endereco(Base):
    __tablename__ = "endereco"
    
    idEndereco = Column(Integer, primary_key=True, index=True)
    cep = Column(String(10), nullable=False)
    estado = Column(String(50), nullable=False)
    cidade = Column(String(100), nullable=False)
    bairro = Column(String(100), nullable=False)
    numero = Column(Integer, nullable=False)
    complemento = Column(String(200))
    
    profissionais = relationship(
        "Profissional",
        secondary="profissionalPossuiEndereco",
        back_populates="enderecos",
    )

class EnderecoBase(BaseModel):
    cep: str
    estado: str
    cidade: str
    bairro: str
    numero: int
    complemento: str

class EnderecoRequest(EnderecoBase):
    '''...'''
    pass

class EnderecoRequestId(EnderecoBase):
    """Necessário para se fazer o update"""
    idEndereco: int

class EnderecoResponse(EnderecoBase):
    '''...'''
    idEndereco:int
    class Config:
        orm_mode = True