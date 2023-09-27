from domain.entities.Diagnostico import PessoaPossuiDiagnostico
from domain.repositories.PessoaPossuiDiagnosticoBaseModel import pessoaPossuiDiagnosticoRepositoryBaseModel
from security import verify_password


class PessoaPossuiDiagnosticoUseCase():
    __pessoaPossuiDiagnostico__: pessoaPossuiDiagnosticoRepositoryBaseModel
    

    def __init__(
        self,
        pessoaPossuiDiagnosticoRepository: pessoaPossuiDiagnosticoRepositoryBaseModel
    ):
        self.__pessoaPossuiDiagnostico__ = pessoaPossuiDiagnosticoRepository

    def save(self, pessoaPossuiDiagnosticoSent: PessoaPossuiDiagnostico) -> PessoaPossuiDiagnostico:

        return self.__pessoaPossuiDiagnostico__.save(pessoaPossuiDiagnosticoSent=pessoaPossuiDiagnosticoSent)

    def delete(self, pessoaId: int, diagnosticoId: int, profissionalCpf: str) -> None:
        return self.__pessoaPossuiDiagnostico__.delete(pessoaId=pessoaId, diagnosticoId= diagnosticoId,profissionalCpf=profissionalCpf )


    def find_by_pessoaId(self, pessoa_id : int) -> PessoaPossuiDiagnostico | None:
        return self.__pessoaPossuiDiagnostico__.find_by_idPessoa(pessoa_id=pessoa_id)
    



