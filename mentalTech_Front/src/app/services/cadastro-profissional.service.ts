import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { MatSnackBar } from '@angular/material/snack-bar';
import { Observable } from 'rxjs';
import { environment } from 'src/environments/environment';
import { Profissional } from '../models/Profissional.models';

@Injectable({
  providedIn: 'root'
})
export class CadastroProfissionalService {

  private profissional: Profissional = {
    nome: '',
    senha: '',
    dataNascimento: new Date,
    telefone: '',
    email: '',
    administrador: false,
    sexo: 1,
    codigoProfissional: '',
    descricaoProfissional: '',
    cpf: '',
    pix: '',
  };
  constructor(private snackBar: MatSnackBar, private http: HttpClient) { }

  create(paciente: Profissional): Observable<Profissional> {
    return this.http.post<Profissional>(`${environment.baseUrl}/profissional`, paciente);
  }
  listar(): Observable<Profissional[]> {
    return this.http.get<Profissional[]>(`${environment.baseUrl}/profissional`);
  }

  listarPorCpf(cpf: any): Observable<Profissional> {
    return this.http.get<Profissional>(`${environment.baseUrl}/profissional/cpf/${cpf}`);
  }

  deletar(idPessoa: number): Observable<any> {
    return this.http.delete<number>(`${environment.baseUrl}/profissional/${idPessoa}`);
  }

  setProfissional(profissional: Profissional){
   this.profissional = profissional;
  }

  getProfissional():Profissional{
    return this.profissional;
  }
}
