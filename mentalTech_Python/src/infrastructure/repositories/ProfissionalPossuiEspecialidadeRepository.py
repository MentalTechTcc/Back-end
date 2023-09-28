from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from typing import Callable
from domain.entities.Especialidade import ProfissionalPossuiEspecialidade

class ProfissionalPossuiEspecialidadeRepository:
    database: Callable[[], Session]
    def __init__(self, session: Callable[[], Session]):
        self.database = session
      

    def save(self,profissionalPossuiEspecialidadeSent: ProfissionalPossuiEspecialidade) -> ProfissionalPossuiEspecialidade:
        session = self.database()
        # TODO : verificar se o URM possui isso built in
        session.add(profissionalPossuiEspecialidadeSent)
        session.commit()
        session.expunge_all()
        session.close()
        return profissionalPossuiEspecialidadeSent

    def delete(self, cpf: str, idEspecialidade: int):
            try:
                session = self.database()
                session.query(ProfissionalPossuiEspecialidade).filter(
                    ProfissionalPossuiEspecialidade.cpfProfissional == cpf,
                    ProfissionalPossuiEspecialidade.idEspecialidade == idEspecialidade
                ).delete()
                session.commit()
                session.close()
            except Exception as e:
                session.rollback()
                raise e

        
    def find_by_cpfProfissional(self, cpf: str) -> ProfissionalPossuiEspecialidade | None:
        """Faz uma busca pelo id no banco e retorna o objeto"""
        session = self.database()
        resultado = session.query(ProfissionalPossuiEspecialidade).filter(ProfissionalPossuiEspecialidade.cpfProfissional==cpf).all()
        session.close()
        return resultado

    
