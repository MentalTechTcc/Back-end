import { Injectable } from '@angular/core';
import { ProfissionalTrataTematica, Tematica, TematicaResponse } from '../models/Tematica.models';
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

  getId(tematicas: TematicaResponse[], atual: String):number{

    for (const tematica of tematicas) {
      // Lógica para comparar a tematica atual
      if (tematica.nomeTematica === atual) {
        return tematica.idTematicasPrincipais;
      }
    }
    return -1;
  }

  createTematicaProfissional(paciente: ProfissionalTrataTematica): Observable<ProfissionalTrataTematica> {
    return this.http.post<ProfissionalTrataTematica>(`${environment.baseUrl}/tematicasPrincipais/ProfissionalTrataTematicas`, paciente);
  }

  listarTematicasProfissional(cpfProfissional:string):Observable<Tematica[]>{
    return this.http.get<Tematica[]>(`${environment.baseUrl}/tematicasPrincipais/cpf/${cpfProfissional}`);
  }

}

