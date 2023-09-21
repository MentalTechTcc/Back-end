from sqlalchemy.orm import Session
from domain.entities.DicaSaude import DicaSaude
from typing import Callable
from typing import NoReturn
from src.domain.repositories import DicaSaudeRepositoryBaseModel

class DicaSaudeRepository:

    database: Callable[[], Session]
    def __init__(self, session: Callable[[], Session]):
        self.database = session


    def save(self, dicaSaudeSent: DicaSaude) -> DicaSaude:
        session = self.database()
        # TODO : verificar se o URM possui isso built in
        session.add(dicaSaudeSent)
        session.commit()
        session.expunge_all()
        session.close()
        return dicaSaudeSent

    def update(self, dicaSaudeSent: DicaSaude) -> NoReturn:
        session = self.database()
        session.merge(dicaSaudeSent)
        session.commit()
        session.expunge_all()
        session.close()

    def find_all(self) -> list[DicaSaude]:
        '''Função para fazer uma query de todas as dicas do DB'''
        session = self.database()
        res = session.query(DicaSaude).all()
        session.close()
        return res

    def delete_by_id(self, dicaSaude_id: int) -> NoReturn:
        """Função para deletar uma dica de saúde do DB, caso exista"""
        session = self.database()
        dicaSaude_session = session.query(DicaSaude).filter(DicaSaude.idDicaSaude == dicaSaude_id).first()

        if dicaSaude_session is not None:
            session.delete(dicaSaude_session)
            session.commit()

        session.close()

    def find_by_id(self, dicaSaude_id: int) -> DicaSaude | None:
        """Faz uma busca pelo id no banco e retorna o objeto"""
        session = self.database()
        session.close()
        return session.query(DicaSaude).filter(DicaSaude.idDicaSaude == dicaSaude_id).first()
    
    
    
    

assert isinstance(DicaSaudeRepository(
    {}), DicaSaudeRepositoryBaseModel.DicaSaudeRepositoryBaseModel)
