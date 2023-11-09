from application.useCases.AvaliacaoUseCase import AvaliacaoUseCase
from infrastructure.repositories.AvaliacaoRepository import AvaliacaoRepository 
from domain.entities.Avaliacao import Avaliacao
from sqlalchemy.orm import Session
from unittest.mock import MagicMock
import pytest
from mock_alchemy.mocking import UnifiedAlchemyMagicMock


test_session = UnifiedAlchemyMagicMock()


def get_mock_db_session():
    """Callable do db em mock para o repository"""
    return test_session


avaliacaoRepo = AvaliacaoRepository(session=get_mock_db_session)
avaliacaoUseCase = AvaliacaoUseCase(
    avaliacaoRepository=avaliacaoRepo,
)


test_list = [
    (Avaliacao(
        idAvaliacao=1,
        cpfProfissional="86778022078",
        idPessoa=1,
        notaGeral= 10,
        notaPontualidade= 9,
        notaAtendimento= 8,
        observacoes= 'Muito boa',
        dataCadastro='2023-11-09',
    )),
    (Avaliacao(
        idAvaliacao=2,
        cpfProfissional="86778022078",
        idPessoa=2,
        notaGeral= 8,
        notaPontualidade= 7,
        notaAtendimento= 8,
        observacoes= 'Muito Pontual',
        dataCadastro='2023-11-09',
    )),
    (Avaliacao(
        idAvaliacao=3,
        cpfProfissional="86778022078",
        idPessoa=3,
        notaGeral= 6,
        notaPontualidade= 8,
        notaAtendimento= 9,
        observacoes= 'Excelente, mas estava com a conexão ruim',
        dataCadastro='2023-11-09',
        )   ),
]


@pytest.mark.parametrize(
    "avaliacao_sent",
    test_list,
)
def testSaveAvaliacaoValido(avaliacao_sent):
    """Testa se o avaliacao é salvo com sucesso, assume que sempre recebe um avaliacao válido"""
    response = avaliacaoUseCase.save(avaliacaoSent=avaliacao_sent)
    assert avaliacao_sent == response, response.__dict__


def testAvaliacaoFindAllCadastrados():
    response = avaliacaoUseCase.find_all()
    response = [r.__dict__ for r in response]
    sorted_response = sorted(response, key=lambda x: x['idAvaliacao'])
    print(sorted_response)

    expected = [r.__dict__ for r in test_list]
    sorted_expected = sorted(expected, key=lambda x: x['idAvaliacao'])
    print(sorted_expected)

    assert len(response) == len(test_list), response