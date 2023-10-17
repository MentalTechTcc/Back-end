import { Component, OnInit } from '@angular/core';
import { Profissional } from 'src/app/models/Profissional.models';
import { CadastroProfissionalService } from 'src/app/services/cadastro-profissional.service';
import { CadastroUsuarioService } from 'src/app/services/cadastro-usuario.service';

@Component({
  selector: 'app-cadastro-profissional',
  templateUrl: './cadastro-profissional.component.html',
  styleUrls: ['./cadastro-profissional.component.css']
})
export class CadastroProfissionalComponent implements OnInit {

  escolhaPerfil: string = '';
  nome: string = '';
  senha: string = '';
  dataNascimento: Date = new Date(); // Se você quiser manter como string
  telefone: string = '';
  email: string= '';
  administrador: boolean=false;
  genero: number = 1;
  codigoProfissional: string = '';
  descricaoProfissional: string = '';
  cpf: string = '';

  constructor(private cadastroService: CadastroUsuarioService, private cadastroProfissionalService: CadastroProfissionalService) {
  }

  ngOnInit() {
    this.escolhaPerfil = this.cadastroService.getEscolhaPerfil();
    console.log('Escolha de perfil recebida:', this.escolhaPerfil);
  }
  cadastrar() {

    if (this.escolhaPerfil === 'Profissional') {

      const profissional: Profissional = {
        nome: this.nome,
        telefone: this.telefone,
        email: this.email,
        senha: this.senha,
        dataNascimento: this.dataNascimento,
        administrador: this.administrador,
        sexo: this.genero,
        codigoProfissional: this.codigoProfissional,
        descricaoProfissional: this.descricaoProfissional,
        cpf: this.cpf
      };

      console.log(profissional);



      // Chame o serviço para cadastrar o paciente
      // this.cadastroPacienteService.create(paciente).subscribe(
      //   response => {
      //     console.log('Cadastro bem-sucedido:', response);
      //   },
      //   error => {
      //     console.error('Erro no cadastro:', error);
      //   }
      // );
    }
  }

  mapearGenero(generoSelecionado: string): void {
    if (generoSelecionado === 'feminino') {
      this.genero = 1;
    } else if (generoSelecionado === 'masculino') {
      this.genero = 2;
    }
  }
}
