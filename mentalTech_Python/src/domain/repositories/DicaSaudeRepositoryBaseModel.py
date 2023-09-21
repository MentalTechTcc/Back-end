from domain.entities.DicaSaude import DicaSaude
from sqlalchemy.orm import Session
from typing import Protocol, runtime_checkable, NoReturn



@runtime_checkable
class DicaSaudeRepositoryBaseModel(Protocol):

    def save(self, dicaSaudeSent: DicaSaude) -> DicaSaude:
        '''Função para salvar um objeto assistente na DB'''
        ...

    def update(self, dicaSaudeSent: DicaSaude) -> NoReturn:
        """Funçãop para atualizar um DicaSaude, assume que o DicaSaude já existe."""
        ...

    def delete_by_id(self, dicaSaude_id: int)-> NoReturn:
        '''Função para apagar um DicaSaude do banco pelo id'''
        ...

    def find_all(self, database: Session) -> list[DicaSaude]:
        '''Função para fazer uma query de todas as dicaSaudes do DB'''
        ...
    
    def find_by_id(self, dicaSaude_id: int) -> DicaSaude | None:
        """Faz uma busca pelo id e retorna os dados do DicaSaude caso existe"""
        ...
