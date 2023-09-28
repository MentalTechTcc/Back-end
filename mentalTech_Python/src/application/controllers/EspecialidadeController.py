from database import engine, Base
from fastapi import APIRouter, status, Response, status, HTTPException
from security import get_password_hash
from typing import List
from domain.entities.Especialidade import (EspecialidadeResponse,
                                   EspecialidadeRequest,
                                   Especialidade,
                                   EspecialidadeRequestId,
                                   ProfissionalPossuiEspecialidade,
                                   ProfissionalPossuiEspecialidadeRequest,
                                   ProfissionalPossuiEspecialidadeBase)
from application.controllers import especialidadeUseCase, profissionalPossuiEspecialidadeUseCase

Base.metadata.create_all(bind=engine)


router_especialidade = APIRouter(
    prefix="/especialidade",
    tags=["especialidade"]
)

@router_especialidade.post("/", status_code=status.HTTP_201_CREATED)
def create(especialidade_request: EspecialidadeRequest):

    especialidade_entitie = Especialidade(**especialidade_request.__dict__)

    especialidadeUseCase.save(especialidadeSent=especialidade_entitie)

    return especialidade_request

@router_especialidade.put("/{idEspecialidade}", status_code=status.HTTP_201_CREATED)
def update(especialidadeSent: EspecialidadeRequestId):
    if especialidadeUseCase.find_by_id(especialidadeSent.idEspecialidade) is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail="especialidade não existente")
    especialidadeUseCase.update(especialidadeSent)


@router_especialidade.delete("/{idEspecialidade}", status_code=status.HTTP_204_NO_CONTENT)
def delete(idEspecialidade: int):
    especialidade = especialidadeUseCase.find_by_id(idEspecialidade)
    if especialidade is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="especialidade não encontrado")

    especialidadeUseCase.delete_by_id(especialidade_id=idEspecialidade)

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router_especialidade.get("/", response_model=list[EspecialidadeResponse])
def find_all():
    '''Faz uma query de todos os objetos assistente na DB (sem paginação)'''
    especialidade = especialidadeUseCase.find_all()
    return especialidade

@router_especialidade.get("/{idEspecialidade}",
                  response_model=EspecialidadeResponse,
                  status_code=status.HTTP_200_OK)
def find_by_id(id: int):
    '''Faz uma query de um objeto assistente na DB pelo id'''
    especialidade = especialidadeUseCase.find_by_id(id)

    if especialidade is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="especialidade não encontrado")

    return especialidade



@router_especialidade.post("/PessoaPossuiEspecialidade", status_code=status.HTTP_201_CREATED)
def create(especialidade_request: ProfissionalPossuiEspecialidadeBase):

    pessoa_especialidade_entitie = ProfissionalPossuiEspecialidade(**especialidade_request.__dict__)
    profissionalPossuiEspecialidadeUseCase.save(profissionalPossuiEspecialidadeSent=pessoa_especialidade_entitie)

    return especialidade_request


@router_especialidade.get("/PessoaPossuiEspecialidade/{cpf}",
                  response_model=List[ProfissionalPossuiEspecialidadeRequest],
                  status_code=status.HTTP_200_OK)
def find_by_idPessoa(cpf: str):
    '''Faz uma query de um objeto assistente na DB pelo id'''
    profissionalEspecialidades = profissionalPossuiEspecialidadeUseCase.find_by_cpfProfissional(cpf)

    if not profissionalEspecialidades:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="especialidade não encontrado")

    response_data = [
        ProfissionalPossuiEspecialidadeRequest(
            cpfProfissional=pessoaEspecialidade.cpfProfissional,
            idEspecialidade=pessoaEspecialidade.idEspecialidade,
        )
        for pessoaEspecialidade in profissionalEspecialidades
    ]

    return response_data


@router_especialidade.delete("/PessoaPossuiEspecialidade/{cpf}/{idEspecialidade}", status_code=status.HTTP_204_NO_CONTENT)
def delete(cpf: str,  idEspecialidade:int):

    profissionalPossuiEspecialidadeUseCase.delete(cpf=cpf,idEspecialidade=idEspecialidade)

    return Response(status_code=status.HTTP_204_NO_CONTENT)


