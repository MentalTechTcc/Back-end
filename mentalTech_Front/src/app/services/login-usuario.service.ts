import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, catchError, map } from 'rxjs';
import { environment } from 'src/environments/environment';

@Injectable({
  providedIn: 'root'
})
export class LoginUsuarioService {

  constructor(private http: HttpClient) { }

  private fezLogin: boolean = false;
  private perfil: string = '';
  private accessToken: any;
  private refreshToken: any;
  private accessToken_stored: any;
  private refreshToken_stored: any;
  private cpfProfissional: any;
  private senha: any;

  setSenha(senha: string){
    this.senha = senha;

  }
  getSenha():string{
    return this.senha;
  }

  setCpfProfissional(id: string){
    this.cpfProfissional = id;

  }
  getCpfProfissional():string{
    return this.cpfProfissional;
  }

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

    return this.http.post(`${environment.baseUrl}/login/pessoa/`, body.toString(), { headers }).pipe(
      catchError((error) => {
        console.error('Erro na solicitação HTTP:', error);
        throw error;
      }),
      map((response: any) => {
        // Aqui você pode extrair o valor do token da resposta
        localStorage.setItem('accessToken', response.access_token); // para guardar na sessão toda
        localStorage.setItem('refreshToken', response.refresh_token); // para guardar na sessão toda

        this.accessToken = response.access_token;
        this.refreshToken = response.refresh_token;
        console.log('acessToken:  ' + this.accessToken);
        console.log('refreshToken:  ' + this.refreshToken);

      })
    );
  }

  logoutPaciente(): Observable<any> {
    this.refreshToken_stored = localStorage.getItem('refreshToken');
    const headers = new HttpHeaders({
      'refresh-token': this.refreshToken_stored ,
    });
    return this.http.post(`${environment.baseUrl}/login/pessoa/logout`, null, { headers });

  }

  getPerfilPessoa(): Observable<any> {
    this.accessToken_stored = localStorage.getItem('accessToken');
    const headers = new HttpHeaders({
      'Authorization': `Bearer ${this.accessToken_stored}`, // token de acesso obtido no login
    });

    return this.http.get(`${environment.baseUrl}/login/pessoa/token`, { headers });
  }

  loginProfissional(cpf: string, senha: string): Observable<any> {
    const body = new HttpParams()
      .set('cpf', cpf)
      .set('senha', senha);

    const headers = new HttpHeaders({
      'Content-Type': 'application/x-www-form-urlencoded',
    });

    return this.http.post(`${environment.baseUrl}/login/profissional/`, body.toString(), { headers }).pipe(
      catchError((error) => {
        console.error('Erro na solicitação HTTP:', error);
        throw error;
      }),
      map((response: any) => {
        // Aqui você pode extrair o valor do token da resposta
        localStorage.setItem('accessToken', response.access_token); // para guardar na sessão toda
        localStorage.setItem('refreshToken', response.refresh_token); // para guardar na sessão toda

        this.accessToken = response.access_token;
        this.refreshToken = response.refresh_token;
        console.log('acessToken:  ' + this.accessToken);
        console.log('refreshToken:  ' + this.refreshToken);

      })
    );
  }

  logoutProfissional(): Observable<any> {
    this.refreshToken_stored = localStorage.getItem('refreshToken');
    const headers = new HttpHeaders({
      'refresh-token': this.refreshToken_stored ,
    });
    return this.http.post(`${environment.baseUrl}/login/profissional/logout`, null, { headers });

  }

  getPerfilProfissional(): Observable<any> {
    this.accessToken_stored = localStorage.getItem('accessToken');
    const headers = new HttpHeaders({
      'Authorization': `Bearer ${this.accessToken_stored}`, // token de acesso obtido no login
    });

    return this.http.get(`${environment.baseUrl}/login/profissional/token`, { headers });
  }

  esqueciSenha(email: string, perfil: string): Observable<any> {
    const url = `${environment.baseUrl}/login/resetSenha`;
    const body = new HttpParams()
      .set('email', email)
      .set('perfil', perfil);

    const headers = new HttpHeaders({
        'Content-Type': 'application/x-www-form-urlencoded',
    });


    return this.http.post(url, body.toString(), { headers });
  }



}
