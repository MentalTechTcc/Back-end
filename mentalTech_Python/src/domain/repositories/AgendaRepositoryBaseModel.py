from domain.entities.Agenda import Agenda
from sqlalchemy.orm import Session
from typing import Protocol, runtime_checkable, NoReturn

@runtime_checkable
class AgendaRepositoryBaseModel(Protocol):

    def save(self, agendaSent: Agenda) -> Agenda:
        '''Função para salvar um objeto assistente na DB'''
        ...

    def update(self, agendaSent: Agenda) -> NoReturn:
        """Funçãop para atualizar um agenda, assume que o agenda já existe."""
        ...

    def delete_by_id(self, agenda_id: int)-> NoReturn:
        '''Função para apagar um agenda do banco pelo id'''
        ...

    def find_all(self, database: Session) -> list[Agenda]:
        '''Função para fazer uma query de todas as agendas do DB'''
        ...
    
    def find_by_id(self, agenda_id: int) -> Agenda | None:
        """Faz uma busca pelo id e retorna os dados do agenda caso existe"""
        ...
    
    def find_by_cpf(self, cpfProfissional: str) -> list[Agenda] | None:
        """Faz uma busca pelo id e retorna os dados do agenda caso existe"""
        ...
