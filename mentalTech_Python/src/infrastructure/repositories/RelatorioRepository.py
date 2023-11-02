from sqlalchemy.orm import Session
from domain.entities.Relatorio import Relatorio
from domain.entities.Agenda import Agenda
from domain.entities.Consulta import Consulta
from domain.entities.Profissional import Profissional
from typing import Callable
from typing import NoReturn
from src.domain.repositories import RelatorioRepositoryBaseModel

class RelatorioRepository:

    database: Callable[[], Session]
    def __init__(self, session: Callable[[], Session]):
        self.database = session


    def save(self, relatorioSent: Relatorio) -> Relatorio:
        session = self.database()
        # TODO : verificar se o URM possui isso built in
        session.add(relatorioSent)
        session.commit()
        session.expunge_all()
        session.close()
        return relatorioSent

    def update(self, relatorioSent: Relatorio) -> NoReturn:
        session = self.database()
        session.merge(relatorioSent)
        session.commit()
        session.expunge_all()
        session.close()

    def find_all(self) -> list[Relatorio]:
        '''Função para fazer uma query de todos os relatorios do DB'''
        session = self.database()
        res = session.query(Relatorio).all()
        session.close()
        return res

    def delete_by_id(self, relatorio_id: int) -> NoReturn:
        """Função para deletar um relatorio do DB, caso exista"""
        session = self.database()
        relatorio_session = session.query(Relatorio).filter(Relatorio.idRelatorio == relatorio_id).first()

        if relatorio_session is not None:
            session.delete(relatorio_session)
            session.commit()

        session.close()

    def find_by_id(self, relatorio_id: int) -> Relatorio | None:
        """Faz uma busca pelo id no banco e retorna o objeto"""
        session = self.database()
        session.close()
        return session.query(Relatorio).filter(Relatorio.idRelatorio == relatorio_id).first()

    def find_by_cpfProfissional(self, cpfProfissional:str) ->  list[Relatorio]|None: #apenas os que permitiram compartilhar conhecimento
        session = self.database()
        session.close()
        return session.query(Relatorio) \
            .join(Consulta, Consulta.idConsulta == Relatorio.idConsulta) \
            .join(Agenda, Agenda.idAgenda == Consulta.idAgenda) \
            .join(Profissional, Profissional.cpf == Agenda.cpfProfissional) \
            .filter(Profissional.cpf == cpfProfissional, Consulta.permiteCompartilharConhecimento==True) \
            .all()
    
    def find_by_cpfProfissional_completo(self, cpfProfissional:str) ->  list[Relatorio]|None:
        session = self.database()
        session.close()
        return session.query(Relatorio) \
            .join(Consulta, Consulta.idConsulta == Relatorio.idConsulta) \
            .join(Agenda, Agenda.idAgenda == Consulta.idAgenda) \
            .join(Profissional, Profissional.cpf == Agenda.cpfProfissional) \
            .filter(Profissional.cpf == cpfProfissional) \
            .all()
    

assert isinstance(RelatorioRepository(
    {}), RelatorioRepositoryBaseModel.RelatorioRepositoryBaseModel)
