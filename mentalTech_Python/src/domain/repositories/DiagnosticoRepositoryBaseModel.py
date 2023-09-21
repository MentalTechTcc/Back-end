from domain.entities.Diagnostico import Diagnostico
from sqlalchemy.orm import Session
from typing import Protocol, runtime_checkable, NoReturn



@runtime_checkable
class DiagnosticoRepositoryBaseModel(Protocol):

    def save(self, diagnosticoSent: Diagnostico) -> Diagnostico:
        '''Função para salvar um objeto assistente na DB'''
        ...

    def update(self, diagnosticoSent: Diagnostico) -> NoReturn:
        """Função para atualizar um Diagnostico, assume que o Diagnostico já existe."""
        ...

    def delete_by_id(self, diagnostico_id: int)-> NoReturn:
        '''Função para apagar um Diagnostico do banco pelo id'''
        ...

    def find_all(self, database: Session) -> list[Diagnostico]:
        '''Função para fazer uma query de todas os diagnosticos do DB'''
        ...
    
    def find_by_id(self, diagnostico_id: int) -> Diagnostico | None:
        """Faz uma busca pelo id e retorna os dados do Diagnostico caso existe"""
        ...
