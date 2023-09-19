from sqlalchemy.orm import Session
from domain.entities.Especialidade import Especialidade
from typing import Callable
from typing import NoReturn
from src.domain.repositories import EspecialidadeRepositoryBaseModel

class EspecialidadeRepository:

    database: Callable[[], Session]
    def __init__(self, session: Callable[[], Session]):
        self.database = session


    def save(self,especialidadeSent: Especialidade) -> Especialidade:
        session = self.database()
        # TODO : verificar se o URM possui isso built in
        session.add(especialidadeSent)
        session.commit()
        session.expunge_all()
        session.close()
        return especialidadeSent

    def update(self,especialidadeSent: Especialidade) -> NoReturn:
        session = self.database()
        session.merge(especialidadeSent)
        session.commit()
        session.expunge_all()
        session.close()

    def find_all(self) -> list[Especialidade]:
        '''Função para fazer uma query de todas as SocialWorker da DB'''
        session = self.database()
        res = session.query(Especialidade).all()
        session.close()
        return res

    def delete_by_id(self,especialidade_id: int) -> NoReturn:
        """Função para deletar um profissional do DB, caso exista"""
        session = self.database()
        pessoa_session = session.query(Especialidade).filter(Especialidade.idEspecialidade == especialidade_id).first()

        if pessoa_session is not None:
            session.delete(pessoa_session)
            session.commit()

        session.close()

    def find_by_id(self, especialidade_id: int) -> Especialidade | None:
        """Faz uma busca pelo id no banco e retorna o objeto"""
        session = self.database()
        session.close()
        return session.query(Especialidade).filter(Especialidade.idEspecialidade == especialidade_id).first()
    
     
assert isinstance(EspecialidadeRepository(
    {}), EspecialidadeRepositoryBaseModel.EspecialidadeRepositoryBaseModel)
