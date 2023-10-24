import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { AvaliacaoPacienteService } from 'src/app/services/avaliacao-paciente.service';
import { CadastroProfissionalService } from 'src/app/services/cadastro-profissional.service';
import { Avaliacao } from 'src/app/models/Avaliacao.models';
import { Profissional } from 'src/app/models/Profissional.models';
import {LoginUsuarioService} from 'src/app/services/login-usuario.service'
import {Paciente} from 'src/app/models/Paciente.models';


@Component({
  selector: 'app-avaliacao-paciente',
  templateUrl: './avaliacao-paciente.component.html',
  styleUrls: ['./avaliacao-paciente.component.css']
})
export class AvaliacaoPacienteComponent implements OnInit {
  avaliacaoForm: FormGroup;
  listaAvaliacao: Avaliacao[] = [];
  listaProfissionais: Profissional[] = [];
  pessoa: any = {};
  timeZone = 'UTC'; 

  constructor(
    private fb: FormBuilder,
    private avaliacaoService: AvaliacaoPacienteService,
    private profissionalService: CadastroProfissionalService,
    private loginService: LoginUsuarioService,
  ) {
    this.avaliacaoForm = this.fb.group({
      cpfProfissional: ['', Validators.required],
      idPessoa: [0, Validators.required],
      notaGeral: [0, [Validators.required, Validators.min(0), Validators.max(10)]],
      notaPontualidade: [0, [Validators.required, Validators.min(0), Validators.max(10)]],
      notaAtendimento: [0, [Validators.required, Validators.min(0), Validators.max(10)]],
      observacoes: ['', Validators.required],
      dataCadastro: this.formatarData(new Date()),
    });
  }

  ngOnInit(): void {
    this.loginService.getPerfilPessoa().subscribe(
      (data: any) => {
        this.pessoa = data;
        console.log(this.pessoa.idPessoa); // Agora você pode acessar this.pessoa.idPessoa
        this.initForm();
        console.log(data);
        this.carregarAvaliacao();
        this.carregarProfissionais(); // lista de profs
      },
      (error) => {
        console.log('error');
      }
    );
  }
 
  initForm() {
    this.avaliacaoForm = this.fb.group({
      cpfProfissional: ['', Validators.required],
      idPessoa: this.pessoa.idPessoa,
      notaGeral: [0, Validators.required],
      notaPontualidade: [0, Validators.required],
      notaAtendimento: [0, Validators.required],
      observacoes: ['', Validators.required],
      dataCadastro: this.formatarData(new Date()),
    });
  }

  onSubmit() {
    if (this.avaliacaoForm.valid) {
      const avaliacaoData: Avaliacao = this.avaliacaoForm.value;
      this.avaliacaoService.cadastrarAvaliacao(avaliacaoData).subscribe(() => {
        this.avaliacaoForm.reset();
        /*this.carregarAvaliacao();*/
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


  formatarData(data: Date): string {
    const yyyy = data.getFullYear();
    const mm = (data.getMonth() + 1).toString().padStart(2, '0');
    const dd = data.getDate().toString().padStart(2, '0');
    return `${yyyy}-${mm}-${dd}`;
  }
}
