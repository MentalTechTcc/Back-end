import { Component, OnInit } from '@angular/core';

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
  constructor() { }

  ngOnInit(): void {
  }

}