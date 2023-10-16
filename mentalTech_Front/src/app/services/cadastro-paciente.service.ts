import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { MatSnackBar } from '@angular/material/snack-bar';
import { Paciente } from '../models/Paciente.models';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class CadastroPacienteService {

  constructor(private snackBar: MatSnackBar, private http: HttpClient) { }

  create(paciente: Paciente): Observable<Paciente> {
    return this.http.post<Paciente>(`${environment.baseUrl}/pessoa`, paciente);
  }
}
