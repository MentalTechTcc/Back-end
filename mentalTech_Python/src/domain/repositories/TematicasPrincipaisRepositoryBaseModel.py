from domain.entities.TematicasPrincipais import TematicasPrincipais
from sqlalchemy.orm import Session
from typing import Protocol, runtime_checkable, NoReturn



@runtime_checkable
class TematicasPrincipaisRepositoryBaseModel(Protocol):

    def save(self, tematicasPrincipaisSent: TematicasPrincipais) -> TematicasPrincipais:
        '''Função para salvar um objeto assistente na DB'''
        ...

    def update(self, tematicasPrincipaisSent: TematicasPrincipais) -> NoReturn:
        """Funçãop para atualizar um TematicasPrincipais, assume que o TematicasPrincipais já existe."""
        ...

    def delete_by_id(self, tematicasPrincipais_id: int)-> NoReturn:
        '''Função para apagar um TematicasPrincipais do banco pelo id'''
        ...

    def find_all(self, database: Session) -> list[TematicasPrincipais]:
        '''Função para fazer uma query de todas as TematicasPrincipaiss do DB'''
        ...
    
    def find_by_id(self, tematicasPrincipais_id: int) -> TematicasPrincipais | None:
        """Faz uma busca pelo id e retorna os dados do TematicasPrincipais caso existe"""
        ...
   