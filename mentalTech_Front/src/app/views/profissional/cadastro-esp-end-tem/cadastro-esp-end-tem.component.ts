import { Component } from '@angular/core';
import { Endereco } from 'src/app/models/Endereco.models';
import { Especialidade, ProfissionalTrataEspecialidade } from 'src/app/models/Especialidade.models';
import { Tematica, TematicaResponse } from 'src/app/models/Tematica.models';
import { EnderecoServiceService } from 'src/app/services/endereco-service.service';
import { EspecialidadeServiceService } from 'src/app/services/especialidade-service.service';
import { LoginUsuarioService } from 'src/app/services/login-usuario.service';
import { TematicaServiceService } from 'src/app/services/tematica-service.service';

@Component({
  selector: 'app-cadastro-esp-end-tem',
  templateUrl: './cadastro-esp-end-tem.component.html',
  styleUrls: ['./cadastro-esp-end-tem.component.css']
})
export class CadastroEspEndTemComponent {
  temEndereco: string = 'Nao';
  possuiEndereco: string = 'Nao';
  novas_tematicas: any[] = [];

  especialidades: Especialidade[] = [];
  enderecos: Endereco[] = [];
  endereco = {
    cep: '',
    estado: '',
    cidade: '',
    bairro: '',
    numero: 0,
    complemento: ''
  };

  tematicas: TematicaResponse[] = [];

  constructor(
    private serviceEspecialidade: EspecialidadeServiceService,
    private serviceTematica: TematicaServiceService,
    private serviceEndereco: EnderecoServiceService,
    private serviceLogin: LoginUsuarioService
  ) {}

  ngOnInit(): void {
    this.serviceEspecialidade.listar().subscribe(
      (data: Especialidade[]) => {
        this.especialidades = data.map(especialidade => ({ ...especialidade, selecionada: false }));
        console.log(this.especialidades);
      },
      error => {
        console.error('Erro ao buscar especialistas:', error);
      }
    );

    this.serviceTematica.listar().subscribe(
      (data: TematicaResponse[]) => {
        this.tematicas = data;
        console.log(this.tematicas);
      },
      error => {
        console.error('Erro ao buscar especialistas:', error);
      }
    );
  }

  toggleEndereco() {
    this.temEndereco = this.temEndereco === 'Sim' ? 'Nao' : 'Sim';
  }

  adicionarEndereco() {
    this.enderecos.push({
      cep: '',
      estado: '',
      cidade: '',
      bairro: '',
      numero: 0,
      complemento: ''
    });
    console.log(this.enderecos);
  }

  adicionarTematica() {
    this.novas_tematicas.push({
      nomeTematica: ''
    });
    console.log(this.novas_tematicas);
  }

  enviar() {
    const cpf = this.serviceLogin.getCpfProfissional();

    console.log('aquii cpf: ' + cpf);


    if (cpf != null) {
      // Filtrar apenas as especialidades selecionadas
      const especialidadesSelecionadas = this.especialidades
        .filter(especialidade => especialidade.selecionada)
        .map(especialidade => ({
          idEspecialidade: especialidade.idEspecialidade,
          cpfProfissional: cpf
        }));

      console.log(especialidadesSelecionadas);
      console.log(this.novas_tematicas);
      console.log(this.enderecos);
      // Enviar para o backend apenas as especialidades selecionadas
      for (const especialidade of especialidadesSelecionadas) {
        this.serviceEspecialidade.createEspecialidadeProfissional(especialidade).subscribe(
          response => {
            console.log('Cadastro bem-sucedido:', response);
          },
          error => {
            console.error('Erro no cadastro:', error);
          }
        );
      }
    }
  }
}
