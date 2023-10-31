from domain.entities.Consulta import Consulta
from sqlalchemy.orm import Session
from typing import Protocol, runtime_checkable, NoReturn



@runtime_checkable
class ConsultaRepositoryBaseModel(Protocol):

    def save(self, consultaSent: Consulta) -> Consulta:
        '''Função para salvar um objeto assistente na DB'''
        ...

    def update(self, consultaSent: Consulta) -> NoReturn:
        """Funçãop para atualizar um Consulta, assume que o Consulta já existe."""
        ...

    def delete_by_id(self, consulta_id: int)-> NoReturn:
        '''Função para apagar um Consulta do banco pelo id'''
        ...
    def delete_by_idAgenda(self, agenda_id: int)-> NoReturn:
        '''Função para apagar um Consulta do banco pelo id'''
        ...

    def find_all(self, database: Session) -> list[Consulta]:
        '''Função para fazer uma query de todas as consultas do DB'''
        ...
    
    def find_by_id(self, consulta_id: int) -> Consulta | None:
        """Faz uma busca pelo id e retorna os dados do Consulta caso existe"""
        ...
    def find_by_idPessoa(self, pessoa_id: int) -> list[Consulta] | None:
        """Faz uma busca pelo id e retorna os dados de consulta caso existe"""
        ...

