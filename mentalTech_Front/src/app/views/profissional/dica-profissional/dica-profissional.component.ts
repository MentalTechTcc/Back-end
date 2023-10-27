import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { DicaSaudeService } from 'src/app/services/dica-saude.service';
import { Dica } from 'src/app/models/Dica.models';
import {LoginUsuarioService} from 'src/app/services/login-usuario.service'

@Component({
  selector: 'app-dica-profissional',
  templateUrl: './dica-profissional.component.html',
  styleUrls: ['./dica-profissional.component.css']
})
export class DicaProfissionalComponent implements OnInit {
  dicaForm: FormGroup = new FormGroup({});
  listaDicas: Dica[] = [];
  profissional: any = {};
  sucesso: boolean = false;
  erro: string = '';

  constructor(
    private fb: FormBuilder,
    private dicaService: DicaSaudeService,
    private loginService: LoginUsuarioService,
  ) { this.dicaForm = this.fb.group({
    cpfProfissional: ['', Validators.required],
    descricaoDica: ['', Validators.required],
    dataCadastro: this.formatarData(new Date()),
  });}

  ngOnInit(): void {
    this.loginService.getPerfilProfissional().subscribe(
      (data: any) => {
        this.profissional = data;
        /*console.log('aquiiii'+this.profissional.cpf); */
        this.initForm();
        /*console.log(data);*/
        this.carregarDicas();
      },
      (error) => {
        console.log('error');
      }
    );
    this.initForm();
    
  }
  
  initForm() {
    this.dicaForm = this.fb.group({
      cpfProfissional: this.profissional.cpf,
      descricaoDica: ['', Validators.required],
      dataCadastro: this.formatarData(new Date()),
    });
  }
  

  onSubmit() {
    if (this.dicaForm.valid) {
      const dicaData = this.dicaForm.value;

      this.dicaService.cadastrarDica(dicaData).subscribe(
        () => {
          this.sucesso = true;
          this.erro = ''; // Limpa
          this.dicaForm.reset();
          this.ngOnInit();
        },
        (error) => {
          this.sucesso = false;
          this.erro = 'Ocorreu um erro ao enviar a avaliação. Por favor, tente novamente.';
        }
      );
    }
  }
  carregarDicas() {
    this.dicaService.listar().subscribe(dicas => {
      this.listaDicas = dicas;
    });
  }

  formatarData(data: Date): string {
    const yyyy = data.getFullYear();
    const mm = (data.getMonth() + 1).toString().padStart(2, '0');
    const dd = data.getDate().toString().padStart(2, '0');
    return `${yyyy}-${mm}-${dd}`;
  }
}
