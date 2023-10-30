import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { Endereco, EnderecoResponse, ProfissionalTemEndereco } from 'src/app/models/Endereco.models';
import { Especialidade, ProfissionalTrataEspecialidade } from 'src/app/models/Especialidade.models';
import { ProfissionalTrataTematica, Tematica, TematicaResponse } from 'src/app/models/Tematica.models';
import { CadastroProfissionalService } from 'src/app/services/cadastro-profissional.service';
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
    private serviceLogin: LoginUsuarioService,
    private cadastroProfissionalService: CadastroProfissionalService,
    private router: Router
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

  adicionaEspecialidade(cpf: string){
    // Filtrar apenas as especialidades selecionadas
    const especialidadesSelecionadas = this.especialidades
      .filter(especialidade => especialidade.selecionada)
      .map(especialidade => ({
        idEspecialidade: especialidade.idEspecialidade,
        cpfProfissional: cpf
      }));

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

  adicionaTematicasSelecionadas(cpf: string){
    const tematicasSelecionadas = this.tematicas
    .filter(tematica => tematica.selecionada)
    .map(tematica => ({
      idTematicasPrincipais: tematica.idTematicasPrincipais,
      cpfProfissional: cpf
    }));

    for (const tematica of tematicasSelecionadas) {
      this.serviceTematica.createTematicaProfissional(tematica).subscribe(
        response => {
          console.log('Cadastro bem-sucedido:', response);
        },
        error => {
          console.error('Erro no cadastro:', error);
        }
      );
    }
  }

  adicionaTematicasAdicionadas(cpf: string){
    for(const tem of this.novas_tematicas){
      this.serviceTematica.create(tem).subscribe(
        response => {
          console.log('Cadastro bem-sucedido:', response);

          this.serviceTematica.listar().subscribe(
            (data: TematicaResponse[]) => {
              this.tematicas_cadastradas = data
              for(const tematica of this.novas_tematicas){

                console.log("aqui:" + tematica.nomeTematica);

                const id = this.serviceTematica.getId(this.tematicas_cadastradas, tematica.nomeTematica);

                const profissional_tematica : ProfissionalTrataTematica ={
                  idTematicasPrincipais: id,
                  cpfProfissional: cpf
                }

                this.serviceTematica.createTematicaProfissional(profissional_tematica).subscribe(
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

        },
        error => {
          console.error('Erro no cadastro:', error);
        }
      );
    }


  }

  adicionaEnderecoBanco(cpf:string){
    for(const endereco of this.enderecos){
      this.serviceEndereco.create(endereco).subscribe(
        response => {
          console.log('Cadastro bem-sucedido:', response);

          this.serviceEndereco.listar().subscribe(
            (data: EnderecoResponse[]) => {
              this.enderecos_cadastrados = data

              for(const endereco_aux of this.enderecos){
                const id = this.serviceEndereco.getId(this.enderecos_cadastrados, endereco_aux.cep, endereco_aux.numero);

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

        },
        error => {
          console.error('Erro no cadastro:', error);
        }
      );
    }
  }

  enviar() {
    const profissional = this.cadastroProfissionalService.getProfissional();

    this.cadastroProfissionalService.create(profissional).subscribe(
      response => {
        console.log('Cadastro bem-sucedido:', response);

        this.adicionaEspecialidade(profissional.cpf);

        this.adicionaTematicasSelecionadas(profissional.cpf);

        this.adicionaTematicasAdicionadas(profissional.cpf);

        this.adicionaEnderecoBanco(profissional.cpf);

        this.router.navigate(['/login']);

      },
      error => {
        console.error('Erro no cadastro:', error);
      }
      );


  }
}

