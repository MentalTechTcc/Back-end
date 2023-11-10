import pytest
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from application.useCases.EspecialidadeUseCase import EspecialidadeUseCase
from infrastructure.repositories.EspecialidadeRepository import EspecialidadeRepository
from domain.entities.Especialidade import Especialidade, EspecialidadeRequestId, EspecialidadeResponse
from sqlalchemy.orm import Session
from unittest.mock import MagicMock

test_session = UnifiedAlchemyMagicMock()


def get_mock_db_session():
    """Callable do db em mock para o repository"""
    return test_session


especialidadeRepo = EspecialidadeRepository(session=get_mock_db_session)
especialidadeUseCase = EspecialidadeUseCase(
    especialidadeRepository=especialidadeRepo,
)

test_list = [
    (EspecialidadeRequestId(
        descricaoEspecialidade="Cardiologia",
        idEspecialidade=1,
    )),
    (EspecialidadeRequestId(
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
    assert especialidade_sent.dict() == response.dict(), response.dict()


# def testEspecialidadeFindAll():
#     response = especialidadeUseCase.find_all()
#     response_ids = sorted([r.idEspecialidade for r in response])

#     expected_ids = sorted([r.idEspecialidade for r in test_list])

#     assert response_ids == expected_ids, response_ids
