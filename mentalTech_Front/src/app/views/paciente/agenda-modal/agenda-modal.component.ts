import { Profissional } from 'src/app/models/Profissional.models';
import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { Router } from '@angular/router';
import { Agenda, AgendaRequestId } from 'src/app/models/Agenda.models';
import { Consulta } from 'src/app/models/Consulta.models';
import { CadastroAgendaProfissionalService } from 'src/app/services/cadastro-agenda-profissional.service';
import { CadastroProfissionalService } from 'src/app/services/cadastro-profissional.service';
import { ConsultaService } from 'src/app/services/consulta.service';
import {LoginUsuarioService} from 'src/app/services/login-usuario.service'
import { Observable, of } from 'rxjs';
import { map } from 'rxjs/operators';
import {EnderecoServiceService} from 'src/app/services/endereco-service.service';

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
  cacheDescricao: { [id: number]: string } = {};


  constructor(
    private consultaService: ConsultaService,
    private loginService: LoginUsuarioService,
    private router: Router,
    private agendaService: CadastroAgendaProfissionalService,
    private profissionalService: CadastroProfissionalService,
    private enderecoService: EnderecoServiceService 
    ) {}

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

    this.agendaService.setLinkPagamento(agenda.linkPagamento);

    this.consultaService.cadastrarConsulta(consulta).subscribe(
      (response) => {
        this.profissionalService.listarPorCpf(agenda.cpfProfissional).subscribe(
          (data: Profissional) => {
            this.agendaService.setPix(data.pix);

            agenda.ocupado=true

            this.agendaService.updateAgendaMarcacao(agenda).subscribe(
              response => {
                console.log('Cadastro bem-sucedido:', response);
              },
              error => {
                console.error('Erro no cadastro:', error);
              }
            );

          },
          (error) => {
            console.error('Erro ao buscar especialistas:', error);
          }
        );
        this.router.navigate(['/pagamento']);

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

  traduzirIdEnderecoParaDescricao(idEndereco: number): Observable<string> {
    if (idEndereco === null || idEndereco === undefined) {
      return of('Sem endereço');
    }

    const descricaoCache = this.cacheDescricao[idEndereco];
    if (descricaoCache) {
      return of(descricaoCache);
    }

    return this.enderecoService.listarEnderecoPorId(idEndereco).pipe(
      map((detalhesEndereco) => {
        const descricao = `${detalhesEndereco.cidade}-${detalhesEndereco.estado}, ${detalhesEndereco.bairro}, ${detalhesEndereco.numero}`;
        this.cacheDescricao[idEndereco] = descricao;
        return descricao;
      })
    );
  }

}
