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
  profissionalRequestId: any;
  idPessoa:any;
  senha: string='';
  profissionalResult: any;

  constructor(
    private loginService: LoginUsuarioService,
    private atualizacaoService: AtualizacaoDadosProfisionalService
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
      }
    );
  }


  deletarDados(): void { // deleta consulta pela agenda
    if (confirm('Tem certeza de que deseja excluir sua conta?')) {
      // this.consultaService.deletar(idAgenda).subscribe(
      //   () => {
      //     this.carregarConsulta(this.pessoa.idPessoa);
      //     console.log('primeiro id: ' + idAgenda);
      //     this.atualizaAgendaMarcacao(idAgenda);


      //   },
      //   (error) => {
      //     console.error('Erro ao excluir a agenda:', error);
      //   }
      // );
    }
  }

}
