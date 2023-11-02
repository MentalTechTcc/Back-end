import { Injectable } from '@angular/core';
import { Agenda, AgendaRequestId } from '../models/Agenda.models';
import { environment } from 'src/environments/environment';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class CadastroAgendaProfissionalService {

  private linkPagamento: string = '';
  private pix: string = '';


  constructor(private http: HttpClient) { }


  setPix(pix: string){
    this.pix = pix;
  }

  getPix(): string{
    return this.pix;
  }

  setLinkPagamento(linkPagamento: string){
    this.linkPagamento = linkPagamento;
  }

  getLinkPagamento(): string{
    return this.linkPagamento;
  }

  cadastrarAgenda(agenda: Agenda): Observable<any> {
    return this.http.post(`${environment.baseUrl}/agenda`, agenda);
  }

  listar(): Observable<Agenda[]> {
    return this.http.get<Agenda[]>(`${environment.baseUrl}/agenda`);
  }

  listarPorCpf(cpfProfissional: string): Observable<AgendaRequestId[]> {
    return this.http.get<AgendaRequestId[]>(`${environment.baseUrl}/agenda/cpf/{cpfProfissional}?cpf=${cpfProfissional}`);
  }

  listarPorIdAgenda(idAgenda: number): Observable<AgendaRequestId> {
    return this.http.get<AgendaRequestId>(`${environment.baseUrl}/agenda/{idAgenda}?id=${idAgenda}`);
  }

  deletar(idAgenda: number): Observable<AgendaRequestId[]> {
    return this.http.delete<AgendaRequestId[]>(`${environment.baseUrl}/consulta/idConsulta/{idConsulta}?id=${idAgenda}`);
  }

  updateAgendaMarcacao(agenda: AgendaRequestId): Observable<any> {
    return this.http.put(`${environment.baseUrl}/agenda/{idAgenda}?id=${agenda.idAgenda}`, agenda);
  }


}


