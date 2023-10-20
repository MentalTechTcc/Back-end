import { Component } from '@angular/core';
import { LoginUsuarioService } from './services/login-usuario.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  opcao: string = 'paciente'; // Inicializa com 'paciente'
  fezLogin: boolean = false;

  constructor(private loginService: LoginUsuarioService) {}
  ngOnInit() {
    this.opcao = this.loginService.getPerfil();
    this.fezLogin = this.loginService.getFezLogin();
  }
}
