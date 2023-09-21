from domain.entities.Avaliacao import Avaliacao
from sqlalchemy.orm import Session
from typing import Protocol, runtime_checkable, NoReturn



@runtime_checkable
class AvaliacaoRepositoryBaseModel(Protocol):

    def save(self, avaliacaoSent: Avaliacao) -> Avaliacao:
        '''Função para salvar um objeto assistente na DB'''
        ...

    def update(self, avaliacaoSent: Avaliacao) -> NoReturn:
        """Função para atualizar uma Avaliacao, assume que o Avaliacao já existe."""
        ...

    def delete_by_id(self, avaliacao_id: int)-> NoReturn:
        '''Função para apagar uma Avaliacao do banco pelo id'''
        ...

    def find_all(self, database: Session) -> list[Avaliacao]:
        '''Função para fazer uma query de todas as avaliacoes do DB'''
        ...
    
    def find_by_id(self, avaliacao_id: int) -> Avaliacao | None:
        """Faz uma busca pelo id e retorna os dados da Avaliacao caso exista"""
        ...
