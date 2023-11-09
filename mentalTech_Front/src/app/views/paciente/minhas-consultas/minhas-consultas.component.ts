import { Agenda } from './../../../models/Agenda.models';
import { Component, OnInit } from '@angular/core';
import {LoginUsuarioService} from 'src/app/services/login-usuario.service'
import {ConsultaService} from 'src/app/services/consulta.service'
import {CadastroAgendaProfissionalService} from 'src/app/services/cadastro-agenda-profissional.service'
import { AgendaRequestId } from 'src/app/models/Agenda.models';
import { ConsultaRequestId } from 'src/app/models/Consulta.models';
import { Observable, of } from 'rxjs';
import { map } from 'rxjs/operators';
import {EnderecoServiceService} from 'src/app/services/endereco-service.service';

@Component({
  selector: 'app-minhas-consultas',
  templateUrl: './minhas-consultas.component.html',
  styleUrls: ['./minhas-consultas.component.css']
})
export class MinhasConsultasComponent implements OnInit {
  listaAgendas: AgendaRequestId[] = [];
  pessoa: any = {};
  listaConsultas: ConsultaRequestId[] = [];
  cacheDescricao: { [id: number]: string } = {};

  constructor(
    private loginService: LoginUsuarioService,
    private agendaService: CadastroAgendaProfissionalService,
    private consultaService: ConsultaService,
    private enderecoService: EnderecoServiceService 
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

  carregarConsulta(idPessoa: number) {
    this.consultaService.listarPorIdPessoa(idPessoa).subscribe(consultas => {

      if (Array.isArray(consultas)) {
        this.listaConsultas = consultas;
        console.log(this.listaConsultas);

        this.listaAgendas = [];

        for (const consulta of this.listaConsultas) {
          this.carregarAgenda(consulta.idAgenda);
        }
      } else {
        console.error('Dados de consulta não são um array:', consultas);
      }
    });
  }

  carregarAgenda(idAgenda: number) {
    this.agendaService.listarPorIdAgenda(idAgenda).subscribe(agendas => {

      if (Array.isArray(agendas)) {

        this.listaAgendas = this.listaAgendas.concat(agendas);
        console.log(this.listaAgendas);
      } else {

        this.listaAgendas = this.listaAgendas.concat([agendas]);
        console.log(this.listaAgendas);
      }
    });
  }


   getOcupadoLabel(ocupado: boolean): string {
    return ocupado ? 'Ocupado' : 'Disponível';
  }

   getModalidadeLabel(modalidade: number): string {
    return modalidade === 1 ? 'Presencial' : 'Online';
  }

  deletarConsulta(idAgenda: number): void { // deleta consulta pela agenda
    if (confirm('Tem certeza de que deseja desistir dessa consulta?')) {
      this.consultaService.deletar(idAgenda).subscribe(
        () => {
          this.carregarConsulta(this.pessoa.idPessoa);
          console.log('primeiro id: ' + idAgenda);
          this.atualizaAgendaMarcacao(idAgenda);


        },
        (error) => {
          console.error('Erro ao excluir a agenda:', error);
        }
      );
    }
  }

  atualizaAgendaMarcacao(agendaId: number): void {
    console.log('segundo id: ' + agendaId);

    this.buscarAgenda(agendaId).subscribe(
      (agenda: AgendaRequestId | undefined) => {
        console.log('resultado ', agenda);

        if (agenda !== undefined) {
          agenda.ocupado = false;

          this.agendaService.updateAgendaMarcacao(agenda).subscribe(
            response => {
              console.log('Cadastro bem-sucedido:', response);
            },
            error => {
              console.error('Erro no cadastro:', error);
            }
          );
        }
      }
    );
  }

  buscarAgenda(idAgenda: number): Observable<AgendaRequestId | undefined> {
    return this.agendaService.listarPorIdAgenda(idAgenda);
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


