import { Component, OnInit } from '@angular/core';
import { Paciente, PacienteResponse } from 'src/app/models/Paciente.models';
import { CadastroPacienteService } from 'src/app/services/cadastro-paciente.service';
import { LoginUsuarioService } from 'src/app/services/login-usuario.service';

@Component({
  selector: 'app-meus-dados-paciente',
  templateUrl: './meus-dados-paciente.component.html',
  styleUrls: ['./meus-dados-paciente.component.css']
})
export class MeusDadosPacienteComponent implements OnInit {

  nome: string = '';
  telefone: string = '';
  emailPaciente: string = '';
  senhaPaciente: string = '';
  dataNascimentoPaciente: Date = new Date();
  paciente: any;
  idPessoa: any;
  constructor(private loginService: LoginUsuarioService, private cadastroPaciente: CadastroPacienteService) { }

  ngOnInit(): void {
    this.loginService.getPerfilPessoa().subscribe(
      (data: PacienteResponse) => {
        this.paciente = data;
        this.idPessoa = this.paciente.idPessoa;
        this.nome = this.paciente.nome;
        this.telefone = this.paciente.telefone;
        this.emailPaciente = this.paciente.email;
        this.dataNascimentoPaciente = this.paciente.dataNascimento;
        this.senhaPaciente = this.loginService.getSenha();
      },
      error => {
        console.error('Erro ao buscar especialistas:', error);
      }
    );
  }

  onCampoAlterado(campo: string) {
    console.log(`Campo ${campo} alterado. Novo valor: `);
    // Aqui você pode realizar as ações que deseja quando um campo é alterado
    // Por exemplo, você pode chamar a função alterar()
  }
  alterar(){
    const paciente_alterado: PacienteResponse ={
      idPessoa: this.idPessoa,
      nome: this.nome,
      telefone: this.telefone,
      email: this.emailPaciente,
      dataNascimento: this.dataNascimentoPaciente,
      senha: this.senhaPaciente,
      sexo: this.paciente.sexo,
      administrador: this.paciente.administrador
    }
    console.log(paciente_alterado);

    this.cadastroPaciente.update(paciente_alterado).subscribe(
      () => {
        console.log("Atualizado com sucesso");
      },
      error => {
        console.error('Erro ao buscar especialistas:', error);
      }
    );
  }

}
