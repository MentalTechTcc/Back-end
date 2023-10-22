import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { DicaSaudeService } from 'src/app/services/dica-saude.service';
import { Dica } from 'src/app/models/Dica.models';

@Component({
  selector: 'app-dica-profissional',
  templateUrl: './dica-profissional.component.html',
  styleUrls: ['./dica-profissional.component.css']
})
export class DicaProfissionalComponent implements OnInit {
  dicaForm: FormGroup = new FormGroup({});
  listaDicas: Dica[] = [];

  constructor(
    private fb: FormBuilder,
    private dicaService: DicaSaudeService
  ) { }

  ngOnInit(): void {
    this.initForm();
    this.carregarDicas();
  }

  initForm() {
    this.dicaForm = this.fb.group({
      descricaoDica: ['', Validators.required],
    });
  }
  

  onSubmit() {
    if (this.dicaForm.valid) {
      const dicaData = this.dicaForm.value;

      this.dicaService.cadastrarDica(dicaData).subscribe(response => {
      
      });
    }
  }
  carregarDicas() {
    this.dicaService.listar().subscribe(dicas => {
      this.listaDicas = dicas;
    });
  }
}
