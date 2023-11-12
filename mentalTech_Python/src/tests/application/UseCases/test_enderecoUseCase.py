from domain.entities.Pessoa import Sexo
from domain.entities.Especialidade import ProfissionalPossuiEspecialidade
import pytest
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from sqlalchemy.orm import Session
from unittest.mock import MagicMock
from application.useCases.EnderecoUseCase import EnderecoUseCase
from infrastructure.repositories.EnderecoRepository import EnderecoRepository
from domain.entities.Endereco import Endereco, EnderecoResponse, ProfissionalPossuiEndereco
from domain.entities.Profissional import Profissional

test_session = UnifiedAlchemyMagicMock()


def get_mock_db_session():
    """Callable do db em mock para o repository"""
    return test_session


enderecoRepo = EnderecoRepository(session=get_mock_db_session)
enderecoUseCase = EnderecoUseCase(
    enderecoRepository=enderecoRepo,
)


from domain.entities.Profissional import Profissional

test_list = [
    (EnderecoResponse(
        cep="12345-678",
        estado="São Paulo",
        cidade="São Paulo",
        bairro="Centro",
        numero=123,
        complemento="Apto 4",
        idEndereco=1
    )),
    (EnderecoResponse(
        cep="12345-679",
        estado="São Paulo",
        cidade="São Paulo",
        bairro="Centro",
        numero=123,
        complemento="Apto 5",
        idEndereco=2
    ))
]

@pytest.mark.parametrize(
    "endereco_sent",
    test_list,
)
def testSaveEnderecoValido(endereco_sent):
    """Testa se o endereco é salvo com sucesso, assume que sempre recebe um endereco válido"""
    response = enderecoUseCase.save(enderecoSent=endereco_sent)
    assert endereco_sent.dict() == response.dict(), response.dict()


# def testEnderecoFindAll():
#     response = enderecoUseCase.find_all()
#     response_ids = sorted([r.idEndereco for r in response])

#     expected_ids = sorted([r.idEndereco for r in test_list])

#     print("Response:", response)
#     print("Response IDs:", response_ids)
    
#     assert response_ids == expected_ids, response_ids
