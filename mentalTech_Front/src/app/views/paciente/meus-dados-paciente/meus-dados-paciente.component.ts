import { Component, OnInit } from '@angular/core';
import { Paciente } from 'src/app/models/Paciente.models';
import { LoginUsuarioService } from 'src/app/services/login-usuario.service';

@Component({
  selector: 'app-meus-dados-paciente',
  templateUrl: './meus-dados-paciente.component.html',
  styleUrls: ['./meus-dados-paciente.component.css']
})
export class MeusDadosPacienteComponent implements OnInit {

  nome: string = '';
  telefone: string = '';
  emailPaciente: string = '';
  senhaPaciente: string = '';
  dataNascimentoPaciente: Date = new Date();
  paciente: any;
  constructor(private loginService: LoginUsuarioService) { }

  ngOnInit(): void {
    this.loginService.getPerfilPessoa().subscribe(
      (data: Paciente) => {
        this.paciente = data;

        this.nome = this.paciente.nome;
        this.telefone = this.paciente.telefone;
        this.emailPaciente = this.paciente.email;
        this.dataNascimentoPaciente = this.paciente.dataNascimento;
      },
      error => {
        console.error('Erro ao buscar especialistas:', error);
      }
    );
  }

}
