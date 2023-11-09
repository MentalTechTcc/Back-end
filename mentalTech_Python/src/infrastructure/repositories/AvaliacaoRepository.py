from sqlalchemy.orm import Session
from domain.entities.Avaliacao import Avaliacao
from typing import Callable
from typing import NoReturn
from domain.repositories import AvaliacaoRepositoryBaseModel

class AvaliacaoRepository:

    database: Callable[[], Session]
    def __init__(self, session: Callable[[], Session]):
        self.database = session


    def save(self, avaliacaoSent: Avaliacao) -> Avaliacao:
        session = self.database()
        # TODO : verificar se o URM possui isso built in
        session.add(avaliacaoSent)
        session.commit()
        session.expunge_all()
        session.close()
        return avaliacaoSent

    def update(self, avaliacaoSent: Avaliacao) -> NoReturn:
        session = self.database()
        session.merge(avaliacaoSent)
        session.commit()
        session.expunge_all()
        session.close()

    def find_all(self) -> list[Avaliacao]:
        '''Função para fazer uma query de todas as avaliações do DB'''
        session = self.database()
        res = session.query(Avaliacao).all()
        session.close()
        return res

    def delete_by_id(self, avaliacao_id: int) -> NoReturn:
        """Função para deletar uma avaliação do DB, caso exista"""
        session = self.database()
        avaliacao_session = session.query(Avaliacao).filter(Avaliacao.idAvaliacao == avaliacao_id).first()

        if avaliacao_session is not None:
            session.delete(avaliacao_session)
            session.commit()

        session.close()

    def find_by_id(self, avaliacao_id: int) -> Avaliacao | None:
        """Faz uma busca pelo id no banco e retorna o objeto"""
        session = self.database()
        session.close()
        return session.query(Avaliacao).filter(Avaliacao.idAvaliacao == avaliacao_id).first()
    
    def find_by_cpfProfissional(self, cpfProfissional: str) -> list[Avaliacao] | None:
        session = self.database()
        session.close()
        return session.query(Avaliacao).filter(Avaliacao.cpfProfissional == cpfProfissional).all()
    

assert isinstance(AvaliacaoRepository(
    {}), AvaliacaoRepositoryBaseModel.AvaliacaoRepositoryBaseModel)
