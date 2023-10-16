import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class CadastroUsuarioService {

  private escolhaPerfil: string = '';

  setEscolhaPerfil(escolha: string) {
    this.escolhaPerfil = escolha;
  }

  getEscolhaPerfil(): string {
    return this.escolhaPerfil;
  }
}
