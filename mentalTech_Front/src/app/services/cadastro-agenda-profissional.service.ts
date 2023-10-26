import { Injectable } from '@angular/core';
import { Agenda } from '../models/Agenda.models';
import { environment } from 'src/environments/environment';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})
export class CadastroAgendaProfissionalService {

  constructor(private http: HttpClient) { }

  cadastrarAgenda(agenda: Agenda): Observable<any> {
    return this.http.post(`${environment.baseUrl}/agenda`, agenda);
  }

  listar(): Observable<Agenda[]> {
    return this.http.get<Agenda[]>(`${environment.baseUrl}/agenda`);
  }

}

