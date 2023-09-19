from database import engine, Base
from fastapi import APIRouter, status, Response, status, HTTPException
from security import get_password_hash
from domain.entities.Endereco import (EnderecoResponse,
                                   EnderecoRequest,
                                   Endereco,
                                   EnderecoRequestId)
from application.controllers import enderecoUseCase

Base.metadata.create_all(bind=engine)


router_endereco = APIRouter(
    prefix="/endereco",
    tags=["endereco"]
)

@router_endereco.post("/", status_code=status.HTTP_201_CREATED)
def create(endereco_request: EnderecoRequest):

    endereco_entitie = Endereco(**endereco_request.__dict__)

    enderecoUseCase.save(enderecoSent=endereco_entitie)

    return endereco_request

@router_endereco.put("/{idEndereco}", status_code=status.HTTP_201_CREATED)
def update(enderecoSent: EnderecoRequestId):
    if enderecoUseCase.find_by_id(enderecoSent.idEndereco) is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail="endereco não existente")
    enderecoUseCase.update(enderecoSent)


@router_endereco.delete("/{idEndereco}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int):
    endereco = enderecoUseCase.find_by_id(id)
    if endereco is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="endereco não encontrado")

    enderecoUseCase.delete_by_id(endereco_id=endereco.idEndereco    )

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router_endereco.get("/", response_model=list[EnderecoResponse])
def find_all():
    '''Faz uma query de todos os objetos assistente na DB (sem paginação)'''
    endereco = enderecoUseCase.find_all()
    return endereco

@router_endereco.get("/{idEndereco}",
                  response_model=EnderecoResponse,
                  status_code=status.HTTP_200_OK)
def find_by_id(id: int):
    '''Faz uma query de um objeto assistente na DB pelo id'''
    endereco = enderecoUseCase.find_by_id(id)

    if endereco is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="endereco não encontrado")

    return endereco



