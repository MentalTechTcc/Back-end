from sqlalchemy.orm import Session
from domain.entities.Profissional import Profissional
from typing import Callable
from typing import NoReturn
from src.domain.repositories import ProfissionalRepositoryBaseModel

class ProfissionalRepository:

    database: Callable[[], Session]
    def __init__(self, session: Callable[[], Session]):
        self.database = session


    def save(self, profissionalSent: Profissional) -> Profissional:
        session = self.database()
        # TODO : verificar se o URM possui isso built in
        session.add(profissionalSent)
        session.commit()
        session.expunge_all()
        session.close()
        return profissionalSent

    def update(self, profissionalSent: Profissional) -> NoReturn:
        session = self.database()
        session.merge(profissionalSent)
        session.commit()
        session.expunge_all()
        session.close()

    def find_all(self) -> list[Profissional]:
        '''Função para fazer uma query de todas as SocialWorker da DB'''
        session = self.database()
        res = session.query(Profissional).all()
        session.close()
        return res

    def delete_by_id(self, profissional_id: int) -> NoReturn:
        """Função para deletar um profissional do DB, caso exista"""
        session = self.database()
        pessoa_session = session.query(Profissional).filter(Profissional.idPessoa == profissional_id).first()

        if pessoa_session is not None:
            session.delete(pessoa_session)
            session.commit()

        session.close()

    def find_by_id(self, profissional_id: int) -> Profissional | None:
        """Faz uma busca pelo id no banco e retorna o objeto"""
        session = self.database()
        session.close()
        return session.query(Profissional).filter(Profissional.idPessoa == profissional_id).first()
    
    def find_by_email(self, email: str) -> Profissional | None:
        """Faz uma busca pelo email no banco e retorna o objeto"""
        session = self.database()
        return session.query(Profissional).filter(Profissional.email == email).first()
    
    

assert isinstance(ProfissionalRepository(
    {}), ProfissionalRepositoryBaseModel.ProfissionalRepositoryBaseModel)
