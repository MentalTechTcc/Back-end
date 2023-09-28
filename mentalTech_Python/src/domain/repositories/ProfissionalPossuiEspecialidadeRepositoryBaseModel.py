from domain.entities.Especialidade import ProfissionalPossuiEspecialidade
from sqlalchemy.orm import Session
from typing import Protocol, runtime_checkable, NoReturn

@runtime_checkable
class ProfissionalPossuiEspecialidadeBaseModel(Protocol):

    def save(self, profissionalPossuiEspecialidadeSent: ProfissionalPossuiEspecialidade) -> ProfissionalPossuiEspecialidade:
        '''Função para salvar um objeto assistente na DB'''
        ...

    def delete(self, cpf: str, idEspecialidade: int)-> NoReturn:
        '''Função para apagar um PessoaPossuiEndereco do banco pelo id'''
        ...
    
    def find_by_cpfProfissional(self, cpf: str) -> ProfissionalPossuiEspecialidade:
        """Faz uma busca pelo id e retorna os dados do PessoaPossuiEspecialidade caso existe"""
        ...
