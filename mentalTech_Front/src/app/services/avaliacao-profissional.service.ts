import { Injectable } from '@angular/core';
import { Avaliacao, AvaliacaoRequestId} from '../models/Avaliacao.models';
import { environment } from 'src/environments/environment';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { MatSnackBar } from '@angular/material';

@Injectable({
  providedIn: 'root'
})
export class AvaliacaoProfissionalService {

  constructor(private snackBar: MatSnackBar, private http: HttpClient) { }

  listarPorCpfProfissional(cpfProfissional:string): Observable<AvaliacaoRequestId[]> {
    return this.http.get<AvaliacaoRequestId[]>(`${environment.baseUrl}/avaliacao/cpfProfissional/${cpfProfissional}`);
  }


}
