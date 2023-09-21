from domain.entities.Diagnostico import Diagnostico, DiagnosticoResponse, DiagnosticoBase, DiagnosticoRequestId
from domain.repositories.DiagnosticoRepositoryBaseModel import DiagnosticoRepositoryBaseModel
from security import verify_password
from typing import NoReturn
from fastapi import HTTPException, status

class DiagnosticoUseCase():
    __diagnosticoRepository__: DiagnosticoRepositoryBaseModel
    

    def __init__(
        self,
        diagnosticoRepository: DiagnosticoRepositoryBaseModel
    ):
        self.__diagnosticoRepository__ = diagnosticoRepository

    def save(self, diagnosticoSent: Diagnostico) -> Diagnostico:

        return self.__diagnosticoRepository__.save(diagnosticoSent=diagnosticoSent)

    def delete_by_id(self, diagnostico_id: int) -> None:
        return self.__diagnosticoRepository__.delete_by_id(diagnostico_id=diagnostico_id)


    def find_all(self) -> list[DiagnosticoResponse]:
        diagnostico_db = self.__diagnosticoRepository__.find_all()
        diagnosticos = []
        for diagnostico_db in diagnostico_db:
            diagnostico = DiagnosticoResponse(
                idDiagnostico =  diagnostico_db.idDiagnostico,
                descricaoDiagnostico=diagnostico_db.descricaoDiagnostico
            )
            diagnosticos.append(diagnostico)
        return diagnosticos

    def find_by_id(self, diagnostico_id : int) -> DiagnosticoBase | None:
        return self.__diagnosticoRepository__.find_by_id(diagnostico_id=diagnostico_id)
    

    def update(self, diagnosticoSent: DiagnosticoRequestId) -> NoReturn:
        """Sobrescreve os dados de diagnostico, assume que ele já exista"""
        self.__diagnosticoRepository__.update(Diagnostico(**diagnosticoSent.__dict__))
