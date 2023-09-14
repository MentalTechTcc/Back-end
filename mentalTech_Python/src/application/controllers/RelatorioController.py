from database import engine, Base
from fastapi import APIRouter, status, Response, status, HTTPException
from security import get_password_hash
from domain.entities.Relatorio import (RelatorioResponse,
                                   RelatorioRequest,
                                   Relatorio,
                                   RelatorioRequestId)
from application.controllers import relatorioUseCase

Base.metadata.create_all(bind=engine)


router_relatorio = APIRouter(
    prefix="/relatorio",
    tags=["relatorio"]
)



@router_relatorio.post("/", status_code=status.HTTP_201_CREATED)
def create(relatorio_request: RelatorioRequest):

    relatorio_entitie = Relatorio(**relatorio_request.__dict__)

    relatorioUseCase.save(relatorioSent=relatorio_entitie)

    return relatorio_request

@router_relatorio.put("/{idRelatorio}", status_code=status.HTTP_201_CREATED)
def update(relatorioSent: RelatorioRequestId):
    if relatorioUseCase.find_by_id(relatorioSent.idRelatorio) is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail="Relatorio não existente")
    relatorioUseCase.update(relatorioSent)


@router_relatorio.delete("/{idRelatorio}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int):
    relatorio = relatorioUseCase.find_by_id(id)
    if relatorio is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Relatorio não encontrado")

    relatorioUseCase.delete_by_id(relatorio_id=relatorio.idRelatorio)

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router_relatorio.get("/", response_model=list[RelatorioResponse])
def find_all():
    '''Faz uma query de todos os objetos assistente na DB (sem paginação)'''
    relatorio = relatorioUseCase.find_all()
    return relatorio

@router_relatorio.get("/{idRelatorio}",
                  response_model=RelatorioResponse,
                  status_code=status.HTTP_200_OK)
def find_by_id(id: int):
    '''Faz uma query de um objeto assistente na DB pelo id'''
    relatorio = relatorioUseCase.find_by_id(id)

    if relatorio is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Relatorio não encontrado")

    return relatorio



