from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Boolean, Float, ForeignKey
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String,Table, Enum as EnumDB
from enum import Enum
from database import Base
from pydantic import BaseModel
from sqlalchemy.orm import relationship


class PessoaPossuiDiagnostico(Base):
    '''Classe para estabelecer o modelo da tabela na DB'''
    __tablename__ = "pessoaPossuiDiagnostico"

    idDiagnostico: int = Column("idDiagnostico", ForeignKey("diagnostico.idDiagnostico", ondelete="CASCADE"), index=True,  primary_key=True)
    cpfProfissional: str =  Column("cpfProfissional", ForeignKey("profissional.cpf", ondelete="CASCADE"), index=True,  primary_key=True)
    idPessoa: int = Column("idPessoa", ForeignKey("pessoa.idPessoa"), index=True, primary_key=True)
    

class PessoaPossuiDiagnosticoBase(BaseModel):
    idDiagnostico:int
    cpfProfissional:str
    idPessoa:int
    class Config:
        orm_mode = True

class PessoaPossuiDiagnosticoRequest(PessoaPossuiDiagnosticoBase):
    ...
    pass


class Diagnostico(Base):
    '''Classe para estabelecer o modelo da tabela na DB'''
    __tablename__ = "diagnostico"

    idDiagnostico: int = Column(Integer, primary_key=True, nullable=False,  index= True)
    descricaoDiagnostico: str = Column(String(250), nullable=False)

    profissionais = relationship(
        "Profissional",
        secondary="pessoaPossuiDiagnostico",
        back_populates="diagnosticos",
        overlaps="pessoas",
    )

    pessoas = relationship(
        "Pessoa",
        secondary="pessoaPossuiDiagnostico",
        back_populates="diagnosticos",
        overlaps="profissionais",
       
    )




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