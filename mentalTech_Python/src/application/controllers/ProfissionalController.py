from database import engine, Base
from fastapi import APIRouter, status, Response, status, HTTPException
from security import get_password_hash
from domain.entities.Profissional import (ProfissionalResponse,
                                   ProfissionalRequest,
                                   Profissional,
                                   ProfissionalRequestId)
from application.controllers import  profissionalUseCase
from fastapi import HTTPException, UploadFile, File, Form

Base.metadata.create_all(bind=engine)


router_profissional = APIRouter(
    prefix="/profissional",
    tags=["profissional"]
)

@router_profissional.post("/", status_code=status.HTTP_201_CREATED)
def create(profissional_request: ProfissionalRequest):

    validaCampos = profissionalUseCase.valida_profissional_create(Profissional(**profissional_request.__dict__))
    if not validaCampos['completeStatus']:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=validaCampos)

    profissional_entitie = Profissional(**profissional_request.__dict__)

    profissional_entitie.senha = get_password_hash(profissional_entitie.senha) 

    profissionalUseCase.save(profissionalSent=profissional_entitie)
    return profissional_request



@router_profissional.put("/{idPessoa}", status_code=status.HTTP_201_CREATED)
def update(profissionalSent: ProfissionalRequestId):
    if profissionalUseCase.find_by_id(profissionalSent.idPessoa) is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail="Profissional não existente")
    profissionalUseCase.update(profissionalSent)


@router_profissional.delete("/{idPessoa}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int):
    profissional = profissionalUseCase.find_by_id(id)
    if profissional is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Profissional não encontrado")

    profissionalUseCase.delete_by_id(profissional_id=profissional.idPessoa)

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router_profissional.get("/", response_model=list[ProfissionalResponse])
def find_all():
    '''Faz uma query de todos os objetos assistente na DB (sem paginação)'''
    profissional = profissionalUseCase.find_all()
    return profissional

@router_profissional.get("/{idPessoa}",
                  response_model=ProfissionalResponse,
                  status_code=status.HTTP_200_OK)
def find_by_id(id: int):
    '''Faz uma query de um objeto assistente na DB pelo id'''
    profissional = profissionalUseCase.find_by_id(id)

    if profissional is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Profissional não encontrado")

    return profissional


@router_profissional.get("/email/{email}", response_model=ProfissionalResponse, status_code=status.HTTP_200_OK)
def find_by_email(email: str):
    '''Faz uma query de um objeto assistente na DB pelo email'''
    profissional = profissionalUseCase.find_by_email(email)

    if profissional is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="email não encontrado")

    return profissional

