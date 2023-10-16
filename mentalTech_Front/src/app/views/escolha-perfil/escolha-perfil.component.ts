import { Component, OnInit } from '@angular/core';
import { CadastroUsuarioService } from 'src/app/services/cadastro-usuario.service';

@Component({
  selector: 'app-escolha-perfil',
  templateUrl: './escolha-perfil.component.html',
  styleUrls: ['./escolha-perfil.component.css']
})
export class EscolhaPerfilComponent{

  escolhaPerfil: string = ''; // Variável para armazenar a escolha do usuário

  constructor(private cadastroService: CadastroUsuarioService) {}
  // Método para lidar com o clique nos botões
  onButtonClick(tipoPerfil: string) {
    this.escolhaPerfil = tipoPerfil;
    this.cadastroService.setEscolhaPerfil(this.escolhaPerfil);
    console.log('Escolha do usuário:', this.escolhaPerfil);
  }
}
