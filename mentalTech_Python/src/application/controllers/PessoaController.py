from database import engine, Base
from fastapi import APIRouter, status, Response, status, HTTPException
from security import get_password_hash
from domain.entities.Pessoa import (PessoaResponse,
                                   PessoaRequest,
                                   Pessoa,
                                   PessoaRequestId)
from application.controllers import  pessoaUseCase

Base.metadata.create_all(bind=engine)


router_pessoa = APIRouter(
    prefix="/pessoa",
    tags=["pessoa"]
)



@router_pessoa.post("/", status_code=status.HTTP_201_CREATED)
def create(pessoa_request: PessoaRequest):
    validaCampos = pessoaUseCase.valida_pessoa_create(Pessoa(**pessoa_request.__dict__))
    
    if not validaCampos['completeStatus']:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=validaCampos)


    pessoa_entitie = Pessoa(**pessoa_request.__dict__)
    pessoa_entitie.senha = get_password_hash(pessoa_entitie.senha) 

    pessoaUseCase.save(pessoaSent=pessoa_entitie)

    return pessoa_request

@router_pessoa.put("/{idPessoa}", status_code=status.HTTP_201_CREATED)
def update(pessoaSent: PessoaRequestId):

    if pessoaUseCase.find_by_id(pessoaSent.idPessoa) is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail="Pessoa não existente")
    
    pessoa_entitie = PessoaRequestId(**pessoaSent.__dict__)
    pessoa_entitie.senha = get_password_hash(pessoa_entitie.senha) 
    pessoaUseCase.update(pessoa_entitie)


@router_pessoa.delete("/{idPessoa}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int):
    pessoa = pessoaUseCase.find_by_id(id)
    if pessoa is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pessoa não encontrado")

    pessoaUseCase.delete_by_id(pessoa_id=pessoa.idPessoa)

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router_pessoa.get("/", response_model=list[PessoaResponse])
def find_all():
    '''Faz uma query de todos os objetos assistente na DB (sem paginação)'''
    pessoa = pessoaUseCase.find_all()
    return pessoa

@router_pessoa.get("/{idPessoa}",
                  response_model=PessoaResponse,
                  status_code=status.HTTP_200_OK)
def find_by_id(id: int):
    '''Faz uma query de um objeto assistente na DB pelo id'''
    pessoa = pessoaUseCase.find_by_id(id)

    if pessoa is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Pessoa não encontrado")

    return pessoa


@router_pessoa.get("/email/{email}", response_model=PessoaResponse, status_code=status.HTTP_200_OK)
def find_by_email(email: str):
    '''Faz uma query de um objeto assistente na DB pelo email'''
    pessoa = pessoaUseCase.find_by_email(email)

    if pessoa is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="email não encontrado")

    return pessoa



@router_pessoa.get("/cpfProfissional/{cpfProfissional}", response_model=list[PessoaResponse], status_code=status.HTTP_200_OK)
def find_by_cpfProfissional(cpfProfissional: str):
    '''Faz uma query de um objeto assistente na DB pelo email'''
    pessoa = pessoaUseCase.find_by_cpfProfissional(cpfProfissional)

    if pessoa is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="cpf não encontrado")

    return pessoa


