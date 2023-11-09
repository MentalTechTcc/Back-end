from sqlalchemy.orm import Session
from domain.entities.Consulta import Consulta
from domain.entities.Agenda import Agenda
from typing import Callable
from typing import NoReturn
from domain.repositories import ConsultaRepositoryBaseModel
from datetime import datetime
from fastapi import HTTPException

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
    
    
    def find_by_idAgenda(self, pessoa_id: int) -> list[Consulta] | None:
        session = self.database()
        session.close()
        return session.query(Consulta).filter(Consulta.idAgenda == pessoa_id).all()
    

    def delete_by_idAgenda(self, agenda_id: int) -> NoReturn:
        session = self.database()
        consulta_session = session.query(Consulta).filter(Consulta.idAgenda == agenda_id).first()

        if consulta_session is not None:
            agenda = session.query(Agenda).filter(Agenda.idAgenda == agenda_id).first()
            if agenda is None:
                session.close()
                raise HTTPException(status_code=404, detail="Agenda não encontrada")

            current_date = datetime.now().date()

            if agenda.data > current_date:
                session.delete(consulta_session)
                session.commit()
            else:
                session.close()
                raise HTTPException(status_code=400, detail="Não é possível excluir consulta em uma agenda passada")

        session.close()

    
    

assert isinstance(ConsultaRepository(
    {}), ConsultaRepositoryBaseModel.ConsultaRepositoryBaseModel)
