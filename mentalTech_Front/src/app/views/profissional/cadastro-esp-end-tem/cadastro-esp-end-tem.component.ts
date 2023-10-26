// cadastro-esp-end-tem.component.ts
import { Component } from '@angular/core';
import { Especialidade } from 'src/app/models/Especialidade.models';
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
  enderecos: any[] = [];
  novas_tematicas: any[] = [];


  especialidades: Especialidade[] = [];

  tematicas = [
    { id: 'tem1', nome: 'depressão' },
    { id: 'tem22', nome: 'sindrome do pânico' },
    // Adicione mais tematicas conforme necessário
  ];

  endereco = {
    cep: '',
    estado: '',
    cidade: '',
    bairro: '',
    numero: '',
    complemento: ''
  };

  constructor(private serviceEspecialidade : EspecialidadeServiceService, private serviceTematica: TematicaServiceService){

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
      numero: '',
      complemento: ''
    });
  }

  adicionarTematica() {
    // Lógica para adicionar um novo endereço ao array
    this.novas_tematicas.push({
      nomeTematica: ''
    });
  }
}
