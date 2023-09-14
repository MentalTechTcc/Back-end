from domain.entities.Relatorio import Relatorio
from sqlalchemy.orm import Session
from typing import Protocol, runtime_checkable, NoReturn



@runtime_checkable
class RelatorioRepositoryBaseModel(Protocol):

    def save(self, relatorioSent: Relatorio) -> Relatorio:
        '''Função para salvar um objeto assistente na DB'''
        ...

    def update(self, relatorioSent: Relatorio) -> NoReturn:
        """Funçãop para atualizar um Relatorio, assume que o Relatorio já existe."""
        ...

    def delete_by_id(self, relatorio_id: int)-> NoReturn:
        '''Função para apagar um Relatorio do banco pelo id'''
        ...

    def find_all(self, database: Session) -> list[Relatorio]:
        '''Função para fazer uma query de todas as Relatorios do DB'''
        ...
    
    def find_by_id(self, relatorio_id: int) -> Relatorio | None:
        """Faz uma busca pelo id e retorna os dados do Relatorio caso existe"""
        ...
   