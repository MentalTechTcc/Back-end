from infrastructure.repositories.PessoaRepository import PessoaRepository
from application.useCases.PessoaUseCase import PessoaUseCase
from infrastructure.repositories.TokenRepository import TokensRepository
from infrastructure.repositories.ConsultaRepository import ConsultaRepository
from src.application.useCases.ConsultaUseCase import ConsultaUseCase
from database import SessionLocal
from src.application.useCases.ProfissionalUseCase import ProfissionalUseCase
from src.infrastructure.repositories.ProfissionalRepository import ProfissionalRepository
from src.application.useCases.AgendaUseCase import AgendaUseCase
from src.infrastructure.repositories.AgendaRepository import AgendaRepository




databaseSessionGenerator = SessionLocal
tokensRepository = TokensRepository()


pessoaRepository = PessoaRepository(databaseSessionGenerator)
pessoaUseCase = PessoaUseCase(
    pessoaRepository=pessoaRepository,
    tokensRepository=tokensRepository
)

profissionalRepository = ProfissionalRepository(databaseSessionGenerator)
profissionalUseCase = ProfissionalUseCase(
    profissionalRepository=profissionalRepository,
    tokensRepository=tokensRepository
)

consultaRepository = ConsultaRepository(databaseSessionGenerator)
consultaUseCase = ConsultaUseCase(
    consultaRepository=consultaRepository
)

consultaRepository = ConsultaRepository(databaseSessionGenerator)
consultaUseCase = ConsultaUseCase(
    consultaRepository=consultaRepository
)

agendaRepository = AgendaRepository(databaseSessionGenerator)
agendaUseCase = AgendaUseCase(
    agendaRepository=agendaRepository
)