from domain.entities.Endereco import ProfissionalPossuiEndereco
from domain.repositories.ProfissionalPossuiEnderecoRepositoryBaseModel import profissionalPossuiEnderecoRepositoryBaseModel


class ProfissionalPossuiEnderecoUseCase():
    __profissionalPossuiEndereco__: profissionalPossuiEnderecoRepositoryBaseModel
    

    def __init__(
        self,
        profissionalPossuiEnderecoRepository: profissionalPossuiEnderecoRepositoryBaseModel
    ):
        self.__profissionalPossuiEndereco__ = profissionalPossuiEnderecoRepository

    def save(self, profissionalPossuiEnderecoSent: ProfissionalPossuiEndereco) -> ProfissionalPossuiEndereco:

        return self.__profissionalPossuiEndereco__.save(profissionalPossuiEnderecoSent=profissionalPossuiEnderecoSent)

    def delete(self, cpf: str, enderecoId: int) -> None:
        return self.__profissionalPossuiEndereco__.delete(cpf=cpf, enderecoId= enderecoId)


    def find_by_cpfProfissional(self, cpf : str) -> ProfissionalPossuiEndereco | None:
        return self.__profissionalPossuiEndereco__.find_by_cpfProfissional(cpf=cpf)
    



