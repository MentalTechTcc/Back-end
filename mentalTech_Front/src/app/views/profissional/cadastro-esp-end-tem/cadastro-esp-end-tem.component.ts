import { Component } from '@angular/core';
import { Endereco, EnderecoResponse, ProfissionalTemEndereco } from 'src/app/models/Endereco.models';
import { Especialidade, ProfissionalTrataEspecialidade } from 'src/app/models/Especialidade.models';
import { ProfissionalTrataTematica, Tematica, TematicaResponse } from 'src/app/models/Tematica.models';
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
  enderecos_cadastrados: EnderecoResponse[] = [];
  tematicas_cadastradas: TematicaResponse[] = [];

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

      for(const endereco of this.enderecos){
        this.serviceEndereco.create(endereco).subscribe(
          response => {
            console.log('Cadastro bem-sucedido:', response);
          },
          error => {
            console.error('Erro no cadastro:', error);
          }
        );

      }

      for(const tem of this.novas_tematicas){
        this.serviceTematica.create(tem).subscribe(
          response => {
            console.log('Cadastro bem-sucedido:', response);
          },
          error => {
            console.error('Erro no cadastro:', error);
          }
        );
      }

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

      //Parte que envia pro backend para cadastrar os enderecos dos proficionais
      this.serviceEndereco.listar().subscribe(
        (data: EnderecoResponse[]) => {
          this.enderecos_cadastrados = data
          console.log(this.enderecos_cadastrados);

          for(const endereco of this.enderecos){
            const id = this.serviceEndereco.getId(this.enderecos_cadastrados, endereco.cep, endereco.numero);
            const profissional_endereco: ProfissionalTemEndereco = {
              idEndereco: id,
              cpfProfissional: cpf
            }

            this.serviceEndereco.createEnderecoProfissional(profissional_endereco).subscribe(
              response => {
                console.log('Cadastro bem-sucedido:', response);
              },
              error => {
                console.error('Erro no cadastro:', error);
              }
            );
          }
        },
        error => {
          console.error('Erro ao buscar especialistas:', error);
        }
      );

      this.serviceTematica.listar().subscribe(
        (data: TematicaResponse[]) => {
          this.tematicas_cadastradas = data
          console.log(this.tematicas_cadastradas);
        //   for(const tematica of this.novas_tematicas){
        //     const id = this.serviceTematica.getId(this.tematicas_cadastradas, tematica);

        //     this.tematicas.push({
        //       idTematicasPrincipais:id,
        //       nomeTematica: tematica
        //     })
        //   }

        //   for(const tematica of this.tematicas){
        //     const profissional_tematica : ProfissionalTrataTematica ={
        //       idTematicasPrincipais: tematica.idTematicasPrincipais,
        //       cpfProfissional: cpf
        //     }

        //     this.serviceTematica.createTematicaProfissional(profissional_tematica).subscribe(
        //       response => {
        //         console.log('Cadastro bem-sucedido:', response);
        //       },
        //       error => {
        //         console.error('Erro no cadastro:', error);
        //       }
        //     );
        //   }
        },
        error => {
           console.error('Erro ao buscar especialistas:', error);
        }
      );








    }
  }
}
