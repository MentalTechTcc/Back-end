from database import engine, Base
from fastapi import APIRouter, status, Response, status, HTTPException
from security import get_password_hash
from domain.entities.Avaliacao import (AvaliacaoResponse,
                                   AvaliacaoRequest,
                                   Avaliacao,
                                   AvaliacaoRequestId)
from application.controllers import avaliacaoUseCase

Base.metadata.create_all(bind=engine)


router_avaliacao = APIRouter(
    prefix="/avaliacao",
    tags=["avaliacao"]
)



@router_avaliacao.post("/", status_code=status.HTTP_201_CREATED)
def create(avaliacao_request: AvaliacaoRequest):

    validaCampos = avaliacaoUseCase.valida_avaliacao_create(Avaliacao(**avaliacao_request.__dict__))
    
    if not validaCampos['completeStatus']:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=validaCampos)

    avaliacao_entitie = Avaliacao(**avaliacao_request.__dict__)

    avaliacaoUseCase.save(avaliacaoSent=avaliacao_entitie)

    return avaliacao_request

@router_avaliacao.put("/{idAvaliacao}", status_code=status.HTTP_201_CREATED)
def update(avaliacaoSent: AvaliacaoRequestId):
    if avaliacaoUseCase.find_by_id(avaliacaoSent.idAvaliacao) is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail="Avaliacao não existente")
    avaliacaoUseCase.update(avaliacaoSent)


@router_avaliacao.delete("/{idAvaliacao}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int):
    avaliacao = avaliacaoUseCase.find_by_id(id)
    if avaliacao is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Avaliacao não encontrado")

    avaliacaoUseCase.delete_by_id(avaliacao_id=avaliacao.idAvaliacao)

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router_avaliacao.get("/", response_model=list[AvaliacaoResponse])
def find_all():
    '''Faz uma query de todos os objetos assistente na DB (sem paginação)'''
    avaliacao = avaliacaoUseCase.find_all()
    return avaliacao

@router_avaliacao.get("/{idAvaliacao}",
                  response_model=AvaliacaoResponse,
                  status_code=status.HTTP_200_OK)
def find_by_id(id: int):
    '''Faz uma query de um objeto assistente na DB pelo id'''
    avaliacao = avaliacaoUseCase.find_by_id(id)

    if avaliacao is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Avaliacao não encontrado")

    return avaliacao



