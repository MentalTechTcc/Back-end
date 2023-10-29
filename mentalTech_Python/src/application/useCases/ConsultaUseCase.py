from domain.entities.Consulta import Consulta, ConsultaResponse, ConsultaBase, ConsultaRequestId
from domain.repositories.ConsultaRepositoryBaseModel import ConsultaRepositoryBaseModel
from .ValidacaoCamposUseCase import ValidacaoCamposUseCase
from security import verify_password
from typing import NoReturn
from fastapi import HTTPException, status

class ConsultaUseCase():
    __consultaRepository__: ConsultaRepositoryBaseModel
    

    def __init__(
        self,
        consultaRepository: ConsultaRepositoryBaseModel
    ):
        self.__consultaRepository__ = consultaRepository

    def save(self, consultaSent: Consulta) -> Consulta:

        return self.__consultaRepository__.save(consultaSent=consultaSent)

    def delete_by_id(self, consulta_id: int) -> None:
        return self.__consultaRepository__.delete_by_id(consulta_id=consulta_id)


    def find_all(self) -> list[ConsultaResponse]:
        consulta_db = self.__consultaRepository__.find_all()
        consultas = []
        for consulta_db in consulta_db:
            consulta = ConsultaResponse(
                idConsulta =  consulta_db.idConsulta,
                valor=consulta_db.valor,
                idPessoa = consulta_db.idPessoa,
                idAgenda=consulta_db.idAgenda,
                permiteCompartilharConhecimento=consulta_db.permiteCompartilharConhecimento,
                ocorreu=consulta_db.ocorreu
            )
            consultas.append(consulta)
        return consultas

    def find_by_id(self, consulta_id : int) -> ConsultaBase | None:
        return self.__consultaRepository__.find_by_id(consulta_id=consulta_id)
    

    def update(self, consultaSent: ConsultaRequestId) -> NoReturn:
        """Sobrescreve os dados de consulta, assume que ele já exista"""
        self.__consultaRepository__.update(Consulta(**consultaSent.__dict__))

    def find_by_idPessoa(self, pessoa_id : int) -> list[ConsultaResponse] | None:
        return self.__consultaRepository__.find_by_idPessoa(pessoa_id=pessoa_id)


    def valida_consulta_create(self, consulta: Consulta) -> dict:

        fieldInfoDict = {}
        fieldInfoDict["valor"] = vars(ValidacaoCamposUseCase.valorValidation(
            consulta.valor))
        completeStatus = True
        for key in fieldInfoDict:
            if fieldInfoDict[key]['status'] == False:
                completeStatus = False
                break
        fieldInfoDict['completeStatus'] = completeStatus

        return fieldInfoDict
