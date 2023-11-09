from sqlalchemy.orm import Session
from domain.entities.Diagnostico import Diagnostico
from typing import Callable
from typing import NoReturn
from domain.repositories import DiagnosticoRepositoryBaseModel

class DiagnosticoRepository:

    database: Callable[[], Session]
    def __init__(self, session: Callable[[], Session]):
        self.database = session


    def save(self, diagnosticoSent: Diagnostico) -> Diagnostico:
        session = self.database()
        # TODO : verificar se o URM possui isso built in
        session.add(diagnosticoSent)
        session.commit()
        session.expunge_all()
        session.close()
        return diagnosticoSent

    def update(self, diagnosticoSent: Diagnostico) -> NoReturn:
        session = self.database()
        session.merge(diagnosticoSent)
        session.commit()
        session.expunge_all()
        session.close()

    def find_all(self) -> list[Diagnostico]:
        '''Função para fazer uma query de todos os diagnosticos da DB'''
        session = self.database()
        res = session.query(Diagnostico).all()
        session.close()
        return res

    def delete_by_id(self, diagnostico_id: int) -> NoReturn:
        """Função para deletar um diagnóstico do DB, caso exista"""
        session = self.database()
        diagnostico_session = session.query(Diagnostico).filter(Diagnostico.idDiagnostico == diagnostico_id).first()

        if diagnostico_session is not None:
            session.delete(diagnostico_session)
            session.commit()

        session.close()

    def find_by_id(self, diagnostico_id: int) -> Diagnostico | None:
        """Faz uma busca pelo id no banco e retorna o objeto"""
        session = self.database()
        session.close()
        return session.query(Diagnostico).filter(Diagnostico.idDiagnostico == diagnostico_id).first()
    
    
    
    

assert isinstance(DiagnosticoRepository(
    {}), DiagnosticoRepositoryBaseModel.DiagnosticoRepositoryBaseModel)
