import { Component, OnInit } from '@angular/core';
import { Profissional } from 'src/app/models/Profissional.models';
import { CadastroProfissionalService } from 'src/app/services/cadastro-profissional.service';

@Component({
  selector: 'app-listar-profissionais',
  templateUrl: './listar-profissionais.component.html',
  styleUrls: ['./listar-profissionais.component.css']
})
export class ListarProfissionaisComponent implements OnInit {

  especialistas: Profissional[] = [];

  constructor(private service: CadastroProfissionalService) {}

  ngOnInit(): void {
    this.service.listar().subscribe(
      (data: Profissional[]) => {
        this.especialistas = data;
      },
      error => {
        console.error('Erro ao buscar especialistas:', error);
      }
    );
  }

}
