import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Agenda } from 'src/app/models/Agenda.models';
import {LoginUsuarioService} from 'src/app/services/login-usuario.service'
import {CadastroAgendaProfissionalService} from 'src/app/services/cadastro-agenda-profissional.service'

@Component({
  selector: 'app-minha-agenda-profissional',
  templateUrl: './minha-agenda-profissional.component.html',
  styleUrls: ['./minha-agenda-profissional.component.css']
})
export class MinhaAgendaProfissionalComponent implements OnInit {
  cpfProfissional:string = '';
  profissional: any = {};
  listaAgendas: Agenda[] = [];
  

  constructor(
    private loginService: LoginUsuarioService,
    private agendaService: CadastroAgendaProfissionalService,
    ) {
 }

  ngOnInit(): void {
    this.loginService.getPerfilProfissional().subscribe(
      (data: any) => {
        this.profissional = data;
    
        this.carregarAgenda();
      },
      (error) => {
        console.log('error');
      }
    );
  }

  carregarAgenda() {
   /* console.log(this.profissional.cpf)*/
    this.agendaService.listarPorCpf(this.profissional.cpf.toString()).subscribe(agendas => {
      this.listaAgendas = agendas;
    });
    console.log(this.listaAgendas);
  }

  getOcupadoLabel(ocupado: boolean): string {
    return ocupado ? 'Ocupado' : 'Disponível';
  }

}
