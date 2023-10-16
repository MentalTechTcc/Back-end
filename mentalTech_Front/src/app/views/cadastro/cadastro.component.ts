import { Component, OnInit } from '@angular/core';
import { CadastroUsuarioService } from 'src/app/services/cadastro-usuario.service';

@Component({
  selector: 'app-cadastro',
  templateUrl: './cadastro.component.html',
  styleUrls: ['./cadastro.component.css']
})
export class CadastroComponent {

  escolhaPerfil: string = ''; // Certifique-se de inicializar conforme necessário
  nome: string = '';
  cpf: string = '';
  email: string = '';
  senha: string = '';
  dataNascimento: string = '';

  nomePaciente: string = '';
  telefone: string = '';
  emailPaciente: string = '';
  senhaPaciente: string = '';
  dataNascimentoPaciente: string = '';
  genero: string = '';

  constructor(private cadastroService: CadastroUsuarioService) {
  }

  ngOnInit() {
    this.escolhaPerfil = this.cadastroService.getEscolhaPerfil();
    console.log('Escolha de perfil recebida:', this.escolhaPerfil);
  }
  cadastrar() {
    // Implemente a lógica para enviar os dados para o back-end aqui
    // Exemplo fictício usando um serviço ou HttpClient:
    // this.authService.cadastrarUsuario(this.usuario).subscribe(
    //   response => {
    //     console.log('Cadastro bem-sucedido:', response);
    //   },
    //   error => {
    //     console.error('Erro no cadastro:', error);
    //   }
    // );
  }
}
