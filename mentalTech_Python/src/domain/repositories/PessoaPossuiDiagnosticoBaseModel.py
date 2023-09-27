from domain.entities.Diagnostico import PessoaPossuiDiagnostico
from sqlalchemy.orm import Session
from typing import Protocol, runtime_checkable, NoReturn

@runtime_checkable
class pessoaPossuiDiagnosticoRepositoryBaseModel(Protocol):

    def save(self, pessoaPossuiDiagnosticoSent: PessoaPossuiDiagnostico) -> PessoaPossuiDiagnostico:
        '''Função para salvar um objeto assistente na DB'''
        ...

    def delete(self, pessoaId: int, diagnosticoId: int, profissionalCpf: str)-> NoReturn:
        '''Função para apagar um PessoaPossuiDiagnostico do banco pelo id'''
        ...
    
    def find_by_idPessoa(self, pessoa_id: int) -> PessoaPossuiDiagnostico:
        """Faz uma busca pelo id e retorna os dados do PessoaPossuiDiagnostico caso existe"""
        ...
