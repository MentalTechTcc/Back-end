import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { AvaliacaoPacienteService } from 'src/app/services/avaliacao-paciente.service';
import { CadastroProfissionalService } from 'src/app/services/cadastro-profissional.service';
import { Avaliacao } from 'src/app/models/Avaliacao.models';
import { Profissional } from 'src/app/models/Profissional.models';

@Component({
  selector: 'app-avaliacao-paciente',
  templateUrl: './avaliacao-paciente.component.html',
  styleUrls: ['./avaliacao-paciente.component.css']
})
export class AvaliacaoPacienteComponent implements OnInit {
  avaliacaoForm: FormGroup;
  listaAvaliacao: Avaliacao[] = [];
  listaProfissionais: Profissional[] = [];
  
  constructor(
    private fb: FormBuilder,
    private avaliacaoService: AvaliacaoPacienteService,
    private profissionalService: CadastroProfissionalService // Adicione o serviço de profissional
  ) {
    this.avaliacaoForm = this.fb.group({
      cpfProfissional: ['', Validators.required],
      idPessoa: [0, Validators.required],
      notaGeral: [0, [Validators.required, Validators.min(0), Validators.max(10)]],
      notaPontualidade: [0, [Validators.required, Validators.min(0), Validators.max(10)]],
      notaAtendimento: [0, [Validators.required, Validators.min(0), Validators.max(10)]],
      observacoes: ['', Validators.required],
      dataCadastro: new Date(),
    });
  }

  ngOnInit(): void {
    this.carregarAvaliacao();
    this.carregarProfissionais(); // lista de prof
  }

  initForm() {
    this.avaliacaoForm = this.fb.group({
      cpfProfissional: ['', Validators.required],
      idPessoa: [0, Validators.required],
      notaGeral: [0, Validators.required],
      notaPontualidade: [0, Validators.required],
      notaAtendimento: [0, Validators.required],
      observacoes: ['', Validators.required],
      dataCadastro: new Date(),
    });
  }

  onSubmit() {
    if (this.avaliacaoForm.valid) {
      const avaliacaoData: Avaliacao = this.avaliacaoForm.value;
      this.avaliacaoService.cadastrarAvaliacao(avaliacaoData).subscribe(() => {
        this.avaliacaoForm.reset();
        this.carregarAvaliacao();
      });
    }
  }

  carregarAvaliacao() {
    this.avaliacaoService.listar().subscribe(avaliacoes => {
      this.listaAvaliacao = avaliacoes;
    });
  }

  carregarProfissionais() {
    this.profissionalService.listar().subscribe(profissionais => {
      this.listaProfissionais = profissionais;
    });
  }
}
