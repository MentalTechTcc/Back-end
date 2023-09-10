from domain.entities.Pessoa import Pessoa, PessoaResponse, PessoaBase, PessoaRequestId
from domain.repositories.PessoaRepositoryBaseModel import PessoaRepositoryBaseModel
from typing import NoReturn

class PessoaUseCase():
    __pessoaRepository__: PessoaRepositoryBaseModel

    def __init__(
        self,
        pessoaRepository: PessoaRepositoryBaseModel
    ):
        self.__pessoaRepository__ = pessoaRepository

    def save(self, pessoaSent: Pessoa) -> Pessoa:
        '''Função para salvar um objeto pessoa na DB, utilizada também como update'''
        return self.__pessoaRepository__.save(pessoaSent=pessoaSent)

    def delete_by_id(self, pessoa_id: int) -> None:
        return self.__pessoaRepository__.delete_by_id(pessoa_id=pessoa_id)


    def find_all(self) -> list[PessoaResponse]:
        pessoas_db = self.__pessoaRepository__.find_all()
        pessoas = []
        for pessoa_db in pessoas_db:
            pessoa = PessoaResponse(
                nome=pessoa_db.nome,
                email=pessoa_db.email,
                telefone=pessoa_db.telefone,
                dataNascimento=pessoa_db.dataNascimento,
                sexo=pessoa_db.sexo
            )
            pessoas.append(pessoa)
        return pessoas

    def find_by_id(self, pessoa_id : int) -> PessoaBase | None:
        return self.__pessoaRepository__.find_by_id(pessoa_id=pessoa_id)

    def update(self, pessoaSent: PessoaRequestId) -> NoReturn:
        """Sobrescreve os dados de pessoa, assume que ele já exista"""
        self.__pessoaRepository__.update(Pessoa(**pessoaSent.__dict__))
