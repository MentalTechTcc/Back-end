import pytest
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from application.useCases.PessoaUseCase import PessoaUseCase
from infrastructure.repositories.PessoaRepository import PessoaRepository
from infrastructure.repositories.TokenRepository import TokensRepository
from domain.entities.Pessoa import Pessoa, PessoaResponse, Sexo
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from unittest.mock import MagicMock
import enum

test_session = UnifiedAlchemyMagicMock()

def get_mock_db_session():
    """Callable do db em mock para o repository"""
    return test_session


pessoaRepo = PessoaRepository(session=get_mock_db_session)
tokensRepo = TokensRepository()  # Adicionado o tokensRepo
pessoaUseCase = PessoaUseCase(
    pessoaRepository=pessoaRepo,
    tokensRepository=tokensRepo,  # Adicionado o tokensRepo
)

class SexoEnum(enum.Enum):
    MASCULINO = 'Masculino'
    FEMININO = 'Feminino'

test_list = [
    (Pessoa(
        nome="João",
        idPessoa=1,
        senha="senha123",
        dataNascimento=datetime.now(),
        telefone="123456789",
        email="joao@example.com",
        sexo=Sexo.M,
        administrador=True,
        dataCadastro=datetime.now(),
        diagnosticos=[],
    )),
    (Pessoa(
        nome="Maria",
        idPessoa=2,
        senha="senha456",
        dataNascimento=datetime.now(),
        telefone="987654321",
        email="maria@example.com",
        sexo=Sexo.F,
        administrador=False,
        dataCadastro=datetime.now(),
        diagnosticos=[],
    ))
]

@pytest.mark.parametrize(
    "pessoa_sent",
    test_list,
)
def testSavePessoaValida(pessoa_sent):
    """Testa se a pessoa é salva com sucesso, assume que sempre recebe uma pessoa válida"""
    response = pessoaUseCase.save(pessoaSent=pessoa_sent)
    assert pessoa_sent == response, response.__dict__

def testPessoaFindAll():
    response = pessoaUseCase.find_all()
    response = [r.__dict__ for r in response]
    sorted_response = sorted(response, key=lambda x: x['idPessoa'])
    #print(sorted_response)

    expected = [r.__dict__ for r in test_list]
    sorted_expected = sorted(expected, key=lambda x: x['idPessoa'])
    #print(sorted_expected)

    assert len(response) == len(test_list), response
