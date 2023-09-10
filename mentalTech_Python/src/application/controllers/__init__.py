from infrastructure.repositories.PessoaRepository import PessoaRepository
from application.useCases.PessoaUseCase import PessoaUseCase
from infrastructure.repositories.TokenRepository import TokensRepository

from database import SessionLocal

databaseSessionGenerator = SessionLocal
tokensRepository = TokensRepository()


pessoaRepository = PessoaRepository(databaseSessionGenerator)
pessoaUseCase = PessoaUseCase(
    pessoaRepository=pessoaRepository,
    tokensRepository=tokensRepository
)