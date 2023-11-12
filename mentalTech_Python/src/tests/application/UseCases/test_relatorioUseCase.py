from domain.entities.Pessoa import Sexo
from domain.entities.Especialidade import ProfissionalPossuiEspecialidade
import pytest
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from sqlalchemy.orm import Session
from unittest.mock import MagicMock
from application.useCases.RelatorioUseCase import RelatorioUseCase
from infrastructure.repositories.RelatorioRepository import RelatorioRepository
from domain.entities.Relatorio import Relatorio, RelatorioResponse
from domain.entities.Profissional import Profissional

test_session = UnifiedAlchemyMagicMock()


def get_mock_db_session():
    """Callable do db em mock para o repository"""
    return test_session


RelatorioRepo = RelatorioRepository(session=get_mock_db_session)
relatorioUseCase = RelatorioUseCase(
    relatorioRepository=RelatorioRepo,
)

 
from domain.entities.Profissional import Profissional

from domain.entities.TematicasPrincipais import TematicasPrincipais

test_list = [
    (Relatorio(
        descricao= 'Paciente relata melhora após inciar tratamento.',
        idConsulta= 1,
        dataCadastro= '2023-11-12', 
        idRelatorio=1,
    )),
    (Relatorio(
        descricao= 'Paciente está sofrendo com ansiedade severa.',
        idConsulta= 2,
        dataCadastro= '2023-11-13', 
        idRelatorio=2,
    ))
]

@pytest.mark.parametrize(
    "relatorio_sent",
    test_list,
)
def testSaveRelatorioValido(relatorio_sent):
    """Testa se o Relatorio é salvo com sucesso, assume que sempre recebe um Relatorio válido"""
    response = relatorioUseCase.save(relatorioSent=relatorio_sent)
    assert relatorio_sent == response, response.__dict__



def testRelatorioFindAllCadastrados():
    response = relatorioUseCase.find_all()
    response = [r.__dict__ for r in response]
    sorted_response = sorted(response, key=lambda x: x['idRelatorio'])
    #print(sorted_response)

    expected = [r.__dict__ for r in test_list]
    sorted_expected = sorted(expected, key=lambda x: x['idRelatorio'])
    #print(sorted_expected)

    assert len(response) == len(test_list), response