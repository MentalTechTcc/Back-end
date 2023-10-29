import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { Agenda, AgendaRequestId } from 'src/app/models/Agenda.models';
import { Consulta } from 'src/app/models/Consulta.models';
import { ConsultaService } from 'src/app/services/consulta.service';
import {LoginUsuarioService} from 'src/app/services/login-usuario.service'

@Component({
  selector: 'app-agenda-modal',
  templateUrl: './agenda-modal.component.html',
  styleUrls: ['./agenda-modal.component.css']
})
export class AgendaModalComponent implements OnInit {
  @Input() agendaDoProfissional: AgendaRequestId[]=[];
  @Output() fecharModalEvent = new EventEmitter<void>(); 
  pessoa: any = {};
  permitirCompartilhamentoMap: { [key: number]: boolean } = {};


  constructor(
    private consultaService: ConsultaService,
    private loginService: LoginUsuarioService,) {}

    ngOnInit(): void {
      this.loginService.getPerfilPessoa().subscribe(
        (data: any) => {
          this.pessoa = data;
          this.agendaDoProfissional.forEach((agenda) => {
            this.permitirCompartilhamentoMap[agenda.idAgenda] = false;
          });
        },
        (error) => {
          console.log('error');
        }
      );
    }
    

  fecharModal() {
    this.fecharModalEvent.emit();
  }
  getModalidadeLabel(modalidade: number): string {
    return modalidade === 1 ? 'Presencial' : 'Online';
  }

  agendarConsulta(agenda: AgendaRequestId) {
    const consulta: Consulta = {
      valor: agenda.valorProposto,
      idAgenda: agenda.idAgenda,
      idPessoa: this.pessoa.idPessoa,
      permiteCompartilharConhecimento: this.permitirCompartilhamentoMap[agenda.idAgenda], 
      ocorreu: false,
    };

    this.consultaService.cadastrarConsulta(consulta).subscribe(
      (response) => {

        /*console.log(consulta);*/
        console.log('Consulta agendada com sucesso', response);
      },
      (error) => {

        console.error('Erro ao agendar consulta', error);
      }
    );
  }

  atualizarPermissao(event: any, idAgenda: number) {
    this.permitirCompartilhamentoMap[idAgenda] = event;
  }
  
  
}
