from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Boolean, Float, ForeignKey, DateTime, func
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Enum as EnumDB
from enum import Enum
from database import Base
from pydantic import BaseModel
from datetime import date



class DicaSaude(Base):
    '''Classe para estabelecer o modelo da tabela na DB'''
    __tablename__ = "dicaSaude"

    idDicaSaude: int = Column(Integer, primary_key=True, nullable=False,  index= True)
    descricaoDica: str = Column(String(500), nullable=False)
    cpfProfissional: str = Column("cpfProfissional", ForeignKey("profissional.cpf"), index=True)
    dataCadastro = Column(DateTime, server_default=func.now()) 
    


class DicaSaudeBase(BaseModel):
    descricaoDica: str
    cpfProfissional: str 
    dataCadastro:date
    

class DicaSaudeRequest(DicaSaudeBase):
    '''...'''
    pass

class DicaSaudeRequestId(DicaSaudeBase):
    """Necessário para se fazer o update"""
    idDicaSaude: int

class DicaSaudeResponse(DicaSaudeBase):
    '''...'''
    idDicaSaude:int
    class Config:
        orm_mode = True