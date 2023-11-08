from domain.entities.Endereco import Endereco, EnderecoResponse, EnderecoBase, EnderecoRequestId
from domain.repositories.EnderecoRepositoryBaseModel import EnderecoRepositoryBaseModel
from .ValidacaoCamposUseCase import ValidacaoCamposUseCase
from security import verify_password
from typing import NoReturn
from fastapi import HTTPException, status

class EnderecoUseCase():
    __enderecoRepository__: EnderecoRepositoryBaseModel
    
    def __init__(
        self,
        enderecoRepository: EnderecoRepositoryBaseModel
    ):
        self.__enderecoRepository__ = enderecoRepository

    def save(self, enderecoSent: Endereco) -> Endereco:  # Corrigido o tipo de entrada aqui
        return self.__enderecoRepository__.save(enderecoSent=enderecoSent)

    def delete_by_id(self, endereco_id: int) -> None:
        return self.__enderecoRepository__.delete_by_id(endereco_id=endereco_id)

    def find_all(self) -> list[EnderecoResponse]:
        endereco_db = self.__enderecoRepository__.find_all()
        enderecos = []
        for endereco_db in endereco_db:
            endereco = EnderecoResponse(
                idEndereco=  endereco_db.idEndereco,
                cep= endereco_db.cep,
                estado= endereco_db.estado,
                cidade= endereco_db.cidade,
                bairro= endereco_db.bairro,
                numero= endereco_db.numero,
                complemento= endereco_db.complemento
            )
            enderecos.append(endereco)
        return enderecos

    def find_by_id(self, endereco_id : int) -> EnderecoBase | None:
        return self.__enderecoRepository__.find_by_id(endereco_id=endereco_id)

    def update(self, enderecoSent: EnderecoRequestId) -> NoReturn:
        """Sobrescreve os dados de endereco, assume que ele já exista"""
        self.__enderecoRepository__.update(Endereco(**enderecoSent.__dict__))


    def valida_endereco_create(self, endereco: Endereco) -> dict:

        fieldInfoDict = {}
        fieldInfoDict["bairro"] = vars(ValidacaoCamposUseCase.bairroValidation(
            endereco.bairro))
        fieldInfoDict["cep"] = vars(ValidacaoCamposUseCase.cepValidation(
            endereco.cep))
        fieldInfoDict["cidade"] = vars(ValidacaoCamposUseCase.cidadeValidation(
        endereco.cidade))
        completeStatus = True
        for key in fieldInfoDict:
            if fieldInfoDict[key]['status'] == False:
                completeStatus = False
                break
        fieldInfoDict['completeStatus'] = completeStatus

        return fieldInfoDict
