from domain.entities.Especialidade import Especialidade
from sqlalchemy.orm import Session
from typing import Protocol, runtime_checkable, NoReturn

@runtime_checkable
class EspecialidadeRepositoryBaseModel(Protocol):

    def save(self, especialidadeSent: Especialidade) -> Especialidade:
        '''Função para salvar um objeto assistente na DB'''
        ...

    def update(self, especialidadeSent: Especialidade) -> NoReturn:
        """Funçãop para atualizar um especialidade, assume que o especialidade já existe."""
        ...

    def delete_by_id(self, especialidade_id: int)-> NoReturn:
        '''Função para apagar um especialidade do banco pelo id'''
        ...

    def find_all(self, database: Session) -> list[Especialidade]:
        '''Função para fazer uma query de todas as especialidades do DB'''
        ...
    
    def find_by_id(self, especialidade_id: int) -> Especialidade | None:
        """Faz uma busca pelo id e retorna os dados do especialidade caso existe"""
        ...

    def find_by_cpfProfissional(self, cpfProfissional: str) -> list[Especialidade] | None:
        """Faz uma busca pelo cpf e retorna os dados do especialidade caso existe"""
        ...
