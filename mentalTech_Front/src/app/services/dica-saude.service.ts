import { Injectable } from '@angular/core';
import { Dica } from '../models/Dica.models';
import { environment } from 'src/environments/environment';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { MatSnackBar } from '@angular/material';

@Injectable({
  providedIn: 'root'
})
export class DicaSaudeService {

  constructor(private snackBar: MatSnackBar, private http: HttpClient) { }

  listar(): Observable<Dica[]> {
    return this.http.get<Dica[]>(`${environment.baseUrl}/dicaSaude`);
  }
  cadastrarDica(dica: Dica): Observable<any> {
    return this.http.post(`${environment.baseUrl}/dicaSaude`, dica);
  }
  
  deletarDica(idDicaSaude: number, cpfProfissional:string): Observable<any> {
    return this.http.delete<number>(`${environment.baseUrl}/dicaSaude/${idDicaSaude}/${cpfProfissional}?id=${idDicaSaude}`);
  }
  
}
