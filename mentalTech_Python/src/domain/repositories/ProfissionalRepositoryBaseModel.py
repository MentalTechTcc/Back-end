from domain.entities.Profissional import Profissional
from sqlalchemy.orm import Session
from typing import Protocol, runtime_checkable, NoReturn



@runtime_checkable
class ProfissionalRepositoryBaseModel(Protocol):

    def save(self, profissionalSent: Profissional) -> Profissional:
        '''Função para salvar um objeto assistente na DB'''
        ...

    def update(self, profissionalSent: Profissional) -> NoReturn:
        """Funçãop para atualizar um Profissional, assume que o Profissional já existe."""
        ...

    def delete_by_id(self, profissional_id: int)-> NoReturn:
        '''Função para apagar um Profissional do banco pelo id'''
        ...

    def find_all(self, database: Session) -> list[Profissional]:
        '''Função para fazer uma query de todas as Profissionals do DB'''
        ...
    
    def find_by_id(self, profissional_id: int) -> Profissional | None:
        """Faz uma busca pelo id e retorna os dados do Profissional caso existe"""
        ...
    def find_by_email(self, email: str) -> Profissional | None:
        '''Função para fazer uma query por login de um objeto Profissional na DB'''
        ...
    def find_by_cpf(self, cpf: str) -> Profissional | None:
        '''Função para fazer uma query por login de um objeto Profissional na DB'''
        ...