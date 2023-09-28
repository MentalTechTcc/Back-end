from domain.entities.Especialidade import ProfissionalPossuiEspecialidade
from domain.repositories.ProfissionalPossuiEspecialidadeRepositoryBaseModel import ProfissionalPossuiEspecialidadeBaseModel


class ProfissionalPossuiEspecialidadeUseCase():
    __profissionalPossuiEspecialidade__: ProfissionalPossuiEspecialidadeBaseModel
    

    def __init__(
        self,
        profissionalPossuiEspecialidadeRepository: ProfissionalPossuiEspecialidadeBaseModel
    ):
        self.__profissionalPossuiEspecialidade__ = profissionalPossuiEspecialidadeRepository

    def save(self, profissionalPossuiEspecialidadeSent: ProfissionalPossuiEspecialidade) -> ProfissionalPossuiEspecialidade:

        return self.__profissionalPossuiEspecialidade__.save(profissionalPossuiEspecialidadeSent=profissionalPossuiEspecialidadeSent)

    def delete(self, cpf: str, idEspecialidade: int) -> None:
        return self.__profissionalPossuiEspecialidade__.delete(cpf=cpf, idEspecialidade= idEspecialidade)


    def find_by_cpfProfissional(self, cpf : str) -> ProfissionalPossuiEspecialidade | None:
        return self.__profissionalPossuiEspecialidade__.find_by_cpfProfissional(cpf=cpf)
    



