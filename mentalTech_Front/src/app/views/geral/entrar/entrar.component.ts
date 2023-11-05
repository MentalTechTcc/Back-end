import { Router } from '@angular/router';
import { LoginUsuarioService } from './../../../services/login-usuario.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-entrar',
  templateUrl: './entrar.component.html',
  styleUrls: ['./entrar.component.css']
})
export class EntrarComponent implements OnInit {

  opcao: string = 'paciente'; // Inicializa com 'paciente'
  email: string = '';
  senha: string = '';
  cpf: string = '';
  errorMessage: string = '';

  constructor(private router: Router, private loginService: LoginUsuarioService) {}

  ngOnInit(): void {
    // Adicione inicializações se necessário
  }

  selectOption(option: string): void {
    this.opcao = option;
  }

  entrar(): void {
    this.loginService.setPerfil(this.opcao);
    this.loginService.setFezLogin(true);
    if (this.opcao === 'paciente') {
      // Navegar para a rota de paciente
      this.loginService.loginPaciente(this.email, this.senha).subscribe(
        (response) => {
          this.loginService.setSenha(this.senha);
          this.router.navigate(['/home-paciente']);
        },
        (error) => {
          // Lida com erros (autenticação falhou, etc.)
          this.errorMessage = 'Falha no login. Verifique seu CPF e senha.';
          console.error(error);
        }
      );
    } else if (this.opcao === 'profissional') {

      // Navegar para a rota de profissional
      this.loginService.loginProfissional(this.cpf, this.senha).subscribe(
        (response) => {
          this.loginService.setSenha(this.senha);

          this.router.navigate(['/home-profissional']);
        },
        (error) => {
          // Lida com erros (autenticação falhou, etc.)
          this.errorMessage = 'Falha no login. Verifique seu CPF e senha.';
          console.error(error);
        }
      );

    }
  }
}
