import pytest
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from sqlalchemy.orm import Session
from application.useCases.ProfissionalUseCase import ProfissionalUseCase
from infrastructure.repositories.ProfissionalRepository import ProfissionalRepository
from infrastructure.repositories.TokenRepository import TokensRepository
from domain.entities.Profissional import Profissional, ProfissionalRequestId, ProfissionalResponse
from domain.repositories.ProfissionalRepositoryBaseModel import ProfissionalRepositoryBaseModel
from domain.entities.Pessoa import Sexo

test_session = UnifiedAlchemyMagicMock()


def get_mock_db_session():
    """Callable do db em mock para o repository"""
    return test_session


profissionalRepo = ProfissionalRepository(session=get_mock_db_session)
tokenRepo = TokensRepository()  # Instancie o TokenRepository
profissionalUseCase = ProfissionalUseCase(
    profissionalRepository=profissionalRepo,
    tokensRepository=tokenRepo
)



from domain.entities.Profissional import Profissional

test_list = [
    (Profissional(
        nome="João",
        idPessoa=1,
        senha="senha123",
        dataNascimento="1990-01-01",
        telefone="123456789",
        email="joao@example.com",
        sexo=Sexo.M,
        administrador=False,
        cpf="12345678901",
        codigoProfissional="ABC123",
        descricaoProfissional="Médico",
        pix="pix123",
        imagem=b'',
    )),
]

@pytest.mark.parametrize(
    "profissional_sent",
    test_list,
)
def test_save_profissional_valido(profissional_sent):
    """Testa se o profissional é salvo com sucesso, assume que sempre recebe um profissional válido"""
    response = profissionalUseCase.save(profissionalSent=profissional_sent)
    assert profissional_sent == response, response.__dict__


def testProfissionalFindAll():
    response = profissionalUseCase.find_all()
    response = [r.__dict__ for r in response]
    sorted_response = sorted(response, key=lambda x: x['idPessoa'])
    #print(sorted_response)

    expected = [r.__dict__ for r in test_list]
    sorted_expected = sorted(expected, key=lambda x: x['idPessoa'])
    #print(sorted_expected)

    assert len(response) == len(test_list), response
