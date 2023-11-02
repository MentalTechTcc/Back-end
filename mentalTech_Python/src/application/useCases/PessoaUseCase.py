from domain.entities.Pessoa import Pessoa, PessoaResponse, PessoaBase, PessoaRequestId
from domain.repositories.PessoaRepositoryBaseModel import PessoaRepositoryBaseModel
from domain.repositories.TokenRepositoryBaseModel import TokensRepositoryBaseModel
from .ValidacaoCamposUseCase import ValidacaoCamposUseCase
from security import verify_password
from typing import NoReturn
from fastapi import HTTPException, status

class PessoaUseCase():
    __pessoaRepository__: PessoaRepositoryBaseModel
    __tokensRepository__: TokensRepositoryBaseModel

    def __init__(
        self,
        pessoaRepository: PessoaRepositoryBaseModel,
        tokensRepository: TokensRepositoryBaseModel
    ):
        self.__pessoaRepository__ = pessoaRepository
        self.__tokensRepository__ = tokensRepository

    def login(self, email: str, senha: str) -> tuple[str, str]:
        pessoa = self.__pessoaRepository__.find_by_email(email)

        if not pessoa or not verify_password(senha, pessoa.senha):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Email ou nome de usuário incorretos"
            )

        userToken = self.__tokensRepository__.createUserToken(
            pessoa.email)
        refreshToken = self.__tokensRepository__.createRefreshToken(
            pessoa.email)

        return (userToken, refreshToken)

    def verifyToken(self, token: str) -> Pessoa:
        userLogin = self.__tokensRepository__.verifyToken(token=token)
        pessoa = self.__pessoaRepository__.find_by_email(
            userLogin)

        return pessoa

    def refreshSession(self, refresh_token: str) -> tuple[str, str] | None:
        print("Token recebido: ", refresh_token)
        isRefreshTokenValid = self.__tokensRepository__.verifyToken(
            token=refresh_token)

        if isRefreshTokenValid:
            return self.__tokensRepository__.refreshToken(refresh_token=refresh_token)

        return None
    
    def deleteRefreshToken(self, refresh_token: str):
        self.__tokensRepository__.delete_refresh_token(refresh_token)
        return None

    def save(self, pessoaSent: Pessoa) -> Pessoa:
        '''Função para salvar um objeto pessoa na DB, utilizada também como update'''
        return self.__pessoaRepository__.save(pessoaSent=pessoaSent)

    def delete_by_id(self, pessoa_id: int) -> None:
        return self.__pessoaRepository__.delete_by_id(pessoa_id=pessoa_id)


    def find_all(self) -> list[PessoaResponse]:
        pessoas_db = self.__pessoaRepository__.find_all()
        pessoas = []
        for pessoa_db in pessoas_db:
            pessoa = PessoaResponse(
                nome=pessoa_db.nome,
                idPessoa = pessoa_db.idPessoa,
                senha = pessoa_db.senha,
                email=pessoa_db.email,
                telefone=pessoa_db.telefone,
                dataNascimento=pessoa_db.dataNascimento,
                sexo=pessoa_db.sexo,
                administrador=pessoa_db.administrador,
                dataCadastro= pessoa_db.dataCadastro
                
            )
            pessoas.append(pessoa)
        return pessoas

    def find_by_id(self, pessoa_id : int) -> PessoaBase | None:
        return self.__pessoaRepository__.find_by_id(pessoa_id=pessoa_id)

    def find_by_email(self, email : str) -> PessoaBase | None:
        return self.__pessoaRepository__.find_by_email(email=email)
    
    def find_by_cpfProfissional(self, cpfProfissional: int) -> list[Pessoa] | None: 
        return self.__pessoaRepository__.find_by_cpfProfissional(cpfProfissional=cpfProfissional)

    def update(self, pessoaSent: PessoaRequestId) -> NoReturn:
        """Sobrescreve os dados de pessoa, assume que ele já exista"""
        self.__pessoaRepository__.update(Pessoa(**pessoaSent.__dict__))

    
    def valida_pessoa_create(self, pessoa: Pessoa) -> dict:

        fieldInfoDict = {}
        fieldInfoDict["nome"] = vars(ValidacaoCamposUseCase.nomeValidation(
            pessoa.nome))
        fieldInfoDict["senha"] = vars(ValidacaoCamposUseCase.senhaValidation(
            pessoa.senha))
        fieldInfoDict["dataNascimento"] = vars(ValidacaoCamposUseCase.dNascimentoValidation(
        pessoa.dataNascimento))
        fieldInfoDict["telefone"] = vars(ValidacaoCamposUseCase.telefoneValidation(
            pessoa.telefone))
        fieldInfoDict["email"] = vars(ValidacaoCamposUseCase.emailValidation(
            pessoa.email))
        completeStatus = True
        for key in fieldInfoDict:
            if fieldInfoDict[key]['status'] == False:
                completeStatus = False
                break
        fieldInfoDict['completeStatus'] = completeStatus

        return fieldInfoDict