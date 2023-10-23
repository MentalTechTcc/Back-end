import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { AvaliacaoPacienteService } from 'src/app/services/avaliacao-paciente.service';
import { Avaliacao } from 'src/app/models/Avaliacao.models';

@Component({
  selector: 'app-avaliacao-paciente',
  templateUrl: './avaliacao-paciente.component.html',
  styleUrls: ['./avaliacao-paciente.component.css']
})
export class AvaliacaoPacienteComponent implements OnInit {
  avaliacaoForm: FormGroup;
  listaAvaliacao: Avaliacao[] = [];

  constructor(
    private fb: FormBuilder,
    private avaliacaoService: AvaliacaoPacienteService,
  ) {
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

  ngOnInit(): void {
    this.carregarAvaliacao();
  }

  onSubmit() {
    if (this.avaliacaoForm.valid) {
      const avaliacaoData: Avaliacao = this.avaliacaoForm.value;
      this.avaliacaoService.cadastrarAvaliacao(avaliacaoData).subscribe(() => {
        // Limpar o formulário ou fazer algo após o envio bem-sucedido.
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
}
