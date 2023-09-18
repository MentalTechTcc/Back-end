from sqlalchemy.orm import Session
from domain.entities.TematicasPrincipais import TematicasPrincipais
from typing import Callable
from typing import NoReturn
from src.domain.repositories import TematicasPrincipaisRepositoryBaseModel

class TematicasPrincipaisRepository:

    database: Callable[[], Session]
    def __init__(self, session: Callable[[], Session]):
        self.database = session


    def save(self, tematicasPrincipaisSent: TematicasPrincipais) -> TematicasPrincipais:
        session = self.database()
        # TODO : verificar se o URM possui isso built in
        session.add(tematicasPrincipaisSent)
        session.commit()
        session.expunge_all()
        session.close()
        return tematicasPrincipaisSent

    def update(self, tematicasPrincipaisSent: TematicasPrincipais) -> NoReturn:
        session = self.database()
        session.merge(tematicasPrincipaisSent)
        session.commit()
        session.expunge_all()
        session.close()

    def find_all(self) -> list[TematicasPrincipais]:
        '''Função para fazer uma query de todos os tematicasPrincipaiss do DB'''
        session = self.database()
        res = session.query(TematicasPrincipais).all()
        session.close()
        return res

    def delete_by_id(self, tematicasPrincipais_id: int) -> NoReturn:
        """Função para deletar um tematicasPrincipais do DB, caso exista"""
        session = self.database()
        tematicasPrincipais_session = session.query(TematicasPrincipais).filter(TematicasPrincipais.idTematicasPrincipais == tematicasPrincipais_id).first()

        if tematicasPrincipais_session is not None:
            session.delete(tematicasPrincipais_session)
            session.commit()

        session.close()

    def find_by_id(self, tematicasPrincipais_id: int) -> TematicasPrincipais | None:
        """Faz uma busca pelo id no banco e retorna o objeto"""
        session = self.database()
        session.close()
        return session.query(TematicasPrincipais).filter(TematicasPrincipais.idTematicasPrincipais == tematicasPrincipais_id).first()
    
    
    
    

assert isinstance(TematicasPrincipaisRepository(
    {}), TematicasPrincipaisRepositoryBaseModel.TematicasPrincipaisRepositoryBaseModel)
