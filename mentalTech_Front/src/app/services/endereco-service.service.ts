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
    return this.http.get<EnderecoResponse[]>(`${environment.baseUrl}/endereco`);
  }


  getId(enderecos: EnderecoResponse[], atual_cep: String, atual_numero: number): number {
    for (const endereco of enderecos) {
      console.log("hi hi hi :", endereco.cep, endereco.numero);
      console.log("atual_cep:", atual_cep);
      console.log("atual_numero:", atual_numero);

      // Lógica para comparar a endereco atual
      if (endereco.cep === atual_cep && endereco.numero == atual_numero) {
        return endereco.idEndereco;
      }
    }
    return -1;
  }

  createEnderecoProfissional(paciente: ProfissionalTemEndereco): Observable<ProfissionalTemEndereco> {
    return this.http.post<ProfissionalTemEndereco>(`${environment.baseUrl}/endereco/PessoaPossuiEndereco`, paciente);
  }

  listarEnderecoProfissional(cpfProfissional:string): Observable<ProfissionalTemEndereco[]> {
    return this.http.get<ProfissionalTemEndereco[]>(`${environment.baseUrl}/endereco/PessoaPossuiEndereco/${cpfProfissional}`);
  }

  listarEnderecoPorId(idEndereco:number): Observable<EnderecoResponse> {
    return this.http.get<EnderecoResponse>(`${environment.baseUrl}/endereco/{idEndereco}?id=${idEndereco}`);
  }

}

