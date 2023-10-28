import { Injectable } from '@angular/core';
import { environment } from 'src/environments/environment';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { MatSnackBar } from '@angular/material';
import { Consulta } from '../models/Consulta.models';

@Injectable({
  providedIn: 'root'
})
export class ConsultaService {

  constructor(private snackBar: MatSnackBar, private http: HttpClient) { }

  listar(): Observable<Consulta[]> {
    return this.http.get<Consulta[]>(`${environment.baseUrl}/consulta`);
  }
  cadastrarDica(consulta: Consulta): Observable<any> {
    return this.http.post(`${environment.baseUrl}/consulta`, consulta);
  }
}