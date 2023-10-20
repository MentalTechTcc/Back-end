import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class LoginUsuarioService {

  constructor() { }

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
}
