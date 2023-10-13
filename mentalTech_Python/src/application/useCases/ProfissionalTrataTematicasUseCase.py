from domain.entities.TematicasPrincipais import ProfissionalTrataTematicas
from domain.repositories.ProfissionalTrataTematicasBaseModel import ProfissionalTrataTematicasBaseModel


class ProfissionalTrataTematicasUseCase():
    __profissionalTrataTematicas__: ProfissionalTrataTematicasBaseModel
    

    def __init__(
        self,
        profissionalTrataTematicasRepository: ProfissionalTrataTematicasBaseModel
    ):
        self.__profissionalTrataTematicas__ = profissionalTrataTematicasRepository

    def save(self, profissionalTrataTematicasSent: ProfissionalTrataTematicas) -> ProfissionalTrataTematicas:

        return self.__profissionalTrataTematicas__.save(profissionalTrataTematicasSent=profissionalTrataTematicasSent)

    def delete(self, cpf: str, idTematicasPrincipais: int) -> None:
        return self.__profissionalTrataTematicas__.delete(cpf=cpf, idTematicasPrincipais= idTematicasPrincipais)


    def find_by_cpfProfissional(self, cpf : str) -> ProfissionalTrataTematicas | None:
        return self.__profissionalTrataTematicas__.find_by_cpfProfissional(cpf=cpf)
    



