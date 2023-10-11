from dataclasses import dataclass
from datetime import datetime
from enum import Enum
import re
from datetime import date


@dataclass
class CampoInfo:
    """Classe para armazenar informações sobre os campos de um modelo"""
    status: bool
    detail: str


class ValidacaoCamposUseCase:
    """Validação quanto ao formato dos dados (não valida lógicas de negócio))"""
    @classmethod
    def nomeValidation(cls, nome: str) -> CampoInfo:
        if len(nome) > 200:
            return CampoInfo(False, "Nome muito grande")
        elif len(nome) == 0:
            return CampoInfo(False, "Nome não pode ser vazio")
        return CampoInfo(True, "Nome válido")

    @classmethod
    def dNascimentoValidation(cls, dNascimento: date) -> CampoInfo:
        if isinstance(dNascimento, date):
            # Se 'dNascimento' é um objeto 'date', não há necessidade de validação adicional.
            return CampoInfo(True, "Data de nascimento válida")
        
        if isinstance(dNascimento, str):
            try:
                dNascimento = date.fromisoformat(dNascimento)
                # A data está no formato 'YYYY-MM-DD' e foi convertida com sucesso.
                return CampoInfo(True, "Data de nascimento válida")
            except ValueError as e:
                return CampoInfo(False, f"Data de nascimento inválida ({e})")
        
        return CampoInfo(False, "Tipo de dado inválido para data de nascimento")

    @classmethod
    def cpfValidation(cls, cpf: str) -> CampoInfo:
        if len(cpf) > 11:
            return CampoInfo(False, "CPF muito grande")

        pattern = r'^\d{11}$'
        if not re.match(pattern, cpf):
            return CampoInfo(False, "Formato CPF inválido")

        if cpf == cpf[0]*11:
            return CampoInfo(False, "CPF inválido")

        sum0 = sum([int(cpf[i])*(10-i) for i in range(9)])
        rest = (sum0*10) % 11
        if rest != 10 and rest != int(cpf[9]):
            return CampoInfo(False, "CPF inválido")

        sum0 = sum([int(cpf[i])*(11-i) for i in range(10)])
        rest = (sum0*10) % 11
        if rest != 10 and rest != int(cpf[10]):
            return CampoInfo(False, "CPF inválido")

        return CampoInfo(True, "CPF válido")

    @classmethod
    def telefoneValidation(cls, telefone: str) -> CampoInfo:
        if len(telefone) > 11:
            return CampoInfo(False, "Telefone muito grande")

        pattern = r'^\d{11}$'
        if not re.match(pattern, telefone):
            return CampoInfo(False, "Telefone inválido")

        return CampoInfo(True, "Telefone válido")

    @classmethod
    def emailValidation(cls, email: str) -> CampoInfo:
        if len(email) > 100:
            return CampoInfo(False, "Email muito grande")

        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(pattern, email):
            return CampoInfo(False, "Email inválido")

        return CampoInfo(True, "Email válido")

    @classmethod
    def senhaValidation(cls, senha: str) -> CampoInfo:
        if len(senha) < 8:
            return CampoInfo(False, "Senha muito pequena")
        if len(senha) > 200:
            return CampoInfo(False, "Senha muito grande")

        return CampoInfo(True, "Senha válida")

    @classmethod
    def descricaoProfissionalValidation(cls, descricao: str) -> CampoInfo:
        if len(descricao) > 500:
            return CampoInfo(False, "Descricao muito grande")

        return CampoInfo(True, "Senha válida")

    @classmethod
    def observacaoValidation(cls, observacao: str) -> CampoInfo:
        if len(observacao) > 200:
            return CampoInfo(False, "Observação muito grande")

        return CampoInfo(True, "Observação válida")

    @classmethod
    def loginValidation(cls, login: str) -> CampoInfo:
        if len(login) < 8:
            return CampoInfo(False, "Login muito pequeno")

        return CampoInfo(True, "Login válido")
    
    @classmethod
    def codigoProfissionalValidation(cls, status: Enum):
        if status.value < 1 or status.value > 3:
            return CampoInfo(False, "Código inválido")
        
        return CampoInfo(True, "Status válido")
    
    @classmethod
    def cepValidation(cls, cep : str):
        if len(cep) > 8:
            return CampoInfo(False, "CEP muito grande")
        
        pattern = r'^\d{8}$'
        if not re.match(pattern, cep):
            return CampoInfo(False, "Formato de CEP inválido")
        
        return CampoInfo(True, "CEP válido")
    
    @classmethod
    def bairroValidation(cls, bairro : str):
        if len(bairro) > 100:
            return CampoInfo(False, "Bairro muito grande")
        
        return CampoInfo(True, "Bairro válido")
    
    @classmethod
    def cidadeValidation(cls, cidade : str):
        if len(cidade) > 100:
            return CampoInfo(False, "Cidade muito grande")
        
        return CampoInfo(True, "Cidade válida")
    
    @classmethod
    def descricaoValidation(cls, descricao:str):
        if len(descricao) > 100:
            return CampoInfo(False,"Descrição muito grande")
        return CampoInfo(True,"Descrição válida")
    

    @classmethod
    def notaValidation(cls, nota:int):
        if nota<0 or nota>10:
            return CampoInfo(False,"Nota inválida")
        return CampoInfo(True,"Nota válida")
        
    @classmethod
    def observacaoValidation(cls, observacao:str):
        if len(observacao)> 500:
            return CampoInfo(False,"Observação inválida")
        return CampoInfo(True,"Observação válida")
    
    @classmethod
    def descricaoDiagnosticoValidation(cls, descricao:str):
        if len(descricao) > 250:
            return CampoInfo(False,"Descrição diagnóstico inválida")
        return CampoInfo(True,"Descrição diagnóstico válida")
    
    @classmethod
    def descricaoDicaValidation(cls, descricao:str):
        if len(descricao) > 500:
            return CampoInfo(False,"Descrição de dica inválida")
        return CampoInfo(True,"Descrição de dica válida")
    
    @classmethod
    def descricaoTematicaValidation(cls, tematica:str):
        if len(tematica) > 250:
            return CampoInfo(False,"Temática inválida")
        return CampoInfo(True,"Temática válida")
    
    @classmethod
    def valorValidation(cls, valor:float):
        if valor<0:
            return CampoInfo(False,"Valor inválido")
        return CampoInfo(True,"Valor válido")
    