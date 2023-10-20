// cadastro-esp-end-tem.component.ts
import { Component } from '@angular/core';

@Component({
  selector: 'app-cadastro-esp-end-tem',
  templateUrl: './cadastro-esp-end-tem.component.html',
  styleUrls: ['./cadastro-esp-end-tem.component.css']
})
export class CadastroEspEndTemComponent {
  temEndereco: string = 'Nao';
  possuiEndereco: string = 'Nao';

  especialidades = [
    { id: 'esp1', nome: 'Psicologo' },
    { id: 'esp2', nome: 'Psiquiatra' },
    // Adicione mais especialidades conforme necessário
  ];

  endereco = {
    cep: '',
    estado: '',
    cidade: '',
    bairro: '',
    numero: '',
    complemento: ''
  };

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
}
