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
from src.application.useCases.RelatorioUseCase import RelatorioUseCase
from src.infrastructure.repositories.RelatorioRepository import RelatorioRepository
from src.application.useCases.EnderecoUseCase import EnderecoUseCase
from src.infrastructure.repositories.EnderecoRepository import EnderecoRepository
from src.application.useCases.EspecialidadeUseCase import EspecialidadeUseCase
from src.infrastructure.repositories.EspecialidadeRepository import EspecialidadeRepository 

from src.application.useCases.TematicasPrincipaisUseCase import TematicasPrincipaisUseCase
from src.infrastructure.repositories.TematicasPrincipaisRepository import TematicasPrincipaisRepository

from src.application.useCases.DicaSaudeUseCase import DicaSaudeUseCase
from src.infrastructure.repositories.DicaSaudeRepository import DicaSaudeRepository

from src.application.useCases.AvaliacaoUseCase import AvaliacaoUseCase
from src.infrastructure.repositories.AvaliacaoRepository import AvaliacaoRepository

from src.application.useCases.DiagnosticoUseCase import DiagnosticoUseCase
from src.infrastructure.repositories.DiagnosticoRepository import DiagnosticoRepository

from src.application.useCases.PessoaPossuiDiagnosticoUseCase import PessoaPossuiDiagnosticoUseCase
from src.infrastructure.repositories.PessoaPossuiDiagnosticoRepository import PessoaPossuiDiagnosticoRepository

from src.application.useCases.ProfissionalPossuiEnderecoUseCase import ProfissionalPossuiEnderecoUseCase
from src.infrastructure.repositories.ProfissionalPossuiEnderecoRepository import ProfissionalPossuiEnderecoRepository

from src.application.useCases.ProfissionalPossuiEspecialidadeUseCase import ProfissionalPossuiEspecialidadeUseCase
from src.infrastructure.repositories.ProfissionalPossuiEspecialidadeRepository import ProfissionalPossuiEspecialidadeRepository

from src.application.useCases.ProfissionalTrataTematicasUseCase import ProfissionalTrataTematicasUseCase
from src.infrastructure.repositories.ProfissionalTrataTematicasRepository import ProfissionalTrataTematicasRepository

from src.application.useCases.ResetSenhaUseCase import ResetSenhaUseCase


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

relatorioRepository = RelatorioRepository(databaseSessionGenerator)
relatorioUseCase = RelatorioUseCase(
    relatorioRepository=relatorioRepository
)

tematicasPrincipaisRepository = TematicasPrincipaisRepository(databaseSessionGenerator)
tematicasPrincipaisUseCase = TematicasPrincipaisUseCase(
    tematicasPrincipaisRepository=tematicasPrincipaisRepository
)

enderecoRepository = EnderecoRepository(databaseSessionGenerator)
enderecoUseCase = EnderecoUseCase(
    enderecoRepository=enderecoRepository
)

especialidadeRepository = EspecialidadeRepository(databaseSessionGenerator)
especialidadeUseCase = EspecialidadeUseCase(
    especialidadeRepository=especialidadeRepository
)

dicaSaudeRepository = DicaSaudeRepository(databaseSessionGenerator)
dicaSaudeUseCase = DicaSaudeUseCase(
    dicaSaudeRepository=dicaSaudeRepository
)

avaliacaoRepository = AvaliacaoRepository(databaseSessionGenerator)
avaliacaoUseCase = AvaliacaoUseCase(
    avaliacaoRepository=avaliacaoRepository
)

diagnosticoRepository = DiagnosticoRepository(databaseSessionGenerator)
diagnosticoUseCase = DiagnosticoUseCase(
    diagnosticoRepository=diagnosticoRepository
)

pessoaPossuiDiagnosticoRepository = PessoaPossuiDiagnosticoRepository(databaseSessionGenerator)
pessoaPossuiDiagnosticoUseCase = PessoaPossuiDiagnosticoUseCase(
    pessoaPossuiDiagnosticoRepository=pessoaPossuiDiagnosticoRepository
)


profissionalPossuiEnderecoRepository = ProfissionalPossuiEnderecoRepository(databaseSessionGenerator)
profissionalPossuiEnderecoUseCase = ProfissionalPossuiEnderecoUseCase(
    profissionalPossuiEnderecoRepository=profissionalPossuiEnderecoRepository
)

profissionalPossuiEspecialidadeRepository = ProfissionalPossuiEspecialidadeRepository(databaseSessionGenerator)
profissionalPossuiEspecialidadeUseCase = ProfissionalPossuiEspecialidadeUseCase(
    profissionalPossuiEspecialidadeRepository=profissionalPossuiEspecialidadeRepository
)


profissionalTrataTematicasRepository = ProfissionalTrataTematicasRepository(databaseSessionGenerator)
profissionalTrataTematicasUseCase = ProfissionalTrataTematicasUseCase(
    profissionalTrataTematicasRepository=profissionalTrataTematicasRepository
)


resetSenhaUseCase = ResetSenhaUseCase(
    pessoaRepository = pessoaRepository,
    professionalRepository=profissionalRepository
)