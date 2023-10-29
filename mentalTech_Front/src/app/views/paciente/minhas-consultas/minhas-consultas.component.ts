import { Component, OnInit } from '@angular/core';
import {LoginUsuarioService} from 'src/app/services/login-usuario.service'
import {ConsultaService} from 'src/app/services/consulta.service'
import {CadastroAgendaProfissionalService} from 'src/app/services/cadastro-agenda-profissional.service'
import { AgendaRequestId } from 'src/app/models/Agenda.models';
import { ConsultaRequestId } from 'src/app/models/Consulta.models';

@Component({
  selector: 'app-minhas-consultas',
  templateUrl: './minhas-consultas.component.html',
  styleUrls: ['./minhas-consultas.component.css']
})
export class MinhasConsultasComponent implements OnInit {
  listaAgendas: AgendaRequestId[] = [];
  pessoa: any = {};
  listaConsultas: ConsultaRequestId[] = [];

  constructor(
    private loginService: LoginUsuarioService,
    private agendaService: CadastroAgendaProfissionalService,
    private consultaService: ConsultaService
    ) { }

  ngOnInit(): void {
    this.loginService.getPerfilPessoa().subscribe(
      (data: any) => {
        this.pessoa = data;
        console.log(this.pessoa.idPessoa);
        this.carregarConsulta(this.pessoa.idPessoa);
      },
      (error) => {
        console.log('error');
      }
    );
  }

  carregarConsulta(idPessoa:number) {
     this.consultaService.listarPorIdPessoa(idPessoa).subscribe(consultas => {
       this.listaConsultas = consultas;
       console.log(this.listaConsultas);
      /* this.carregarAgenda(this.listaConsultas.idAgenda);*/
     });
    
   }

   carregarAgenda(idAgenda:number) {
     this.agendaService.listarPorIdAgenda(idAgenda).subscribe(consultas => {
       this.listaAgendas = consultas;
       console.log(this.listaAgendas);
     });
     
   }

}


