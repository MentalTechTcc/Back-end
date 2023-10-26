import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { MatSnackBar } from '@angular/material';
import { Especialidade } from '../models/Especialidade.models';
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
}
