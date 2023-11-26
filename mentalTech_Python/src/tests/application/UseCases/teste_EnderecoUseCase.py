from domain.entities.Endereco import ProfissionalPossuiEndereco
import pytest
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from sqlalchemy.orm import Session
from unittest.mock import MagicMock
from application.useCases.EnderecoUseCase import EnderecoUseCase
from infrastructure.repositories.EnderecoRepository import EnderecoRepository
from domain.entities.Endereco import Endereco


test_session = UnifiedAlchemyMagicMock()


def get_mock_db_session():
    """Callable do db em mock para o repository"""
    return test_session


EnderecoRepo = EnderecoRepository(session=get_mock_db_session)
enderecoUseCase = EnderecoUseCase(
    enderecoRepository=EnderecoRepo,
)

 
from domain.entities.Profissional import Profissional

test_list = [
    (Endereco(
        idEndereco =1,
        cep = '72001654',
        estado = 'RJ',
        cidade = 'Rio de Janeiro',
        bairro = 'Copacabana',
        numero = '505',
        complemento = 'Avenida Getúlio Vargas',
    )),
    (Endereco(
        idEndereco =2,
        cep = '730046456',
        estado = 'SC',
        cidade = 'Tubarão',
        bairro = 'Santa Lúcia',
        numero = '509',
        complemento = 'Residencial Costa',
    ))
]


@pytest.mark.parametrize(
    "endereco_sent",
    test_list,
)
def testSaveEndereco(endereco_sent):
    """Testa se o Endereco é salvo com sucesso, assume que sempre recebe um Endereco válido"""
    response = enderecoUseCase.save(enderecoSent=endereco_sent)
    assert endereco_sent == response, response.__dict__



def testEnderecoFindAllCadastradas():
    response = enderecoUseCase.find_all()
    response = [r.__dict__ for r in response]
    sorted_response = sorted(response, key=lambda x: x['idEndereco'])
    #print(sorted_response)

    expected = [r.__dict__ for r in test_list]
    sorted_expected = sorted(expected, key=lambda x: x['idEndereco'])
    #print(sorted_expected)

    assert len(response) == len(test_list), response