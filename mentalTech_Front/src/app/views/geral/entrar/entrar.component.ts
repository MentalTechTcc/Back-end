import { Router } from '@angular/router';
import { LoginUsuarioService } from './../../../services/login-usuario.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-entrar',
  templateUrl: './entrar.component.html',
  styleUrls: ['./entrar.component.css']
})
export class EntrarComponent implements OnInit {

  opcao: string = 'paciente'; // Inicializa com 'paciente'

  constructor(private router: Router, private loginService: LoginUsuarioService) {}

  ngOnInit(): void {
    // Adicione inicializações se necessário
  }

  selectOption(option: string): void {
    this.opcao = option;
  }

  entrar(): void {

    this.loginService.setPerfil(this.opcao);
    this.loginService.setFezLogin(true);
    if (this.opcao === 'paciente') {
      // Navegar para a rota de paciente
      this.router.navigate(['/home-paciente']);
    } else if (this.opcao === 'profissional') {

      // Navegar para a rota de profissional
      this.router.navigate(['/home-profissional']);
    }
  }
}
