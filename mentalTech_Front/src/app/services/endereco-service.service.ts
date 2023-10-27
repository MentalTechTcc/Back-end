import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { MatSnackBar } from '@angular/material';
import { Endereco, EnderecoResponse, ProfissionalTemEndereco } from '../models/Endereco.models';
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

  listar(): Observable<EnderecoResponse[]> {
    return this.http.get<EnderecoResponse[]>(`${environment.baseUrl}/tematicasPrincipais`);
  }


  getId(enderecos: EnderecoResponse[], atual_cpf: String, atual_numero: number):number{

    for (const endeco of enderecos) {
      // Lógica para comparar a endeco atual
      if (endeco.cep === atual_cpf && endeco.numero == atual_numero) {
        return endeco.idEndereco;
      }
    }
    return -1;
  }

  createEnderecoProfissional(paciente: ProfissionalTemEndereco): Observable<ProfissionalTemEndereco> {
    return this.http.post<ProfissionalTemEndereco>(`${environment.baseUrl}/endereco/PessoaPossuiEndereco`, paciente);
  }
}
