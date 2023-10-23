import { Injectable } from '@angular/core';
import { Avaliacao } from '../models/Avaliacao.models';
import { environment } from 'src/environments/environment';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class AvaliacaoPacienteService {

  constructor(private http: HttpClient) { }

  listar(): Observable<Avaliacao[]> {
    return this.http.get<Avaliacao[]>(`${environment.baseUrl}/avaliacao`);
  }

  cadastrarAvaliacao(avaliacao: Avaliacao): Observable<any> {
    return this.http.post(`${environment.baseUrl}/avaliacao`, avaliacao);
  }
}
