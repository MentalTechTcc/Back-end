import { Component, OnInit } from '@angular/core';
import { Profissional } from 'src/app/models/Profissional.models';
import { LoginUsuarioService } from 'src/app/services/login-usuario.service';

@Component({
  selector: 'app-meus-dados-profissional',
  templateUrl: './meus-dados-profissional.component.html',
  styleUrls: ['./meus-dados-profissional.component.css']
})
export class MeusDadosProfissionalComponent implements OnInit {

  nome: string = '';
  telefone: string = '';
  emailProfissional: string = '';
  senhaProfissional: string = '';
  codigoProfissional: string= '';
  dataNascimentoProfissional: Date = new Date();
  Profissional: any;

  constructor(private loginService: LoginUsuarioService) { }

  ngOnInit(): void {
    this.loginService.getPerfilProfissional().subscribe(
      (data: Profissional) => {
        this.Profissional = data;

        this.nome = this.Profissional.nome;
        this.telefone = this.Profissional.telefone;
        this.emailProfissional = this.Profissional.email;
        this.codigoProfissional= this.Profissional.codigoProfissional;
        this.dataNascimentoProfissional = this.Profissional.dataNascimento;
      },
      error => {
        console.error('Erro ao buscar especialistas:', error);
      }
    );
  }

}
