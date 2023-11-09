from sqlalchemy.orm import Session
from domain.entities.Agenda import Agenda
from typing import Callable
from typing import NoReturn
from domain.repositories import AgendaRepositoryBaseModel

class AgendaRepository:

    database: Callable[[], Session]
    def __init__(self, session: Callable[[], Session]):
        self.database = session


    def save(self, agendaSent: Agenda) -> Agenda:
        session = self.database()
        # TODO : verificar se o URM possui isso built in
        session.add(agendaSent)
        session.commit()
        session.expunge_all()
        session.close()
        return agendaSent

    def update(self, agendaSent: Agenda) -> NoReturn:
        session = self.database()
        session.merge(agendaSent)
        session.commit()
        session.expunge_all()
        session.close()

    def find_all(self) -> list[Agenda]:
        '''Função para fazer uma query de todas as SocialWorker da DB'''
        session = self.database()
        res = session.query(Agenda).all()
        session.close()
        return res

    def delete_by_id(self, agenda_id: int) -> NoReturn:
        """Função para deletar um profissional do DB, caso exista"""
        session = self.database()
        pessoa_session = session.query(Agenda).filter(Agenda.idAgenda == agenda_id).first()

        if pessoa_session is not None:
            session.delete(pessoa_session)
            session.commit()

        session.close()

    def find_by_id(self, agenda_id: int) -> Agenda | None:
        """Faz uma busca pelo id no banco e retorna o objeto"""
        session = self.database()
        session.close()
        return session.query(Agenda).filter(Agenda.idAgenda == agenda_id).first()
    
    def find_by_cpf(self, cpfProfissional: str) -> list[Agenda]| None:
        session = self.database()
        session.close()
        return session.query(Agenda).filter(Agenda.cpfProfissional == cpfProfissional).all()
    
    

assert isinstance(AgendaRepository(
    {}), AgendaRepositoryBaseModel.AgendaRepositoryBaseModel)
