from sqlalchemy.orm import Session
from domain.entities.Pessoa import Pessoa
from typing import Callable
from domain.repositories import PessoaRepositoryBaseModel
from typing import NoReturn

class PessoaRepository:

    database: Callable[[], Session]
    def __init__(self, session: Callable[[], Session]):
        self.database = session


    def save(self, pessoaSent: Pessoa) -> Pessoa:
        session = self.database()
        # TODO : verificar se o URM possui isso built in
        session.add(pessoaSent)
        session.commit()
        session.expunge_all()
        session.close()
        return pessoaSent

    def update(self, pessoaSent: Pessoa) -> NoReturn:
        session = self.database()
        session.merge(pessoaSent)
        session.commit()
        session.expunge_all()
        session.close()

    def find_all(self) -> list[Pessoa]:
        '''Função para fazer uma query de todas as SocialWorker da DB'''
        session = self.database()
        res = session.query(Pessoa).all()
        session.close()
        return res

    def delete_by_id(self, pessoa_id: int) -> NoReturn:
        """Função para deletar um Pessoa do DB, caso exista"""
        session = self.database()
        pessoa_session = session.query(Pessoa).filter(Pessoa.idPessoa == pessoa_id).first()

        if pessoa_session is not None:
            session.delete(pessoa_session)
            session.commit()

        session.close()

    def find_by_id(self, pessoa_id: int) -> Pessoa | None:
        """Faz uma busca pelo id no banco e retorna o objeto"""
        session = self.database()
        session.close()
        return session.query(Pessoa).filter(Pessoa.idPessoa == pessoa_id).first()

assert isinstance(PessoaRepository(
    {}), PessoaRepositoryBaseModel.PessoaRepositoryBaseModel)
