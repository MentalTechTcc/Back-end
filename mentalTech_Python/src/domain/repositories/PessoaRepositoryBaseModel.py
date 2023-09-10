from domain.entities.Pessoa import Pessoa
from sqlalchemy.orm import Session
from typing import Protocol, runtime_checkable, NoReturn



@runtime_checkable
class PessoaRepositoryBaseModel(Protocol):

    def save(self, pessoaSent: Pessoa) -> Pessoa:
        '''Função para salvar um objeto assistente na DB'''
        ...

    def update(self, pessoaSent: Pessoa) -> NoReturn:
        """Funçãop para atualizar um Pessoa, assume que o Pessoa já existe."""
        ...

    def delete_by_id(self, pessoa_id: int)-> NoReturn:
        '''Função para apagar um Pessoa do banco pelo id'''
        ...

    def find_all(self, database: Session) -> list[Pessoa]:
        '''Função para fazer uma query de todas as pessoas do DB'''
        ...
    
    def find_by_id(self, pessoa_id: int) -> Pessoa | None:
        """Faz uma busca pelo id e retorna os dados do Pessoa caso existe"""
        ...
    def find_by_email(self, email: str) -> Pessoa | None:
        '''Função para fazer uma query por login de um objeto Pessoa na DB'''
        ...