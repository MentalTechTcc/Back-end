from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from typing import Callable
from domain.entities.Endereco import ProfissionalPossuiEndereco

class ProfissionalPossuiEnderecoRepository:
    database: Callable[[], Session]
    def __init__(self, session: Callable[[], Session]):
        self.database = session
      

    def save(self,profissionalPossuiEnderecoSent: ProfissionalPossuiEndereco) -> ProfissionalPossuiEndereco:
        session = self.database()
        # TODO : verificar se o URM possui isso built in
        session.add(profissionalPossuiEnderecoSent)
        session.commit()
        session.expunge_all()
        session.close()
        return profissionalPossuiEnderecoSent

    def delete(self, cpf: str, enderecoId: int):
            try:
                session = self.database()
                session.query(ProfissionalPossuiEndereco).filter(
                    ProfissionalPossuiEndereco.cpfProfissional == cpf,
                    ProfissionalPossuiEndereco.idEndereco == enderecoId
                ).delete()
                session.commit()
                session.close()
            except Exception as e:
                session.rollback()
                raise e

        
    def find_by_cpfProfissional(self, cpf: str) -> ProfissionalPossuiEndereco | None:
        """Faz uma busca pelo id no banco e retorna o objeto"""
        session = self.database()
        resultado = session.query(ProfissionalPossuiEndereco).filter(ProfissionalPossuiEndereco.cpfProfissional==cpf).all()
        session.close()
        return resultado

    
