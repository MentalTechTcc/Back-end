import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Agenda, AgendaRequestId } from 'src/app/models/Agenda.models';
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
  listaAgendas: AgendaRequestId[] = [];
  

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
      console.log(this.listaAgendas);
    });
    
  }

deletarAgenda(idAgenda: number): void {
    if (confirm('Tem certeza de que deseja excluir esta agenda?')) {
      this.agendaService.deletar(idAgenda).subscribe(
        () => {
          this.carregarAgenda();
        },
        (error) => {
          console.error('Erro ao excluir a agenda:', error);
        }
      );
    }
  }
  

  getOcupadoLabel(ocupado: boolean): string {
    return ocupado ? 'Ocupado' : 'Disponível';
  }

}
