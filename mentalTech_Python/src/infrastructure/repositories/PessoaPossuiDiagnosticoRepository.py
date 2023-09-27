from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from typing import Callable
from domain.entities.Diagnostico import PessoaPossuiDiagnostico

class PessoaPossuiDiagnosticoRepository:
    database: Callable[[], Session]
    def __init__(self, session: Callable[[], Session]):
        self.database = session
      

    def save(self,pessoaPossuiDiagnosticoSent: PessoaPossuiDiagnostico) -> PessoaPossuiDiagnostico:
        session = self.database()
        # TODO : verificar se o URM possui isso built in
        session.add(pessoaPossuiDiagnosticoSent)
        session.commit()
        session.expunge_all()
        session.close()
        return pessoaPossuiDiagnosticoSent

    def delete(self, pessoaId: int, diagnosticoId: int, profissionalCpf: str):
            try:
                session = self.database()
                session.query(PessoaPossuiDiagnostico).filter(
                    PessoaPossuiDiagnostico.idPessoa == pessoaId,
                    PessoaPossuiDiagnostico.idDiagnostico == diagnosticoId,
                    PessoaPossuiDiagnostico.cpfProfissional == profissionalCpf
                ).delete()
                session.commit()
                session.close()
            except Exception as e:
                session.rollback()
                raise e

        
    def find_by_idPessoa(self, pessoa_id: int) -> PessoaPossuiDiagnostico | None:
        """Faz uma busca pelo id no banco e retorna o objeto"""
        session = self.database()
        resultado = session.query(PessoaPossuiDiagnostico).filter(PessoaPossuiDiagnostico.idPessoa == pessoa_id).all()
        session.close()
        return resultado

    
