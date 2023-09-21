from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Boolean, Float, ForeignKey
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Enum as EnumDB
from enum import Enum
from database import Base
from pydantic import BaseModel



class DicaSaude(Base):
    '''Classe para estabelecer o modelo da tabela na DB'''
    __tablename__ = "dicaSaude"

    idDicaSaude: int = Column(Integer, primary_key=True, nullable=False,  index= True)
    descricaoDica: str = Column(String(500), nullable=False)
    cpfProfissional: str = Column("cpfProfissional", ForeignKey("profissional.cpf"), index=True)
    


class DicaSaudeBase(BaseModel):
    descricaoDica: str
    cpfProfissional: str 
    

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