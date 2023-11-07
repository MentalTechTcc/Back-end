from database import engine, Base
from fastapi import APIRouter, status, Response, status, HTTPException
from security import get_password_hash
from domain.entities.TematicasPrincipais import (TematicasPrincipaisResponse,
                                   TematicasPrincipaisRequest,
                                   TematicasPrincipais,
                                   TematicasPrincipaisRequestId,
                                   ProfissionalTrataTematicas,
                                   ProfissionalTrataTematicasRequest,
                                   ProfissionalTrataTematicasBase)
from application.controllers import tematicasPrincipaisUseCase, profissionalTrataTematicasUseCase
from typing import List

Base.metadata.create_all(bind=engine)


router_tematicas_principais = APIRouter(
    prefix="/tematicasPrincipais",
    tags=["tematicasPrincipais"]
)



@router_tematicas_principais.post("/", status_code=status.HTTP_201_CREATED)
def create(tematicasPrincipais_request: TematicasPrincipaisRequest):
    validaCampos = tematicasPrincipaisUseCase.valida_tematica_create(TematicasPrincipais(**tematicasPrincipais_request.__dict__))
    
    if not validaCampos['completeStatus']:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=validaCampos)

    tematicasPrincipais_entitie = TematicasPrincipais(**tematicasPrincipais_request.__dict__)

    tematicasPrincipaisUseCase.save(tematicasPrincipaisSent=tematicasPrincipais_entitie)

    return tematicasPrincipais_request

@router_tematicas_principais.put("/{idTematicasPrincipais}", status_code=status.HTTP_201_CREATED)
def update(tematicasPrincipaisSent: TematicasPrincipaisRequestId):
    if tematicasPrincipaisUseCase.find_by_id(tematicasPrincipaisSent.idTematicasPrincipais) is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail="TematicasPrincipais não existente")
    tematicasPrincipaisUseCase.update(tematicasPrincipaisSent)


@router_tematicas_principais.delete("/{idTematicasPrincipais}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int):
    tematicasPrincipais = tematicasPrincipaisUseCase.find_by_id(id)
    if tematicasPrincipais is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="TematicasPrincipais não encontrado")

    tematicasPrincipaisUseCase.delete_by_id(tematicasPrincipais_id=tematicasPrincipais.idTematicasPrincipais)

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router_tematicas_principais.get("/", response_model=list[TematicasPrincipaisResponse])
def find_all():
    '''Faz uma query de todos os objetos assistente na DB (sem paginação)'''
    tematicasPrincipais = tematicasPrincipaisUseCase.find_all()
    return tematicasPrincipais

@router_tematicas_principais.get("/{idTematicasPrincipais}",
                  response_model=TematicasPrincipaisResponse,
                  status_code=status.HTTP_200_OK)
def find_by_id(id: int):
    '''Faz uma query de um objeto assistente na DB pelo id'''
    tematicasPrincipais = tematicasPrincipaisUseCase.find_by_id(id)

    if tematicasPrincipais is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="TematicasPrincipais não encontrado")

    return tematicasPrincipais


### profissional trata temáticas principais #####

@router_tematicas_principais.post("/ProfissionalTrataTematicas", status_code=status.HTTP_201_CREATED)
def create(tematicasPrincipais_request: ProfissionalTrataTematicasBase):

    pessoaTematicasPrincipaisEntitie = ProfissionalTrataTematicas(**tematicasPrincipais_request.__dict__)
    pessoa_sent = pessoaTematicasPrincipaisEntitie
    idsTematicas=pessoa_sent.idTematicasPrincipais.split(',')

    for id in idsTematicas:
        pessoa_tematicasPrincipais = ProfissionalTrataTematicas(**tematicasPrincipais_request.__dict__) 
        pessoa_tematicasPrincipais.idTematicasPrincipais= int(id)
        profissionalTrataTematicasUseCase.save(profissionalTrataTematicasSent=pessoa_tematicasPrincipais)

    return tematicasPrincipais_request


@router_tematicas_principais.get("/ProfissionalTrataTematicas/{cpf}",
                  response_model=List[ProfissionalTrataTematicasRequest],
                  status_code=status.HTTP_200_OK)
def find_by_idPessoa(cpf: str):
    '''Faz uma query de um objeto assistente na DB pelo id'''
    profissionalEspecialidades = profissionalTrataTematicasUseCase.find_by_cpfProfissional(cpf)

    if not profissionalEspecialidades:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="tematicasPrincipais não encontrado")

    response_data = [
        ProfissionalTrataTematicasRequest(
            cpfProfissional=pessoaEspecialidade.cpfProfissional,
            idTematicasPrincipais=pessoaEspecialidade.idTematicasPrincipais,
        )
        for pessoaEspecialidade in profissionalEspecialidades
    ]

    return response_data


@router_tematicas_principais.delete("/ProfissionalTrataTematicas/{cpf}/{idTematicasPrincipais}", status_code=status.HTTP_204_NO_CONTENT)
def delete(cpf: str,  idTematicasPrincipais:int):

    profissionalTrataTematicasUseCase.delete(cpf=cpf,idTematicasPrincipais=idTematicasPrincipais)

    return Response(status_code=status.HTTP_204_NO_CONTENT)



@router_tematicas_principais.get("/cpf/{cpfProfissional}",
                  response_model=list[TematicasPrincipaisResponse],
                  status_code=status.HTTP_200_OK)
def find_by_cpfProfissional( cpfProfissional:str):

    tematicas = tematicasPrincipaisUseCase.find_by_cpfProfissional(cpfProfissional)

    if tematicas is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="temáticas não encontrado")

    return tematicas
