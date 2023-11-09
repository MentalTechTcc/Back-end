import pytest
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from sqlalchemy.orm import Session
from unittest.mock import MagicMock
from application.useCases.ConsultaUseCase import ConsultaUseCase
from infrastructure.repositories.ConsultaRepository import ConsultaRepository
from domain.entities.Consulta import Consulta

test_session = UnifiedAlchemyMagicMock()


def get_mock_db_session():
    """Callable do db em mock para o repository"""
    return test_session


consultaRepo = ConsultaRepository(session=get_mock_db_session)
consultaUseCase = ConsultaUseCase(
    consultaRepository=consultaRepo,
)

test_list = [
    (Consulta(
        idConsulta=1,
        valor=100.0,
        idAgenda=1,
        idPessoa=1,
        permiteCompartilharConhecimento=True,
        ocorreu=True,
    )),
    (Consulta(
        idConsulta=2,
        valor=150.0,
        idAgenda=2,
        idPessoa=2,
        permiteCompartilharConhecimento=False,
        ocorreu=False,
    )),
    (Consulta(
        idConsulta=3,
        valor=120.0,
        idAgenda=3,
        idPessoa=3,
        permiteCompartilharConhecimento=True,
        ocorreu=True,
    )),
    # Adicione mais instâncias conforme necessário
]

@pytest.mark.parametrize(
    "consulta_sent",
    test_list,
)
def testSaveConsultaValido(consulta_sent):
    """Testa se a consulta é salva com sucesso, assume que sempre recebe uma consulta válida"""
    response = consultaUseCase.save(consultaSent=consulta_sent)
    assert consulta_sent == response, response.__dict__


def testConsultaFindAll():
    response = consultaUseCase.find_all()
    response = [r.__dict__ for r in response]
    sorted_response = sorted(response, key=lambda x: x['idConsulta'])
    print(sorted_response)

    expected = [r.__dict__ for r in test_list]
    sorted_expected = sorted(expected, key=lambda x: x['idConsulta'])
    print(sorted_expected)

    assert len(response) == len(test_list), response 