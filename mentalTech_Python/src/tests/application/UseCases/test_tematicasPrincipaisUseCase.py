from domain.entities.Especialidade import ProfissionalPossuiEspecialidade
import pytest
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from sqlalchemy.orm import Session
from unittest.mock import MagicMock
from application.useCases.TematicasPrincipaisUseCase import TematicasPrincipaisUseCase
from infrastructure.repositories.TematicasPrincipaisRepository import TematicasPrincipaisRepository
from domain.entities.TematicasPrincipais import TematicasPrincipais


test_session = UnifiedAlchemyMagicMock()


def get_mock_db_session():
    """Callable do db em mock para o repository"""
    return test_session


TematicasPrincipaisRepo = TematicasPrincipaisRepository(session=get_mock_db_session)
tematicasPrincipaisUseCase = TematicasPrincipaisUseCase(
    tematicasPrincipaisRepository=TematicasPrincipaisRepo,
)

 
from domain.entities.Profissional import Profissional

test_list = [
    (TematicasPrincipais(
        nomeTematica= 'Terapia Familiar',
        idTematicasPrincipais=1,
    )),
    (TematicasPrincipais(
        nomeTematica= 'Ansiedade',
        idTematicasPrincipais=2,
    ))
]

@pytest.mark.parametrize(
    "tematicasPrincipais_sent",
    test_list,
)
def testSaveTematicasPrincipais(tematicasPrincipais_sent):
    """Testa se o TematicasPrincipais é salvo com sucesso, assume que sempre recebe um TematicasPrincipais válido"""
    response = tematicasPrincipaisUseCase.save(tematicasPrincipaisSent=tematicasPrincipais_sent)
    assert tematicasPrincipais_sent == response, response.__dict__



def testTematicasPrincipaisFindAllCadastradas():
    response = tematicasPrincipaisUseCase.find_all()
    response = [r.__dict__ for r in response]
    sorted_response = sorted(response, key=lambda x: x['idTematicasPrincipais'])
    #print(sorted_response)

    expected = [r.__dict__ for r in test_list]
    sorted_expected = sorted(expected, key=lambda x: x['idTematicasPrincipais'])
    #print(sorted_expected)

    assert len(response) == len(test_list), response