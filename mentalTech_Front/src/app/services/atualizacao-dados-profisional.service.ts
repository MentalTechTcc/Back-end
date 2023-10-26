import { Injectable } from '@angular/core';
import {  ProfissionalRequestId } from '../models/Profissional.models';
import { environment } from 'src/environments/environment';
import { Observable } from 'rxjs';
import { MatSnackBar } from '@angular/material';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class AtualizacaoDadosProfisionalService {

  
  constructor(private http: HttpClient) { }

  atualizarProfissional(profissional: ProfissionalRequestId): Observable<any> {
    const url = `${environment.baseUrl}/profissionais/${profissional.idPessoa}`;
    return this.http.put(url, profissional);
  }

}
