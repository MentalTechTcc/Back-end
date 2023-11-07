import { Router } from '@angular/router';
import { LoginUsuarioService } from './../../../services/login-usuario.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-entrar',
  templateUrl: './entrar.component.html',
  styleUrls: ['./entrar.component.css']
})
export class EntrarComponent implements OnInit {

  opcao: string = 'paciente';
  email: string = '';
  senha: string = '';
  cpf: string = '';
  errorMessage: string = '';
  esqueciSenhaVisible: boolean = false;
  forgotEmail: string = '';

  constructor(private router: Router, private loginService: LoginUsuarioService) {}

  ngOnInit(): void {
    // Adicione inicializações se necessário
  }

  selectOption(option: string): void {
    this.opcao = option;
  }

  entrar(): void {
    // Se não estiver visível, trata como o login normal
    if (!this.esqueciSenhaVisible) {
      this.loginService.setPerfil(this.opcao);
      this.loginService.setFezLogin(true);

      if (this.opcao === 'paciente') {
        this.loginService.loginPaciente(this.email, this.senha).subscribe(
          (response) => {
            this.loginService.setSenha(this.senha);
            this.router.navigate(['/home-paciente']);
          },
          (error) => {
            this.errorMessage = 'Falha no login. Verifique seu email e senha.';
            console.error(error);
            this.delayErrorMessageRemoval();
          }
        );
      } else if (this.opcao === 'profissional') {
        this.loginService.loginProfissional(this.cpf, this.senha).subscribe(
          (response) => {
            this.loginService.setSenha(this.senha);
            this.router.navigate(['/home-profissional']);
          },
          (error) => {
            this.errorMessage = 'Falha no login. Verifique seu cpf e senha.';
            console.error(error);
            this.delayErrorMessageRemoval();
          }
        );
      }
    } else {
      // Se estiver visível, trata como "Esqueci Minha Senha"
      this.enviarEsqueciSenha();
    }
  }

  toggleEsqueciSenhaForm(): void {
    this.esqueciSenhaVisible = !this.esqueciSenhaVisible;
  }

  enviarEsqueciSenha(): void {
    if (this.forgotEmail && this.opcao) {
      console.log("email: " + this.forgotEmail);
      console.log("perfil" + this.opcao)
      // this.loginService.enviarEsqueciSenha(this.opcao, this.forgotEmail).subscribe(
      //   (response) => {
      //     console.log(response);
      //     // Adicione lógica para exibir mensagem ao usuário se necessário
      //   },
      //   (error) => {
      //     console.error(error);
      //     // Adicione lógica para exibir mensagem de erro ao usuário se necessário
      //   }
      // );
    }
  }

  delayErrorMessageRemoval(): void {
    setTimeout(() => {
      this.errorMessage = '';
    }, 5000);
  }
}
