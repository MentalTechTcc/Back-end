import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { MatSnackBar } from '@angular/material';
import { Relatorio, RelatorioRequestId } from '../models/Relatorio.models';

@Injectable({
  providedIn: 'root'
})
export class RelatorioService {

  constructor(private snackBar: MatSnackBar, private http: HttpClient) { }


  cadastrarRelatorio(relatorio: Relatorio): Observable<any> {
    return this.http.post(`${environment.baseUrl}/relatorio`, relatorio);
  }

  listarPorCpfProfissional(cpfProfissional:string): Observable<RelatorioRequestId[]> {
    return this.http.get<RelatorioRequestId[]>(`${environment.baseUrl}/relatorio/cpfProfissional/{CpfProfissional}?cpf=${cpfProfissional}`);
  }

 
}


