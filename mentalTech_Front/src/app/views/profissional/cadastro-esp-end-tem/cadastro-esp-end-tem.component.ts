// cadastro-esp-end-tem.component.ts
import { Component } from '@angular/core';
import { Endereco } from 'src/app/models/Endereco.models';
import { Especialidade } from 'src/app/models/Especialidade.models';
import { Tematica, TematicaResponse } from 'src/app/models/Tematica.models';
import { EnderecoServiceService } from 'src/app/services/endereco-service.service';
import { EspecialidadeServiceService } from 'src/app/services/especialidade-service.service';
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

  tematicas: TematicaResponse[] = []

  constructor(private serviceEspecialidade : EspecialidadeServiceService, private serviceTematica: TematicaServiceService, private serviceEndereco: EnderecoServiceService){

  }


  ngOnInit(): void {
    this.serviceEspecialidade.listar().subscribe(
      (data: Especialidade[]) => {
        this.especialidades = data;
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

  selecionarEspecialidades() {
    // Adicione a lógica para processar as especialidades selecionadas
    console.log('Especialidades selecionadas');
  }

  onChangePossuiEndereco(value: string) {
    this.possuiEndereco = value;
  }

  adicionarEndereco() {
    // Lógica para adicionar um novo endereço ao array
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
    // Lógica para adicionar um novo endereço ao array
    this.novas_tematicas.push({
      nomeTematica: ''
    });
  }
}
