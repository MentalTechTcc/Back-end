from fastapi import APIRouter, Form, Header, HTTPException
from infrastructure.repositories.PessoaRepository import PessoaRepository
from infrastructure.repositories.TokenRepository import TokensRepository


from fastapi import APIRouter, Form, Header, HTTPException, status

from ..controllers import pessoaUseCase
from ..controllers import profissionalUseCase


routerLoginPessoa = APIRouter(
    prefix="/login",
    tags=["login: pessoa"],
    responses={404: {"description": "Not found"}},
)


@routerLoginPessoa.post("/pessoa/")
async def login(email: str = Form(...), senha: str = Form(...)):
    access_token, refresh_token = pessoaUseCase.login(
        email=email, senha=senha
    )

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
    }


@routerLoginPessoa.get("/pessoa/token", status_code=201)
async def verificarToken(authorization: str = Header(...)):
    pessoa = pessoaUseCase.verifyToken(authorization)
    pessoa.senha = None
    return pessoa


@routerLoginPessoa.post("/pessoa/token/refresh", status_code=201)
async def refreshToken(refresh_token: str = Header(...)):
    tokens = pessoaUseCase.refreshSession(refresh_token=refresh_token)
    if tokens:
        return {
            "access_token": tokens[0],
            "refresh_token": tokens[1],
            "token_type": "bearer",
        }

    raise HTTPException(401, "Not Allowed")


@routerLoginPessoa.post("/pessoa/logout")
def logout(refresh_token: str = Header(...)):
    pessoaUseCase.deleteRefreshToken(refresh_token)

    return {"message": "Logout realizado com sucesso"}


### profissional

@routerLoginPessoa.post("/profissional/")
async def login(cpf: str = Form(...), senha: str = Form(...)):
    access_token, refresh_token = profissionalUseCase.login(
        cpf=cpf, senha=senha
    )

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
    }


@routerLoginPessoa.get("/profissional/token", status_code=201)
async def verificarToken(authorization: str = Header(...)):
    profissional = profissionalUseCase.verifyToken(authorization)
    profissional.senha = None
    return profissional


@routerLoginPessoa.post("/profissional/token/refresh", status_code=201)
async def refreshToken(refresh_token: str = Header(...)):
    tokens = profissionalUseCase.refreshSession(refresh_token=refresh_token)
    if tokens:
        return {
            "access_token": tokens[0],
            "refresh_token": tokens[1],
            "token_type": "bearer",
        }

    raise HTTPException(401, "Not Allowed")


@routerLoginPessoa.post("/profissional/logout")
def logout(refresh_token: str = Header(...)):
    profissionalUseCase.deleteRefreshToken(refresh_token)

    return {"message": "Logout realizado com sucesso"}
