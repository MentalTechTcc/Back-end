from database import engine, Base
from fastapi import APIRouter, status, Response, status, HTTPException
from typing import List
from security import get_password_hash
from domain.entities.Endereco import (EnderecoResponse,
                                   EnderecoRequest,
                                   Endereco,
                                   EnderecoRequestId,
                                   ProfissionalPossuiEndereco,
                                   ProfissionalPossuiEnderecoBase,
                                   ProfissionalPossuiEnderecoRequest)
from application.controllers import enderecoUseCase, profissionalPossuiEnderecoUseCase

Base.metadata.create_all(bind=engine)


router_endereco = APIRouter(
    prefix="/endereco",
    tags=["endereco"]
)

@router_endereco.post("/", status_code=status.HTTP_201_CREATED)
def create(endereco_request: EnderecoRequest):

    validaCampos = enderecoUseCase.valida_endereco_create(Endereco(**endereco_request.__dict__))
    
    if not validaCampos['completeStatus']:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=validaCampos)

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






@router_endereco.post("/PessoaPossuiEndereco", status_code=status.HTTP_201_CREATED)
def create(endereco_request: ProfissionalPossuiEnderecoBase):

    pessoa_endereco_entitie = ProfissionalPossuiEndereco(**endereco_request.__dict__)
    profissionalPossuiEnderecoUseCase.save(profissionalPossuiEnderecoSent=pessoa_endereco_entitie)

    return endereco_request


@router_endereco.get("/PessoaPossuiEndereco/{cpf}",
                  response_model=List[ProfissionalPossuiEnderecoRequest],
                  status_code=status.HTTP_200_OK)
def find_by_idPessoa(cpf: str):
    '''Faz uma query de um objeto assistente na DB pelo id'''
    profissionalEnderecos = profissionalPossuiEnderecoUseCase.find_by_cpfProfissional(cpf)

    if not profissionalEnderecos:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="endereco não encontrado")

    response_data = [
        ProfissionalPossuiEnderecoRequest(
            cpfProfissional=pessoaEndereco.cpfProfissional,
            idEndereco=pessoaEndereco.idEndereco,
        )
        for pessoaEndereco in profissionalEnderecos
    ]

    return response_data


@router_endereco.delete("/PessoaPossuiEndereco/{cpf}/{enderecoId}", status_code=status.HTTP_204_NO_CONTENT)
def delete(cpf: str,  enderecoId:int):

    profissionalPossuiEnderecoUseCase.delete(cpf=cpf,enderecoId=enderecoId)

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router_endereco.get("/cpfProfissional/{cpfProfissional}",
                  response_model=list[EnderecoResponse],
                  status_code=status.HTTP_200_OK)
def find_by_cpfProfissional(cpfProfissional:str):

    endereco = enderecoUseCase.find_by_cpfProfissional(cpfProfissional=cpfProfissional)

    if endereco is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="endereco não encontrado")

    return endereco
