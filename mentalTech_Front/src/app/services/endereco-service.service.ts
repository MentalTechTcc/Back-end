import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { MatSnackBar } from '@angular/material';
import { Endereco } from '../models/Endereco.models';
import { environment } from 'src/environments/environment';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class EnderecoServiceService {

  constructor(private snackBar: MatSnackBar, private http: HttpClient) { }

  create(paciente: Endereco): Observable<Endereco> {
    return this.http.post<Endereco>(`${environment.baseUrl}/endereco`, paciente);
  }
}
