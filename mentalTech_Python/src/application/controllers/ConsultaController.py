from database import engine, Base
from fastapi import APIRouter, status, Response, status, HTTPException
from security import get_password_hash
from domain.entities.Consulta import (ConsultaResponse,
                                   ConsultaRequest,
                                   Consulta,
                                   ConsultaRequestId)
from application.controllers import consultaUseCase, agendaUseCase

Base.metadata.create_all(bind=engine)


router_consulta = APIRouter(
    prefix="/consulta",
    tags=["consulta"]
)



@router_consulta.post("/", status_code=status.HTTP_201_CREATED)
def create(consulta_request: ConsultaRequest):
    
    validaCampos = consultaUseCase.valida_consulta_create(Consulta(**consulta_request.__dict__))
    
    if not validaCampos['completeStatus']:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=validaCampos)

    consulta_entitie = Consulta(**consulta_request.__dict__)

    consultaUseCase.save(consultaSent=consulta_entitie)

    return consulta_request

@router_consulta.put("/{idConsulta}", status_code=status.HTTP_201_CREATED)
def update(consultaSent: ConsultaRequestId):
    if consultaUseCase.find_by_id(consultaSent.idConsulta) is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail="Consulta não existente")
    consultaUseCase.update(consultaSent)


@router_consulta.delete("/{idConsulta}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int):
    consulta = consultaUseCase.find_by_id(id)
    if consulta is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Consulta não encontrado")

    consultaUseCase.delete_by_id(consulta_id=consulta.idConsulta)

    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router_consulta.delete("/idAgenda/{idAgenda}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int):
    consultaUseCase.delete_by_idAgenda(agenda_id=int(id))

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router_consulta.get("/", response_model=list[ConsultaResponse])
def find_all():
    '''Faz uma query de todos os objetos assistente na DB (sem paginação)'''
    consulta = consultaUseCase.find_all()
    return consulta

@router_consulta.get("/{idConsulta}",
                  response_model=ConsultaResponse,
                  status_code=status.HTTP_200_OK)
def find_by_id(id: int):
    '''Faz uma query de um objeto assistente na DB pelo id'''
    consulta = consultaUseCase.find_by_id(id)

    if consulta is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Consulta não encontrado")

    return consulta


@router_consulta.get("/idPessoa/{idPessoa}",
                  response_model=list[ConsultaResponse],
                  status_code=status.HTTP_200_OK)
def find_by_idPessoa(idPessoa: int):

    consulta = consultaUseCase.find_by_idPessoa(idPessoa)

    if consulta is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Agenda não encontrado")

    return consulta





