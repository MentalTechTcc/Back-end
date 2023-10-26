import { Component, OnInit } from '@angular/core';
import { Profissional, ProfissionalRequestId } from 'src/app/models/Profissional.models';
import { LoginUsuarioService } from 'src/app/services/login-usuario.service';
import { AtualizacaoDadosProfisionalService } from 'src/app/services/atualizacao-dados-profisional.service';

@Component({
  selector: 'app-meus-dados-profissional',
  templateUrl: './meus-dados-profissional.component.html',
  styleUrls: ['./meus-dados-profissional.component.css']
})
export class MeusDadosProfissionalComponent implements OnInit {
  nome: string = '';
  telefone: string = '';
  emailProfissional: string = '';
  dataNascimentoProfissional: Date = new Date();
  codigoProfissional: string = '';
  Profissional: any;
  ProfissionalRequestId: any;
  idPessoa:number=0;
  
  constructor(
    private loginService: LoginUsuarioService,
    private atualizacaoService: AtualizacaoDadosProfisionalService
  ) {}

  ngOnInit(): void {
    this.loginService.getPerfilProfissional().subscribe(
      (data: Profissional) => {
        this.Profissional = data;
        this.nome = this.Profissional.nome;
        this.telefone = this.Profissional.telefone;
        this.emailProfissional = this.Profissional.email;
        this.codigoProfissional = this.Profissional.codigoProfissional;
        this.dataNascimentoProfissional = this.Profissional.dataNascimento;
        this.idPessoa= this.Profissional.idPessoa


        this.ProfissionalRequestId = {
          cpf: this.Profissional.cpf,
          senha: this.Profissional.senha,
          administrador: this.Profissional.administrador,
          sexo: this.Profissional.sexo,
          descricaoProfissional: this.Profissional.descricaoProfissional
        };
      },
      (error) => {
        console.error('Erro ao buscar especialistas:', error);
      }
    );
  }

  atualizarProfissional() {

    const dadosFormulario = {
      nome: this.nome,
      telefone: this.telefone,
      email: this.emailProfissional,
      dataNascimento: this.dataNascimentoProfissional,
      codigoProfissional: this.codigoProfissional,
      idPessoa: this.idPessoa,
    };


    const dadosAtualizados = { ...this.ProfissionalRequestId, ...dadosFormulario };

    this.atualizacaoService.atualizarProfissional(dadosAtualizados).subscribe(
      (response) => {
        console.log('Dados atualizados com sucesso:', response);
      },
      (error) => {
        console.error('Erro na atualização de dados:', error);
      }
    );
  }
}
