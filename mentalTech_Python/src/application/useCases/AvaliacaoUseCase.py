from domain.entities.Avaliacao import Avaliacao, AvaliacaoResponse, AvaliacaoBase, AvaliacaoRequestId
from domain.repositories.AvaliacaoRepositoryBaseModel import AvaliacaoRepositoryBaseModel
from .ValidacaoCamposUseCase import ValidacaoCamposUseCase
from security import verify_password
from typing import NoReturn
from fastapi import HTTPException, status

class AvaliacaoUseCase():
    __avaliacaoRepository__: AvaliacaoRepositoryBaseModel
    

    def __init__(
        self,
        avaliacaoRepository: AvaliacaoRepositoryBaseModel
    ):
        self.__avaliacaoRepository__ = avaliacaoRepository

    def save(self, avaliacaoSent: Avaliacao) -> Avaliacao:

        return self.__avaliacaoRepository__.save(avaliacaoSent=avaliacaoSent)

    def delete_by_id(self, avaliacao_id: int) -> None:
        return self.__avaliacaoRepository__.delete_by_id(avaliacao_id=avaliacao_id)


    def find_all(self) -> list[AvaliacaoResponse]:
        avaliacao_db = self.__avaliacaoRepository__.find_all()
        avaliacoes = []
        for avaliacao_db in avaliacao_db:
            avaliacao = AvaliacaoResponse(
                idAvaliacao =  avaliacao_db.idAvaliacao,
                cpfProfissional=avaliacao_db.cpfProfissional,
                idPessoa = avaliacao_db.idPessoa,
                notaGeral=avaliacao_db.notaGeral,
                notaPontualidade=avaliacao_db.notaPontualidade,
                notaAtendimento=avaliacao_db.notaAtendimento,
                observacoes =avaliacao_db.observacoes
            )
            avaliacoes.append(avaliacao)
        return avaliacoes

    def find_by_id(self, avaliacao_id : int) -> AvaliacaoBase | None:
        return self.__avaliacaoRepository__.find_by_id(avaliacao_id=avaliacao_id)
    

    def update(self, avaliacaoSent: AvaliacaoRequestId) -> NoReturn:
        """Sobrescreve os dados de avaliacao, assume que ele já exista"""
        self.__avaliacaoRepository__.update(Avaliacao(**avaliacaoSent.__dict__))

    def valida_avaliacao_create(self, avaliacao: Avaliacao) -> dict:

        fieldInfoDict = {}
        fieldInfoDict["cpf"] = vars(ValidacaoCamposUseCase.cpfValidation(
            avaliacao.cpfProfissional))
        fieldInfoDict["notaGeral"] = vars(ValidacaoCamposUseCase.notaValidation(
            avaliacao.notaGeral))
        fieldInfoDict["notaAtendimento"] = vars(ValidacaoCamposUseCase.notaValidation(
            avaliacao.notaAtendimento))
        fieldInfoDict["notaPontualidade"] = vars(ValidacaoCamposUseCase.notaValidation(
            avaliacao.notaPontualidade))
        completeStatus = True
        for key in fieldInfoDict:
            if fieldInfoDict[key]['status'] == False:
                completeStatus = False
                break
        fieldInfoDict['completeStatus'] = completeStatus

        return fieldInfoDict