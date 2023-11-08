from sqlalchemy.orm import Session
from domain.entities.Endereco import Endereco, ProfissionalPossuiEndereco
from typing import Callable
from typing import NoReturn
from src.domain.repositories import EnderecoRepositoryBaseModel

class EnderecoRepository:

    database: Callable[[], Session]
    def __init__(self, session: Callable[[], Session]):
        self.database = session


    def save(self,enderecoSent: Endereco) -> Endereco:
        session = self.database()
        # TODO : verificar se o URM possui isso built in
        session.add(enderecoSent)
        session.commit()
        session.expunge_all()
        session.close()
        return enderecoSent

    def update(self,enderecoSent: Endereco) -> NoReturn:
        session = self.database()
        session.merge(enderecoSent)
        session.commit()
        session.expunge_all()
        session.close()

    def find_all(self) -> list[Endereco]:
        '''Função para fazer uma query de todas as SocialWorker da DB'''
        session = self.database()
        res = session.query(Endereco).all()
        session.close()
        return res

    def delete_by_id(self,endereco_id: int) -> NoReturn:
        """Função para deletar um profissional do DB, caso exista"""
        session = self.database()
        pessoa_session = session.query(Endereco).filter(Endereco.idEndereco == endereco_id).first()

        if pessoa_session is not None:
            session.delete(pessoa_session)
            session.commit()

        session.close()

    def find_by_id(self, endereco_id: int) -> Endereco | None:
        """Faz uma busca pelo id no banco e retorna o objeto"""
        session = self.database()
        session.close()
        return session.query(Endereco).filter(Endereco.idEndereco == endereco_id).first()
    
    def find_by_cpfProfissional(self, cpfProfissional: str) -> list[Endereco] | None:
        """Faz uma busca pelo cpf no banco e retorna o objeto"""
        session = self.database()
    
        enderecos = session.query(Endereco) \
            .join(ProfissionalPossuiEndereco, ProfissionalPossuiEndereco.idEndereco == Endereco.idEndereco) \
            .filter(ProfissionalPossuiEndereco.cpfProfissional == cpfProfissional) \
            .all()

        session.close()

        return enderecos
    
    
     
assert isinstance(EnderecoRepository(
    {}), EnderecoRepositoryBaseModel.EnderecoRepositoryBaseModel)
