from domain.entities.Relatorio import Relatorio, RelatorioResponse, RelatorioBase, RelatorioRequestId
from domain.repositories.RelatorioRepositoryBaseModel import RelatorioRepositoryBaseModel
from typing import NoReturn
from .ValidacaoCamposUseCase import ValidacaoCamposUseCase


class RelatorioUseCase():
    __relatorioRepository__: RelatorioRepositoryBaseModel
    

    def __init__(
        self,
        relatorioRepository: RelatorioRepositoryBaseModel
    ):
        self.__relatorioRepository__ = relatorioRepository

    def save(self, relatorioSent: Relatorio) -> Relatorio:

        return self.__relatorioRepository__.save(relatorioSent=relatorioSent)

    def delete_by_id(self, relatorio_id: int) -> None:
        return self.__relatorioRepository__.delete_by_id(relatorio_id=relatorio_id)


    def find_all(self) -> list[RelatorioResponse]:
        relatorio_db = self.__relatorioRepository__.find_all()
        relatorios = []
        for relatorio_db in relatorio_db:
            relatorio = RelatorioResponse(
                idRelatorio =  relatorio_db.idRelatorio,
                idConsulta = relatorio_db.idConsulta,
                descricao=relatorio_db.descricao,
                dataCadastro = relatorio_db.dataCadastro
            )
            relatorios.append(relatorio)
        return relatorios

    def find_by_id(self, relatorio_id : int) -> RelatorioBase | None:
        return self.__relatorioRepository__.find_by_id(relatorio_id=relatorio_id)
    
    def find_by_cpfProfissional(self, cpfProfissional : str) -> list[RelatorioResponse] | None:
        return self.__relatorioRepository__.find_by_cpfProfissional(cpfProfissional=cpfProfissional)

    def find_by_cpfProfissional_completo(self, cpfProfissional : str) -> list[RelatorioResponse] | None:
        return self.__relatorioRepository__.find_by_cpfProfissional(cpfProfissional=cpfProfissional)
    
    def find_by_idPessoa(self, idPessoa:int, cpfProfissional:str) ->  list[Relatorio]|None:
         return self.__relatorioRepository__.find_by_idPessoa(idPessoa=idPessoa, cpfProfissional=cpfProfissional)
    
    def update(self, relatorioSent: RelatorioRequestId) -> NoReturn:
        """Sobrescreve os dados de relatorio, assume que ele já exista"""
        self.__relatorioRepository__.update(Relatorio(**relatorioSent.__dict__))

    def valida_relatorio_create(self, relatorio: Relatorio) -> dict:

        fieldInfoDict = {}
        fieldInfoDict["descricao"] = vars(ValidacaoCamposUseCase.descricaoValidation(
            relatorio.descricao))
        completeStatus = True
        for key in fieldInfoDict:
            if fieldInfoDict[key]['status'] == False:
                completeStatus = False
                break
        fieldInfoDict['completeStatus'] = completeStatus

        return fieldInfoDict
