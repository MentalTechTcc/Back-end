from sqlalchemy import Column, String, Boolean, ForeignKey, Table
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Enum as EnumDB
from enum import Enum
from database import Base
from pydantic import BaseModel

profissional_possui_endereco = Table(
    "profissional_possui_endereco",
    Base.metadata,
    Column("endereco_id", Integer, ForeignKey("endereco.idEndereco")),
    Column("profissional_cpf", String, ForeignKey("profissional.cpf")),
)

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
        secondary=profissional_possui_endereco,
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