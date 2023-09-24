from database import engine, Base
from fastapi import APIRouter, status, Response, status, HTTPException
from security import get_password_hash
from domain.entities.DicaSaude import (DicaSaudeResponse,
                                   DicaSaudeRequest,
                                   DicaSaude,
                                   DicaSaudeRequestId)
from application.controllers import dicaSaudeUseCase

Base.metadata.create_all(bind=engine)


router_dica_saude = APIRouter(
    prefix="/dicaSaude",
    tags=["dicaSaude"]
)



@router_dica_saude.post("/", status_code=status.HTTP_201_CREATED)
def create(dicaSaude_request: DicaSaudeRequest):
    validaCampos = dicaSaudeUseCase.valida_dica_create(DicaSaude(**dicaSaude_request.__dict__))
    
    if not validaCampos['completeStatus']:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=validaCampos)


    dicaSaude_entitie = DicaSaude(**dicaSaude_request.__dict__)

    dicaSaudeUseCase.save(dicaSaudeSent=dicaSaude_entitie)

    return dicaSaude_request

@router_dica_saude.put("/{idDicaSaude}", status_code=status.HTTP_201_CREATED)
def update(dicaSaudeSent: DicaSaudeRequestId):
    if dicaSaudeUseCase.find_by_id(dicaSaudeSent.idDicaSaude) is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND,
                            detail="DicaSaude não existente")
    dicaSaudeUseCase.update(dicaSaudeSent)


@router_dica_saude.delete("/{idDicaSaude}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int):
    dicaSaude = dicaSaudeUseCase.find_by_id(id)
    if dicaSaude is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="DicaSaude não encontrado")

    dicaSaudeUseCase.delete_by_id(dicaSaude_id=dicaSaude.idDicaSaude)

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router_dica_saude.get("/", response_model=list[DicaSaudeResponse])
def find_all():
    '''Faz uma query de todos os objetos assistente na DB (sem paginação)'''
    dicaSaude = dicaSaudeUseCase.find_all()
    return dicaSaude

@router_dica_saude.get("/{idDicaSaude}",
                  response_model=DicaSaudeResponse,
                  status_code=status.HTTP_200_OK)
def find_by_id(id: int):
    '''Faz uma query de um objeto assistente na DB pelo id'''
    dicaSaude = dicaSaudeUseCase.find_by_id(id)

    if dicaSaude is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="DicaSaude não encontrado")

    return dicaSaude



