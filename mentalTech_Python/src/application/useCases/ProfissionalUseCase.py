from domain.entities.Profissional import Profissional, ProfissionalResponse, ProfissionalBase, ProfissionalRequestId
from domain.repositories.TokenRepositoryBaseModel import TokensRepositoryBaseModel
from domain.repositories.ProfissionalRepositoryBaseModel import ProfissionalRepositoryBaseModel
from .ValidacaoCamposUseCase import ValidacaoCamposUseCase
from security import verify_password
from typing import NoReturn
from fastapi import HTTPException, status


class ProfissionalUseCase():
    __profissionalRepository__: ProfissionalRepositoryBaseModel
    __tokensRepository__: TokensRepositoryBaseModel

    def __init__(
        self,
        profissionalRepository: ProfissionalRepositoryBaseModel,
        tokensRepository: TokensRepositoryBaseModel
    ):
        self.__profissionalRepository__ = profissionalRepository
        self.__tokensRepository__ = tokensRepository

    def login(self, email: str, senha: str) -> tuple[str, str]:
        profissional = self.__profissionalRepository__.find_by_email(email)

        if not profissional or not verify_password(senha, profissional.senha):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Email ou nome de usuário incorretos"
            )

        userToken = self.__tokensRepository__.createUserToken(
            profissional.email)
        refreshToken = self.__tokensRepository__.createRefreshToken(
            profissional.email)

        return (userToken, refreshToken)

    def verifyToken(self, token: str) -> Profissional:
        userLogin = self.__tokensRepository__.verifyToken(token=token)
        profissional = self.__profissionalRepository__.find_by_email(
            userLogin)

        return profissional

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

    def save(self, profissionalSent: Profissional) -> Profissional:
        '''Função para salvar um objeto profissional na DB, utilizada também como update'''
        return self.__profissionalRepository__.save(profissionalSent=profissionalSent)

    def delete_by_id(self, profissional_id: int) -> None:
        return self.__profissionalRepository__.delete_by_id(profissional_id=profissional_id)


    def find_all(self) -> list[ProfissionalResponse]:
        profissional_db = self.__profissionalRepository__.find_all()
        profissionais = []
        for profissional_db in profissional_db:
            profissional = ProfissionalResponse(
                nome=profissional_db.nome,
                idPessoa = profissional_db.idPessoa,
                senha=profissional_db.senha,
                dataNascimento=profissional_db.dataNascimento,
                telefone=profissional_db.telefone,
                email=profissional_db.email,
                sexo=profissional_db.sexo,
                administrador = profissional_db.administrador,
                cpf = profissional_db.cpf,
                codigoProfissional = profissional_db.codigoProfissional,
                descricaoProfissional = profissional_db.descricaoProfissional
            )
            profissionais.append(profissional)
        return profissionais

    def find_by_id(self, profissional_id : int) -> ProfissionalBase | None:
        return self.__profissionalRepository__.find_by_id(profissional_id=profissional_id)

    def find_by_email(self, email : str) -> ProfissionalBase | None:
        return self.__profissionalRepository__.find_by_email(email=email)

    def update(self, profissionalSent: ProfissionalRequestId) -> NoReturn:
        """Sobrescreve os dados de profissional, assume que ele já exista"""
        self.__profissionalRepository__.update(Profissional(**profissionalSent.__dict__))

    def valida_profissional_create(self, profissional: Profissional) -> dict:

        fieldInfoDict = {}
        fieldInfoDict["nome"] = vars(ValidacaoCamposUseCase.nomeValidation(
            profissional.nome))
        fieldInfoDict["senha"] = vars(ValidacaoCamposUseCase.senhaValidation(
            profissional.senha))
        fieldInfoDict["dataNascimento"] = vars(ValidacaoCamposUseCase.dNascimentoValidation(
        profissional.dataNascimento))
        fieldInfoDict["telefone"] = vars(ValidacaoCamposUseCase.telefoneValidation(
            profissional.telefone))
        fieldInfoDict["email"] = vars(ValidacaoCamposUseCase.emailValidation(
            profissional.email))
        fieldInfoDict["cpf"] = vars(ValidacaoCamposUseCase.cpfValidation(
            profissional.cpf))
        fieldInfoDict["descricaoProfissional"] = vars(ValidacaoCamposUseCase.descricaoProfissionalValidation(
            profissional.descricaoProfissional))
        completeStatus = True
        for key in fieldInfoDict:
            if fieldInfoDict[key]['status'] == False:
                completeStatus = False
                break
        fieldInfoDict['completeStatus'] = completeStatus

        return fieldInfoDict