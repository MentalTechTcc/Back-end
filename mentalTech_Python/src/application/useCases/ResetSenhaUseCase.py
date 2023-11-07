from domain.repositories.PessoaRepositoryBaseModel import PessoaRepositoryBaseModel
from domain.repositories.ProfissionalRepositoryBaseModel import ProfissionalRepositoryBaseModel
from email.mime.text import MIMEText
import smtplib
import ssl


class ResetSenhaUseCase():
    __pessoaRepository__: PessoaRepositoryBaseModel
    __profissionalRepository__: ProfissionalRepositoryBaseModel

    def __init__(
        self,
        pessoaRepository: PessoaRepositoryBaseModel,
        professionalRepository: ProfissionalRepositoryBaseModel
    ):
        self.__pessoaRepository__ = pessoaRepository
        self.__profissionalRepository__ = professionalRepository

    def resetSenha(self, email: str):
        email_config = {
            "smtp_server": "smtp.office365.com",
            "smtp_port": 587,  # Use a porta 587 para TLS
            "smtp_user": "mentalTech123@outlook.com",
            "smtp_password": "mental1234",
            "sender_email": "mentalTech123@outlook.com",
        }

        pessoa_reset = self.__pessoaRepository__.find_by_email(email=email)

        if pessoa_reset is None:
            pessoa_reset = self.__profissionalRepository__.find_by_email(email=email)

        if pessoa_reset is not None:
            body = f"Olá, sua senha atual é {pessoa_reset.senha}, para uma maior segurança, altere sua senha na tela de meus dados."
            message = MIMEText(body)
            message["Subject"] = "Recuperação de senha"
            message["From"] = email_config["sender_email"]
            message["To"] = email

            # Conexão com o servidor SMTP usando starttls()
            context = ssl.create_default_context()
            with smtplib.SMTP(email_config["smtp_server"], email_config["smtp_port"]) as server:
                server.starttls(context=context)
                server.login(email_config["smtp_user"], email_config["smtp_password"])
                server.sendmail(email_config["sender_email"], [pessoa_reset.email], message.as_string())

            return {"message": "E-mail enviado com sucesso"}