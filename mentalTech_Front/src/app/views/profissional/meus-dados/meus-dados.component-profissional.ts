import { Component, OnInit } from '@angular/core';
import { Profissional, ProfissionalRequestId } from 'src/app/models/Profissional.models';
import { LoginUsuarioService } from 'src/app/services/login-usuario.service';
import { AtualizacaoDadosProfisionalService } from 'src/app/services/atualizacao-dados-profisional.service';
import { CadastroProfissionalService } from 'src/app/services/cadastro-profissional.service';
import { Router } from '@angular/router';

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
  profissionalRequestId: any;
  idPessoa:any;
  senha: string='';
  profissionalResult: any;
  errorMessage: string = '';


  constructor(
    private loginService: LoginUsuarioService,
    private atualizacaoService: AtualizacaoDadosProfisionalService,
    private profissionalService: CadastroProfissionalService,
    private route: Router
  ) {}

  ngOnInit(): void {
    this.loginService.getPerfilProfissional().subscribe(
      (data: Profissional) => {

        this.profissionalResult = data;
        this.nome = this.profissionalResult.nome;
        this.telefone = this.profissionalResult.telefone;
        this.emailProfissional = this.profissionalResult.email;
        this.codigoProfissional = this.profissionalResult.codigoProfissional;
        this.dataNascimentoProfissional = this.profissionalResult.dataNascimento;
        this.idPessoa= this.profissionalResult.idPessoa
        this.senha = this.loginService.getSenha();

        this.profissionalRequestId = {
          cpf: this.profissionalResult.cpf,
          administrador: this.profissionalResult.administrador,
          sexo: this.profissionalResult.sexo,
          descricaoProfissional: this.profissionalResult.descricaoProfissional
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
      senha: this.senha,
      dataNascimento: this.dataNascimentoProfissional,
      telefone: this.telefone,
      email: this.emailProfissional,
      administrador: this.profissionalResult.administrador,
      sexo: this.profissionalResult.sexo,
      codigoProfissional: this.codigoProfissional,
      descricaoProfissional: this.profissionalResult.descricaoProfissional,
      cpf: this.profissionalResult.cpf,
      pix: this.profissionalResult.pix,
      idPessoa: this.idPessoa
    };


    const dadosAtualizados = { ...this.profissionalRequestId, ...dadosFormulario };

    console.log(dadosAtualizados);

    this.atualizacaoService.atualizarProfissional(dadosFormulario).subscribe(
      (response) => {
        console.log('Dados atualizados com sucesso:', response);
      },
      (error) => {
        console.error('Erro na atualização de dados:', error);
        this.errorMessage = 'Falha no login. Verifique seu CPF e senha.';
        this.delayErrorMessageRemoval();
      }
    );
  }


  deletarDados(): void { // deleta consulta pela agenda
    if (confirm('Tem certeza de que deseja excluir sua conta?')) {
      console.log("id:  " + this.idPessoa);
      this.profissionalService.deletar(this.idPessoa).subscribe(
        () => {
          this.route.navigate(['/home']);


        },
        (error) => {
          console.error('Erro ao excluir os dados:', error);
          this.errorMessage = 'Falha no login. Verifique seu CPF e senha.';
          this.delayErrorMessageRemoval();
        }
      );
    }
  }

  delayErrorMessageRemoval(): void {
    setTimeout(() => {
      this.errorMessage = ''; // Remove a mensagem após alguns segundos
    }, 5000); // 5000 milissegundos = 5 segundos, ajuste conforme necessário
  }
}
