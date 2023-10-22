import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Agenda } from 'src/app/models/Agenda.models';

@Component({
  selector: 'app-cadastro-agenda-profissional',
  templateUrl: './cadastro-agenda-profissional.component.html',
  styleUrls: ['./cadastro-agenda-profissional.component.css']
})
export class CadastroAgendaProfissionalComponent implements OnInit {
  disponibilidadeForm: FormGroup = new FormGroup({});

  constructor(private fb: FormBuilder) {}

  ngOnInit(): void {
    this.initForm();
  }

  initForm() {
    this.disponibilidadeForm = this.fb.group({
      data: [null, Validators.required],
      hora: [null, Validators.required],
      duracao: [null, Validators.required],
      modalidadeAtendimento: ['presencial', Validators.required],
      ocupado:false
    });
  }

  onSubmit() {
    if (this.disponibilidadeForm.valid) {
      const disponibilidadeData = this.disponibilidadeForm.value as Agenda;
  
    }
  }
}
