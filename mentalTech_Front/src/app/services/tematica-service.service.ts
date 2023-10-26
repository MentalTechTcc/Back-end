import { Injectable } from '@angular/core';
import { Tematica, TematicaResponse } from '../models/Tematica.models';
import { environment } from 'src/environments/environment';
import { Observable } from 'rxjs';
import { MatSnackBar } from '@angular/material';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class TematicaServiceService {

  constructor(private snackBar: MatSnackBar, private http: HttpClient) { }

  create(paciente: Tematica): Observable<Tematica> {
    return this.http.post<Tematica>(`${environment.baseUrl}/tematicasPrincipais`, paciente);
  }
  listar(): Observable<TematicaResponse[]> {
    return this.http.get<TematicaResponse[]>(`${environment.baseUrl}/tematicasPrincipais`);
  }
}
