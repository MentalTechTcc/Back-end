import { Component, OnInit } from '@angular/core';
import { LoginUsuarioService } from 'src/app/services/login-usuario.service';

@Component({
  selector: 'app-meus-dados-paciente',
  templateUrl: './meus-dados-paciente.component.html',
  styleUrls: ['./meus-dados-paciente.component.css']
})
export class MeusDadosPacienteComponent implements OnInit {

  nome: string = "Teste";
  telefone: string = '';
  emailPaciente: string = '';
  senhaPaciente: string = '';
  dataNascimentoPaciente: Date = new Date();
  constructor(private loginService: LoginUsuarioService) { }

  ngOnInit(): void {
    console.log(this.loginService.getPerfilPessoa());
  }

}
