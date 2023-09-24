from database import engine, Base
from fastapi import APIRouter, status, Response, status, HTTPException
from domain.entities.Diagnostico import (DiagnosticoResponse,
                                   DiagnosticoRequest,
                                   Diagnostico,
                                   DiagnosticoRequestId)
from application.controllers import diagnosticoUseCase

Base.metadata.create_all(bind=engine)


router_diagnostico = APIRouter(
    prefix="/diagnostico",
    tags=["diagnostico"]
)



@router_diagnostico.post("/", status_code=status.HTTP_201_CREATED)
def create(diagnostico_request: DiagnosticoRequest):

    validaCampos = diagnosticoUseCase.valida_diagnostico_create(Diagnostico(**diagnostico_request.__dict__))
    
    if not validaCampos['completeStatus']:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=validaCampos)

    diagnostico_entitie = Diagnostico(**diagnostico_request.__dict__)

    diagnosticoUseCase.save(diagnosticoSent=diagnostico_entitie)

    return diagnostico_request

@router_diagnostico.put("/{idDiagnostico}", status_code=status.HTTP_201_CREATED)
def update(diagnosticoSent: DiagnosticoRequestId):
    if diagnosticoUseCase.find_by_id(diagnosticoSent.idDiagnostico) is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail="Diagnostico não existente")
    diagnosticoUseCase.update(diagnosticoSent)


@router_diagnostico.delete("/{idDiagnostico}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int):
    diagnostico = diagnosticoUseCase.find_by_id(id)
    if diagnostico is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Diagnostico não encontrado")

    diagnosticoUseCase.delete_by_id(diagnostico_id=diagnostico.idDiagnostico)

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router_diagnostico.get("/", response_model=list[DiagnosticoResponse])
def find_all():
    '''Faz uma query de todos os objetos assistente na DB (sem paginação)'''
    diagnostico = diagnosticoUseCase.find_all()
    return diagnostico

@router_diagnostico.get("/{idDiagnostico}",
                  response_model=DiagnosticoResponse,
                  status_code=status.HTTP_200_OK)
def find_by_id(id: int):
    '''Faz uma query de um objeto assistente na DB pelo id'''
    diagnostico = diagnosticoUseCase.find_by_id(id)

    if diagnostico is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Diagnostico não encontrado")

    return diagnostico



