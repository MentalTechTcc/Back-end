from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from typing import Callable
from domain.entities.TematicasPrincipais import ProfissionalTrataTematicas

class ProfissionalTrataTematicasRepository:
    database: Callable[[], Session]
    def __init__(self, session: Callable[[], Session]):
        self.database = session
      

    def save(self,profissionalTrataTematicasSent: ProfissionalTrataTematicas) -> ProfissionalTrataTematicas:
        session = self.database()
        # TODO : verificar se o URM possui isso built in
        session.add(profissionalTrataTematicasSent)
        session.commit()
        session.expunge_all()
        session.close()
        return profissionalTrataTematicasSent

    def delete(self, cpf: str, idTematicasPrincipais: int):
            try:
                session = self.database()
                session.query(ProfissionalTrataTematicas).filter(
                    ProfissionalTrataTematicas.cpfProfissional == cpf,
                    ProfissionalTrataTematicas.idTematicasPrincipais == idTematicasPrincipais
                ).delete()
                session.commit()
                session.close()
            except Exception as e:
                session.rollback()
                raise e

        
    def find_by_cpfProfissional(self, cpf: str) -> ProfissionalTrataTematicas | None:
        """Faz uma busca pelo id no banco e retorna o objeto"""
        session = self.database()
        resultado = session.query(ProfissionalTrataTematicas).filter(ProfissionalTrataTematicas.cpfProfissional==cpf).all()
        session.close()
        return resultado

    
