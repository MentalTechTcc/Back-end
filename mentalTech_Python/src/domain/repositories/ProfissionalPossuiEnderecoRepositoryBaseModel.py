from domain.entities.Endereco import ProfissionalPossuiEndereco
from sqlalchemy.orm import Session
from typing import Protocol, runtime_checkable, NoReturn

@runtime_checkable
class profissionalPossuiEnderecoRepositoryBaseModel(Protocol):

    def save(self, profissionalPossuiEnderecoSent: ProfissionalPossuiEndereco) -> ProfissionalPossuiEndereco:
        '''Função para salvar um objeto assistente na DB'''
        ...

    def delete(self, cpf: str, enderecoId: int)-> NoReturn:
        '''Função para apagar um PessoaPossuiEndereco do banco pelo id'''
        ...
    
    def find_by_cpfProfissional(self, cpf: str) -> ProfissionalPossuiEndereco:
        """Faz uma busca pelo id e retorna os dados do PessoaPossuiEndereco caso existe"""
        ...
