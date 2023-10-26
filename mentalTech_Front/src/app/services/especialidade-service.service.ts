import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { MatSnackBar } from '@angular/material';
import { Especialidade, ProfissionalTrataEspecialidade } from '../models/Especialidade.models';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class EspecialidadeServiceService {

  constructor(private snackBar: MatSnackBar, private http: HttpClient) { }

  listar(): Observable<Especialidade[]> {
    return this.http.get<Especialidade[]>(`${environment.baseUrl}/especialidade`);
  }

  createEspecialidadeProfissional(paciente: ProfissionalTrataEspecialidade): Observable<ProfissionalTrataEspecialidade> {
    return this.http.post<ProfissionalTrataEspecialidade>(`${environment.baseUrl}/especialidade/PessoaPossuiEspecialidade`, paciente);
  }
  getId(especialidades: Especialidade[], atual: String):number{

    for (const especialidade of especialidades) {
      // Lógica para comparar a especialidade atual
      if (especialidade.descricaoEspecialidade === atual) {
        return especialidade.idEspecialidade;
      }
    }
    return -1;
  }

}
