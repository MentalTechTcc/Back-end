from domain.entities.Endereco import Endereco
from sqlalchemy.orm import Session
from typing import Protocol, runtime_checkable, NoReturn

@runtime_checkable
class EnderecoRepositoryBaseModel(Protocol):

    def save(self, enderecoSent: Endereco) -> Endereco:
        '''Função para salvar um objeto assistente na DB'''
        ...

    def update(self, enderecoSent: Endereco) -> NoReturn:
        """Funçãop para atualizar um endereco, assume que o endereco já existe."""
        ...

    def delete_by_id(self, endereco_id: int)-> NoReturn:
        '''Função para apagar um endereco do banco pelo id'''
        ...

    def find_all(self, database: Session) -> list[Endereco]:
        '''Função para fazer uma query de todas as enderecos do DB'''
        ...
    
    def find_by_id(self, endereco_id: int) -> Endereco | None:
        """Faz uma busca pelo id e retorna os dados do endereco caso existe"""
        ...

    def find_by_cpfProfissional(self, cpfProfissional: str) -> list[Endereco] | None:
        ...
