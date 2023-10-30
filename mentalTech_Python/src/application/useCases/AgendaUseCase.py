from domain.entities.Agenda import Agenda, AgendaResponse, AgendaBase, AgendaRequestId
from domain.repositories.AgendaRepositoryBaseModel import AgendaRepositoryBaseModel
from .ValidacaoCamposUseCase import ValidacaoCamposUseCase
from security import verify_password
from typing import NoReturn
from fastapi import HTTPException, status

class AgendaUseCase():
    __agendaRepository__: AgendaRepositoryBaseModel
    

    def __init__(
        self,
        agendaRepository: AgendaRepositoryBaseModel
    ):
        self.__agendaRepository__ = agendaRepository

    def save(self, agendaSent: Agenda) -> Agenda:

        return self.__agendaRepository__.save(agendaSent=agendaSent)

    def delete_by_id(self, agenda_id: int) -> None:
        return self.__agendaRepository__.delete_by_id(agenda_id=agenda_id)


    def find_all(self) -> list[AgendaResponse]:
        agendas_db = self.__agendaRepository__.find_all()
        profissionais = []
        for agenda_db in agendas_db:
            agenda = AgendaResponse(
                idAgenda =  agenda_db.idAgenda,
                data=agenda_db.data,
                hora = agenda_db.hora,
                duracao=agenda_db.duracao,
                cpfProfissional=agenda_db.cpfProfissional,
                modalidadeAtendimento=agenda_db.modalidadeAtendimento,
                ocupado= agenda_db.ocupado,
                valorProposto= agenda_db.valorProposto,
                linkPagamento=agenda_db.linkPagamento
            )
            profissionais.append(agenda)
        return profissionais

    def find_by_id(self, agenda_id : int) -> AgendaBase | None:
        return self.__agendaRepository__.find_by_id(agenda_id=agenda_id)
    
    def find_by_cpf(self, cpfProfissional : int) -> list[AgendaResponse] | None:
        return self.__agendaRepository__.find_by_cpf(cpfProfissional=cpfProfissional)
    

    def update(self, agendaSent: AgendaRequestId) -> NoReturn:
        """Sobrescreve os dados de agenda, assume que ele já exista"""
        self.__agendaRepository__.update(Agenda(**agendaSent.__dict__))

    def valida_agenda_create(self, agenda: Agenda) -> dict:

        fieldInfoDict = {}
        fieldInfoDict["cpf"] = vars(ValidacaoCamposUseCase.cpfValidation(
            agenda.cpfProfissional))
        completeStatus = True
        for key in fieldInfoDict:
            if fieldInfoDict[key]['status'] == False:
                completeStatus = False
                break
        fieldInfoDict['completeStatus'] = completeStatus

        return fieldInfoDict