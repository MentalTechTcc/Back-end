from domain.entities.TematicasPrincipais import ProfissionalTrataTematicas
from sqlalchemy.orm import Session
from typing import Protocol, runtime_checkable, NoReturn

@runtime_checkable
class ProfissionalTrataTematicasBaseModel(Protocol):

    def save(self, profissionalTrataTematicasSent: ProfissionalTrataTematicas) -> ProfissionalTrataTematicas:
        '''Função para salvar um objeto assistente na DB'''
        ...

    def delete(self, cpf: str, idTematicasPrincipais: int)-> NoReturn:
        '''Função para apagar um PessoaPossuiEndereco do banco pelo id'''
        ...
    
    def find_by_cpfProfissional(self, cpf: str) -> ProfissionalTrataTematicas:
        """Faz uma busca pelo id e retorna os dados do PessoaPossuiEspecialidade caso existe"""
        ...
