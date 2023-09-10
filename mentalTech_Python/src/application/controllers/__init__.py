from infrastructure.repositories.PessoaRepository import PessoaRepository
from application.useCases.PessoaUseCase import PessoaUseCase

from database import SessionLocal

databaseSessionGenerator = SessionLocal


pessoaRepository = PessoaRepository(databaseSessionGenerator)
pessoaUseCase = PessoaUseCase(
    pessoaRepository=pessoaRepository
)