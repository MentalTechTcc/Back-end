import { Component, OnInit } from '@angular/core';
import { Dica } from 'src/app/models/Dica.models';
import { DicaSaudeService } from 'src/app/services/dica-saude.service';

@Component({
  selector: 'app-dicas-paciente',
  templateUrl: './dicas-paciente.component.html',
  styleUrls: ['./dicas-paciente.component.css']
})
export class DicasPacienteComponent implements OnInit {

  dicas: Dica[] = [];

  constructor(private service: DicaSaudeService) {}

  ngOnInit(): void {
    this.service.listar().subscribe(
      (data: Dica[]) => {
        this.dicas = data;
      },
      error => {
        console.error('Erro ao buscar dicas:', error);
      }
    );
  }

}
