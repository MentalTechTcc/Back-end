import pytest
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from application.useCases.EspecialidadeUseCase import EspecialidadeUseCase
from infrastructure.repositories.EspecialidadeRepository import EspecialidadeRepository
from domain.entities.Especialidade import Especialidade, EspecialidadeRequestId, EspecialidadeResponse
from sqlalchemy.orm import Session
from unittest.mock import MagicMock
from domain.entities.Profissional import Profissional

from domain.entities.TematicasPrincipais import TematicasPrincipais

test_session = UnifiedAlchemyMagicMock()


def get_mock_db_session():
    """Callable do db em mock para o repository"""
    return test_session


especialidadeRepo = EspecialidadeRepository(session=get_mock_db_session)
especialidadeUseCase = EspecialidadeUseCase(
    especialidadeRepository=especialidadeRepo,
)

test_list = [
    (Especialidade(
        descricaoEspecialidade="Cardiologia",
        idEspecialidade=1,
    )),
    (Especialidade(
        descricaoEspecialidade="Ortopedia",
        idEspecialidade=2,
    ))
]

@pytest.mark.parametrize(
    "especialidade_sent",
    test_list,
)
def testSaveEspecialidadeValida(especialidade_sent):
    """Testa se a especialidade é salva com sucesso, assume que sempre recebe uma especialidade válida"""
    response = especialidadeUseCase.save(especialidadeSent=especialidade_sent)
    assert especialidade_sent == response, response.__dict__



def testEspecialidadeFindAll():
    response = especialidadeUseCase.find_all()
    response = [r.__dict__ for r in response]
    sorted_response = sorted(response, key=lambda x: x['idEspecialidade'])
    #print(sorted_response)

    expected = [r.__dict__ for r in test_list]
    sorted_expected = sorted(expected, key=lambda x: x['idEspecialidade'])
    #print(sorted_expected)

    assert len(response) == len(test_list), response
