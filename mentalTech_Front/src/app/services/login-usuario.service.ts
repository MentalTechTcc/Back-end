import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, catchError } from 'rxjs';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class LoginUsuarioService {

  constructor(private http: HttpClient) { }

  private fezLogin: boolean = false;
  private perfil: string = '';

  setFezLogin(resposta: boolean) {
    this.fezLogin = resposta;
  }

  getFezLogin(): boolean {
    return this.fezLogin;
  }

  setPerfil(resposta: string) {
    this.perfil = resposta;
  }

  getPerfil(): string {
    return this.perfil;
  }

  loginPaciente(email: string, senha: string): Observable<any> {
    const body = new HttpParams()
      .set('email', email)
      .set('senha', senha);

    const headers = new HttpHeaders({
      'Content-Type': 'application/x-www-form-urlencoded',
    });

    const request_value = this.http.post(`${environment.baseUrl}/login/pessoa/`, body.toString(), { headers }).pipe(
      catchError((error) => {
        console.error('Erro na solicitação HTTP:', error);
        throw error;
      })
    );

    return request_value
  }


  logout():void{

  }
}
