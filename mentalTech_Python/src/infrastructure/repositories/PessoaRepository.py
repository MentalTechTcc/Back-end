from sqlalchemy.orm import Session
from domain.entities.Pessoa import Pessoa
from domain.entities.Agenda import Agenda
from domain.entities.Consulta import Consulta
from domain.entities.Profissional import Profissional
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
    
    def find_by_email(self, email: str) -> Pessoa | None:
        """Faz uma busca pelo email no banco e retorna o objeto"""
        session = self.database()
        return session.query(Pessoa).filter(Pessoa.email == email).first()
    
    def find_by_cpfProfissional(self, cpfProfissional: int) -> list[Pessoa] | None: 
        session = self.database()
        try:
            result = session.query(Pessoa) \
                .join(Consulta, Consulta.idPessoa == Pessoa.idPessoa) \
                .join(Agenda, Agenda.idAgenda == Consulta.idAgenda) \
                .join(Profissional, Profissional.cpf == Agenda.cpfProfissional) \
                .filter(Profissional.cpf == cpfProfissional) \
                .all()
            return result
        finally:
            session.close()
    

assert isinstance(PessoaRepository(
    {}), PessoaRepositoryBaseModel.PessoaRepositoryBaseModel)
