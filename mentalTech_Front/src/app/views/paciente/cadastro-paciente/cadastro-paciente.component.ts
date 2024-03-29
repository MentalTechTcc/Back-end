import { Router } from '@angular/router';
import { Component, OnInit } from '@angular/core';
import { Paciente } from 'src/app/models/Paciente.models';
import { CadastroPacienteService } from 'src/app/services/cadastro-paciente.service';
import { CadastroUsuarioService } from 'src/app/services/cadastro-usuario.service';

@Component({
  selector: 'app-cadastro',
  templateUrl: './cadastro-paciente.component.html',
  styleUrls: ['./cadastro-paciente.component.css']
})
export class CadastroPacienteComponent {

  escolhaPerfil: string = '';
  nomePaciente: string = '';
  telefone: string = '';
  emailPaciente: string = '';
  senhaPaciente: string = '';
  dataNascimentoPaciente: Date = new Date();
  genero: number = 1;
  errorMessage: string = '';

  constructor(private router: Router, private cadastroService: CadastroUsuarioService, private cadastroPacienteService: CadastroPacienteService) {
  }

  ngOnInit() {
    this.escolhaPerfil = this.cadastroService.getEscolhaPerfil();
    console.log('Escolha de perfil recebida:', this.escolhaPerfil);
  }
  cadastrar() {

    if (this.escolhaPerfil === 'Paciente') {
      const paciente: Paciente = {
        nome: this.nomePaciente,
        senha: this.senhaPaciente,
        dataNascimento: this.dataNascimentoPaciente,
        telefone: this.telefone,
        email: this.emailPaciente,
        administrador: false,
        sexo: this.genero
      };

      console.log(paciente);

      this.cadastroPacienteService.create(paciente).subscribe(
        response => {
          console.log('Cadastro bem-sucedido:', response);
          this.router.navigate(['/login']);

        },
        error => {
          console.error('Erro no cadastro:', error);
          this.errorMessage = 'Falha no login. Verifique seu CPF e senha.';
          this.delayErrorMessageRemoval();
        }
      );
    }
  }

  mapearGenero(generoSelecionado: string): void {
    if (generoSelecionado === 'feminino') {
      this.genero = 1;
    } else if (generoSelecionado === 'masculino') {
      this.genero = 2;
    }
  }

  delayErrorMessageRemoval(): void {
    setTimeout(() => {
      this.errorMessage = ''; // Remove a mensagem após alguns segundos
    }, 5000); // 5000 milissegundos = 5 segundos, ajuste conforme necessário
  }
}
