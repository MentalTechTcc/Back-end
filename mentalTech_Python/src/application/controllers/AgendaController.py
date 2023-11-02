from database import engine, Base
from fastapi import APIRouter, status, Response, status, HTTPException
from security import get_password_hash
from domain.entities.Agenda import (AgendaResponse,
                                   AgendaRequest,
                                   Agenda,
                                   AgendaRequestId)
from application.controllers import agendaUseCase

Base.metadata.create_all(bind=engine)


router_agenda = APIRouter(
    prefix="/agenda",
    tags=["agenda"]
)

@router_agenda.post("/", status_code=status.HTTP_201_CREATED)
def create(agenda_request: AgendaRequest):

    validaCampos = agendaUseCase.valida_agenda_create(Agenda(**agenda_request.__dict__))
    
    if not validaCampos['completeStatus']:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=validaCampos)

    agenda_entitie = Agenda(**agenda_request.__dict__)

    agendaUseCase.save(agendaSent=agenda_entitie)

    return agenda_request

@router_agenda.put("/{idAgenda}", status_code=status.HTTP_201_CREATED)
def update(agendaSent: AgendaRequestId):
    if agendaUseCase.find_by_id(agendaSent.idAgenda) is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail="agenda não existente")
    agendaUseCase.update(agendaSent)


@router_agenda.delete("/{idAgenda}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int):
    agenda = agendaUseCase.find_by_id(id)
    if agenda is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="agenda não encontrado")

    agendaUseCase.delete_by_id(agenda_id=agenda.idAgenda)

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router_agenda.get("/", response_model=list[AgendaResponse])
def find_all():
    '''Faz uma query de todos os objetos assistente na DB (sem paginação)'''
    agenda = agendaUseCase.find_all()
    return agenda

@router_agenda.get("/{idAgenda}",
                  response_model=AgendaResponse,
                  status_code=status.HTTP_200_OK)
def find_by_id(idAgenda: int):
    '''Faz uma query de um objeto assistente na DB pelo id'''
    agenda = agendaUseCase.find_by_id(idAgenda)

    if agenda is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Agenda não encontrado")

    return agenda

@router_agenda.get("/cpf/{cpfProfissional}",
                  response_model=list[AgendaResponse],
                  status_code=status.HTTP_200_OK)
def find_by_cpf(cpf: str):
    '''Faz uma query de um objeto assistente na DB pelo id'''
    agenda = agendaUseCase.find_by_cpf(cpf)

    if agenda is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Agenda não encontrado")

    return agenda


