from domain.entities.Especialidade import Especialidade, EspecialidadeResponse, EspecialidadeBase, EspecialidadeRequestId
from domain.repositories.EspecialidadeRepositoryBaseModel import EspecialidadeRepositoryBaseModel
from security import verify_password
from typing import NoReturn
from fastapi import HTTPException, status

class EspecialidadeUseCase():
    __especialidadeRepository__: EspecialidadeRepositoryBaseModel
    
    def __init__(
        self,
        especialidadeRepository: EspecialidadeRepositoryBaseModel
    ):
        self.__especialidadeRepository__ = especialidadeRepository

    def save(self, especialidadeSent: Especialidade) -> Especialidade:  # Corrigido o tipo de entrada aqui
        return self.__especialidadeRepository__.save(especialidadeSent=especialidadeSent)

    def delete_by_id(self, especialidade_id: int) -> None:
        return self.__especialidadeRepository__.delete_by_id(especialidade_id=especialidade_id)

    def find_all(self) -> list[EspecialidadeResponse]:
        especialidades_db = self.__especialidadeRepository__.find_all()
        especialidades = []
        for especialidade_db in especialidades_db:
            especialidade = EspecialidadeResponse(
                idEspecialidade = especialidade_db.idEspecialidade,
                descricaoEspecialidade = especialidade_db.descricaoEspecialidade
            )
            especialidades.append(especialidade)
        return especialidades

    def find_by_id(self, especialidade_id : int) -> EspecialidadeBase | None:
        return self.__especialidadeRepository__.find_by_id(especialidade_id=especialidade_id)

    def find_by_cpfProfissional(self, cpfProfissional: str) -> list[Especialidade] | None:
        return self.__especialidadeRepository__.find_by_cpfProfissional(cpfProfissional=cpfProfissional)

    def update(self, especialidadeSent: EspecialidadeRequestId) -> NoReturn:
        """Sobrescreve os dados de especialidade, assume que ele já exista"""
        self.__especialidadeRepository__.update(Especialidade(**especialidadeSent.__dict__))
