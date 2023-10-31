from sqlalchemy.orm import Session
from domain.entities.Consulta import Consulta
from typing import Callable
from typing import NoReturn
from src.domain.repositories import ConsultaRepositoryBaseModel

class ConsultaRepository:

    database: Callable[[], Session]
    def __init__(self, session: Callable[[], Session]):
        self.database = session


    def save(self, consultaSent: Consulta) -> Consulta:
        session = self.database()
        # TODO : verificar se o URM possui isso built in
        session.add(consultaSent)
        session.commit()
        session.expunge_all()
        session.close()
        return consultaSent

    def update(self, consultaSent: Consulta) -> NoReturn:
        session = self.database()
        session.merge(consultaSent)
        session.commit()
        session.expunge_all()
        session.close()

    def find_all(self) -> list[Consulta]:
        '''Função para fazer uma query de todas as SocialWorker da DB'''
        session = self.database()
        res = session.query(Consulta).all()
        session.close()
        return res

    def delete_by_id(self, consulta_id: int) -> NoReturn:
        """Função para deletar um profissional do DB, caso exista"""
        session = self.database()
        consulta_session = session.query(Consulta).filter(Consulta.idConsulta == consulta_id).first()

        if consulta_session is not None:
            session.delete(consulta_session)
            session.commit()

        session.close()

    def delete_by_idAgenda(self, agenda_id: int) -> NoReturn:
        """Função para deletar um profissional do DB, caso exista"""
        session = self.database()
        consulta_session = session.query(Consulta).filter(Consulta.idAgenda == agenda_id).first()

        if consulta_session is not None:
            session.delete(consulta_session)
            session.commit()

        session.close()

    def find_by_id(self, consulta_id: int) -> Consulta | None:
        """Faz uma busca pelo id no banco e retorna o objeto"""
        session = self.database()
        session.close()
        return session.query(Consulta).filter(Consulta.idConsulta == consulta_id).first()
    
    def find_by_idPessoa(self, pessoa_id: int) -> list[Consulta] | None:
        session = self.database()
        session.close()
        return session.query(Consulta).filter(Consulta.idPessoa == pessoa_id).all()
    
    
    
    

assert isinstance(ConsultaRepository(
    {}), ConsultaRepositoryBaseModel.ConsultaRepositoryBaseModel)
