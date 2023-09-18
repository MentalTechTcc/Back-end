from domain.entities.TematicasPrincipais import TematicasPrincipais, TematicasPrincipaisResponse, TematicasPrincipaisBase, TematicasPrincipaisRequestId
from domain.repositories.TematicasPrincipaisRepositoryBaseModel import TematicasPrincipaisRepositoryBaseModel
from typing import NoReturn


class TematicasPrincipaisUseCase():
    __tematicasPrincipaisRepository__: TematicasPrincipaisRepositoryBaseModel
    

    def __init__(
        self,
        tematicasPrincipaisRepository: TematicasPrincipaisRepositoryBaseModel
    ):
        self.__tematicasPrincipaisRepository__ = tematicasPrincipaisRepository

    def save(self, tematicasPrincipaisSent: TematicasPrincipais) -> TematicasPrincipais:

        return self.__tematicasPrincipaisRepository__.save(tematicasPrincipaisSent=tematicasPrincipaisSent)

    def delete_by_id(self, tematicasPrincipais_id: int) -> None:
        return self.__tematicasPrincipaisRepository__.delete_by_id(tematicasPrincipais_id=tematicasPrincipais_id)


    def find_all(self) -> list[TematicasPrincipaisResponse]:
        tematicasPrincipais_db = self.__tematicasPrincipaisRepository__.find_all()
        tematicasPrincipaisList = []
        for tematicasPrincipais_db in tematicasPrincipais_db:
            tematicasPrincipais = TematicasPrincipaisResponse(
                idTematicasPrincipais =  tematicasPrincipais_db.idTematicasPrincipais,
                idConsulta = tematicasPrincipais_db.nomeTematica
            )
            tematicasPrincipaisList.append(tematicasPrincipais)
        return tematicasPrincipaisList

    def find_by_id(self, tematicasPrincipais_id : int) -> TematicasPrincipaisBase | None:
        return self.__tematicasPrincipaisRepository__.find_by_id(tematicasPrincipais_id=tematicasPrincipais_id)
    

    def update(self, tematicasPrincipaisSent: TematicasPrincipaisRequestId) -> NoReturn:
        """Sobrescreve os dados de tematicasPrincipais, assume que ele já exista"""
        self.__tematicasPrincipaisRepository__.update(TematicasPrincipais(**tematicasPrincipaisSent.__dict__))
