import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Agenda } from 'src/app/models/Agenda.models';
import {LoginUsuarioService} from 'src/app/services/login-usuario.service'
import {CadastroAgendaProfissionalService} from 'src/app/services/cadastro-agenda-profissional.service'
import { ProfissionalTemEndereco } from 'src/app/models/Endereco.models';
import {EnderecoServiceService} from 'src/app/services/endereco-service.service'

@Component({
  selector: 'app-cadastro-agenda-profissional',
  templateUrl: './cadastro-agenda-profissional.component.html',
  styleUrls: ['./cadastro-agenda-profissional.component.css']
})
export class CadastroAgendaProfissionalComponent implements OnInit {
  disponibilidadeForm: FormGroup = new FormGroup({});
  cpfProfissional:string = '';
  profissional: any = {};
  sucesso: boolean = false;
  erro: string = '';
  enderecosDisponiveis: ProfissionalTemEndereco[] = [];
  enderecoSelecionadoId: number | null = null;

  constructor(
    private fb: FormBuilder,
    private loginService: LoginUsuarioService,
    private agendaService: CadastroAgendaProfissionalService,
    private enderecoService: EnderecoServiceService
    ) {
   this.disponibilidadeForm = this.fb.group({
    cpfProfissional: ['', Validators.required],
    data: ['2023-01-01', Validators.required],
    hora: ['00:00', Validators.required],
    duracao: [1, Validators.required],
    modalidadeAtendimento: [2, Validators.required],
    ocupado:false,
    valorProposto:[50.0, Validators.required],
    linkPagamento: ''
  });}

  ngOnInit(): void {
    this.loginService.getPerfilProfissional().subscribe(
      (data: any) => {
        this.profissional = data;
        this.initForm();
        console.log(data);
      /*  this.carregarAgenda();
        this.carregarProfissionais(); */
        this.carregarEnderecosDisponiveis();
      },
      (error) => {
        console.log('error');
      }
    );
  }

  initForm() {
    this.disponibilidadeForm = this.fb.group({
      cpfProfissional: this.profissional.cpf,
      data: [null, Validators.required],
      hora: [null, Validators.required],
      duracao: [null, Validators.required],
      modalidadeAtendimento: [2, Validators.required],
      ocupado:false,
      valorProposto:[50.0, Validators.required],
      linkPagamento:'',
      idEndereco: this.enderecoSelecionadoId
    });
  }

  onSubmit() {
    if (this.disponibilidadeForm.valid) {
      console.log( this.disponibilidadeForm.value)
      const agendaData: Agenda = this.disponibilidadeForm.value;
      console.log('apertou')
      /*console.log(this.disponibilidadeForm.value)*/
      agendaData.modalidadeAtendimento = +agendaData.modalidadeAtendimento;
      this.agendaService.cadastrarAgenda(agendaData).subscribe(
        () => {
          this.sucesso = true;
          this.erro = ''; // Limpa
          this.disponibilidadeForm.reset();
          this.ngOnInit();
        },
        (error) => {
          this.sucesso = false;
          this.erro = 'Ocorreu um erro ao enviar a avaliação. Por favor, tente novamente.';
        }
      );
    }
  }

  carregarEnderecosDisponiveis() {
    this.enderecoService.listarEnderecoProfissional(this.profissional.cpf).subscribe((enderecos) => {
      this.enderecosDisponiveis = enderecos;
  
      this.enderecosDisponiveis.forEach((endereco) => {
        this.enderecoService.listarEnderecoPorId(endereco.idEndereco).subscribe((detalhesEndereco) => {
       
          endereco.detalhes = detalhesEndereco;
        });
      });
    });
  }


  selecionarEndereco(idEndereco: number) {
    this.enderecoSelecionadoId = idEndereco;
  }

}



