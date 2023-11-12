from application.useCases.DicaSaudeUseCase import DicaSaudeUseCase
from infrastructure.repositories.DicaSaudeRepository import DicaSaudeRepository 
from domain.entities.DicaSaude import DicaSaude
from sqlalchemy.orm import Session
from unittest.mock import MagicMock
import pytest
from mock_alchemy.mocking import UnifiedAlchemyMagicMock


test_session = UnifiedAlchemyMagicMock()


def get_mock_db_session():
    """Callable do db em mock para o repository"""
    return test_session


dicaSaudeRepo = DicaSaudeRepository(session=get_mock_db_session)
dicaSaudeUseCase = DicaSaudeUseCase(
    dicaSaudeRepository=dicaSaudeRepo,
)


test_list = [
    (DicaSaude(
        idDicaSaude=1,
        descricaoDica="Beba bastante água",
        cpfProfissional="86778022078",
        dataCadastro='2023-11-09',
    )),
    (DicaSaude(
        idDicaSaude=2,
        descricaoDica="Corra 2k por dia",
        cpfProfissional="86778022078",
        dataCadastro='2023-11-09',
    )),
    (DicaSaude(
        idDicaSaude=3,
        descricaoDica="Coma saudável",
        cpfProfissional="86778022078",
        dataCadastro='2023-11-09',
        )   ),
    (DicaSaude(
        idDicaSaude=4,
        descricaoDica="Leia bastante",
        cpfProfissional="86778022078",
        dataCadastro='2023-11-09',
    )),
    (DicaSaude(
        idDicaSaude=5,
        descricaoDica="Se precisar de ajuda se consulte",
        cpfProfissional="86778022078",
        dataCadastro='2023-11-09',
    )),
]


@pytest.mark.parametrize(
    "dicaSaude_sent",
    test_list,
)
def testSaveDicaSaudeValido(dicaSaude_sent):
    """Testa se o dicaSaude é salvo com sucesso, assume que sempre recebe um dicaSaude válido"""
    response = dicaSaudeUseCase.save(dicaSaudeSent=dicaSaude_sent)
    assert dicaSaude_sent == response, response.__dict__


def testDicaSaudeFindAllCadastrados():
    response = dicaSaudeUseCase.find_all()
    response = [r.__dict__ for r in response]
    sorted_response = sorted(response, key=lambda x: x['idDicaSaude'])
    #print(sorted_response)

    expected = [r.__dict__ for r in test_list]
    sorted_expected = sorted(expected, key=lambda x: x['idDicaSaude'])
    #print(sorted_expected)

    assert len(response) == len(test_list), response