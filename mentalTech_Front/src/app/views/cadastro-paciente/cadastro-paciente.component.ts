import { Paciente } from '../../models/Paciente.models';
import { CadastroPacienteService } from '../../services/cadastro-paciente.service';
import { Component, OnInit } from '@angular/core';
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

  constructor(private cadastroService: CadastroUsuarioService, private cadastroPacienteService: CadastroPacienteService) {
  }

  ngOnInit() {
    this.escolhaPerfil = this.cadastroService.getEscolhaPerfil();
    console.log('Escolha de perfil recebida:', this.escolhaPerfil);
  }
  cadastrar() {

    if (this.escolhaPerfil === 'Paciente') {
      const paciente: Paciente = {
        nome: this.nomePaciente,
        telefone: this.telefone,
        email: this.emailPaciente,
        senha: this.senhaPaciente,
        dataNascimento: this.dataNascimentoPaciente,
        sexo: this.genero,
        administrador: false
      };

      console.log(paciente);

      // Chame o serviço para cadastrar o paciente
      // this.cadastroPacienteService.create(paciente).subscribe(
      //   response => {
      //     console.log('Cadastro bem-sucedido:', response);
      //   },
      //   error => {
      //     console.error('Erro no cadastro:', error);
      //   }
      // );
    }
  }

  mapearGenero(generoSelecionado: string): void {
    if (generoSelecionado === 'feminino') {
      this.genero = 1;
    } else if (generoSelecionado === 'masculino') {
      this.genero = 2;
    }
  }
}