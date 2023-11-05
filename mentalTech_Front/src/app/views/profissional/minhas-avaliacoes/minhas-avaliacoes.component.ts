import { Component, OnInit } from '@angular/core';
import {LoginUsuarioService} from 'src/app/services/login-usuario.service'
import {AvaliacaoProfissionalService} from 'src/app/services/avaliacao-profissional.service'
import { Avaliacao, AvaliacaoRequestId} from 'src/app/models/Avaliacao.models';

@Component({
  selector: 'app-minhas-avaliacoes',
  templateUrl: './minhas-avaliacoes.component.html',
  styleUrls: ['./minhas-avaliacoes.component.css']
})
export class MinhasAvaliacoesComponent implements OnInit {
  cpfProfissional:string = '';
  profissional: any = {};
  listaAvaliacoes: AvaliacaoRequestId[] = [];
  observacoesExpandidas: boolean = false;

  constructor(
    private loginService: LoginUsuarioService,
    private avaliacaoService: AvaliacaoProfissionalService,
  ) { }

  ngOnInit(): void {
    this.loginService.getPerfilProfissional().subscribe(
      (data: any) => {
        this.profissional = data;
    
        this.carregarAgenda();
      },
      (error) => {
        console.log('error');
      }
    );
  }

  carregarAgenda() {
   /* console.log(this.profissional.cpf)*/
    this.avaliacaoService.listarPorCpfProfissional(this.profissional.cpf.toString()).subscribe(avaliacoes => {
      this.listaAvaliacoes = avaliacoes;
      console.log(this.listaAvaliacoes);
    });
    
  }

  toggleObservacoes() {
    this.observacoesExpandidas = !this.observacoesExpandidas;
  }
  
  

}
