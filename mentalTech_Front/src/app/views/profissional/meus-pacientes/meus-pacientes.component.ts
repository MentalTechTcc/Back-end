import { Component, OnInit } from '@angular/core';
import { Relatorio } from 'src/app/models/Relatorio.models';
import { PacienteResponse } from 'src/app/models/Paciente.models';
import {LoginUsuarioService} from 'src/app/services/login-usuario.service'
import {RelatorioService} from 'src/app/services/relatorio.service'
import {CadastroPacienteService} from 'src/app/services/cadastro-paciente.service'
import { Router } from '@angular/router';

@Component({
  selector: 'app-meus-pacientes',
  templateUrl: './meus-pacientes.component.html',
  styleUrls: ['./meus-pacientes.component.css']
})
export class MeusPacientesComponent implements OnInit {

  pacientes: PacienteResponse[] = [];
  profissional:any=[];
  isModalOpen = false;
  relatorioModal: Relatorio | null = null;


  constructor(
    private service: RelatorioService,
    private serviceProfissional: LoginUsuarioService,
    private servicePaciente:CadastroPacienteService,
    private router: Router
    ) { }

  ngOnInit(): void {
    this.serviceProfissional.getPerfilProfissional().subscribe(
      (data: any) => {
        this.profissional = data;
        console.log(data)
        this.servicePaciente.listarPacientesPorCpfProfissional(this.profissional.cpf).subscribe(
          (data: PacienteResponse[]) => {
            this.pacientes = data;
            console.log(data)
          },
          error => {
            console.error('Erro ao buscar relatórios:', error);
          }
        );
      },
      (error) => {
        console.log('error');
      }
    );

  }

  irParaRelatorios(idPessoa: number) {
    this.router.navigate(['/relatorios-paciente', idPessoa]);
  }



}
