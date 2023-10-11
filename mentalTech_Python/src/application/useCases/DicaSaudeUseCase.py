from domain.entities.DicaSaude import DicaSaude, DicaSaudeResponse, DicaSaudeBase, DicaSaudeRequestId
from domain.repositories.DicaSaudeRepositoryBaseModel import DicaSaudeRepositoryBaseModel
from .ValidacaoCamposUseCase import ValidacaoCamposUseCase
from typing import NoReturn

class DicaSaudeUseCase():
    __dicaSaudeRepository__: DicaSaudeRepositoryBaseModel
    

    def __init__(
        self,
        dicaSaudeRepository: DicaSaudeRepositoryBaseModel
    ):
        self.__dicaSaudeRepository__ = dicaSaudeRepository

    def save(self, dicaSaudeSent: DicaSaude) -> DicaSaude:

        return self.__dicaSaudeRepository__.save(dicaSaudeSent=dicaSaudeSent)

    def delete_by_id(self, dicaSaude_id: int) -> None:
        return self.__dicaSaudeRepository__.delete_by_id(dicaSaude_id=dicaSaude_id)


    def find_all(self) -> list[DicaSaudeResponse]:
        dicaSaude_db = self.__dicaSaudeRepository__.find_all()
        dicaSaudes = []
        for dicaSaude_db in dicaSaude_db:
            dicaSaude = DicaSaudeResponse(
                idDicaSaude =  dicaSaude_db.idDicaSaude,
                descricaoDica=dicaSaude_db.descricaoDica,
                cpfProfissional= dicaSaude_db.cpfProfissional,
                dataCadastro= dicaSaude_db.dataCadastro
            )
            dicaSaudes.append(dicaSaude)
        return dicaSaudes

    def find_by_id(self, dicaSaude_id : int) -> DicaSaudeBase | None:
        return self.__dicaSaudeRepository__.find_by_id(dicaSaude_id=dicaSaude_id)
    

    def update(self, dicaSaudeSent: DicaSaudeRequestId) -> NoReturn:
        """Sobrescreve os dados de dicaSaude, assume que ele já exista"""
        self.__dicaSaudeRepository__.update(DicaSaude(**dicaSaudeSent.__dict__))

    def valida_dica_create(self, dica: DicaSaude) -> dict:

        fieldInfoDict = {}
        fieldInfoDict["descricaoDica"] = vars(ValidacaoCamposUseCase.descricaoDicaValidation(
            dica.descricaoDica))
        completeStatus = True
        for key in fieldInfoDict:
            if fieldInfoDict[key]['status'] == False:
                completeStatus = False
                break
        fieldInfoDict['completeStatus'] = completeStatus

        return fieldInfoDict
