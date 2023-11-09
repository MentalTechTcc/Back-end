from application.useCases.AgendaUseCase import AgendaUseCase
from infrastructure.repositories.AgendaRepository import AgendaRepository 
from domain.entities.Agenda import Agenda, Modalidade
from sqlalchemy.orm import Session
from unittest.mock import MagicMock
import pytest
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from datetime import date, time


test_session = UnifiedAlchemyMagicMock()


def get_mock_db_session():
    """Callable do db em mock para o repository"""
    return test_session


agendaRepo = AgendaRepository(session=get_mock_db_session)
agendaUseCase = AgendaUseCase(
    agendaRepository=agendaRepo,
)


test_list = [
    (Agenda(
        idAgenda=1,
        data=date(2023, 11, 9),
        hora=time(10, 0),
        duracao=60,
        cpfProfissional="86778022078",
        modalidadeAtendimento=Modalidade.PRESENCIAL,
        ocupado=False,
        valorProposto=50.0,
        linkPagamento="https://pagamento.com",
        idEndereco=1,
    )),
    (Agenda(
        idAgenda=2,
        data=date(2023, 11, 10),
        hora=time(14, 30),
        duracao=45,
        cpfProfissional="86778022078",
        modalidadeAtendimento=Modalidade.ONLINE,
        ocupado=True,
        valorProposto=40.0,
        linkPagamento=None,
        idEndereco=2,
    )),
]

@pytest.mark.parametrize(
    "agenda_sent",
    test_list,
)
def testSaveAgendaValido(agenda_sent):
    """Testa se a agenda é salva com sucesso, assume que sempre recebe uma agenda válida"""
    response = agendaUseCase.save(agendaSent=agenda_sent)
    assert agenda_sent == response, response.__dict__


def testAgendaFindAll():
    response = agendaUseCase.find_all()
    response = [r.__dict__ for r in response]
    sorted_response = sorted(response, key=lambda x: x['idAgenda'])
    print(sorted_response)

    expected = [r.__dict__ for r in test_list]
    sorted_expected = sorted(expected, key=lambda x: x['idAgenda'])
    print(sorted_expected)

    assert len(response) == len(test_list), response 