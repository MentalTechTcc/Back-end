import { Component, OnInit } from '@angular/core';
import { Relatorio } from 'src/app/models/Relatorio.models';

@Component({
  selector: 'app-educacional',
  templateUrl: './educacional.component.html',
  styleUrls: ['./educacional.component.css']
})
export class EducacionalComponent implements OnInit {

  relatorios: Relatorio[] = [
    {descricao: 'testando123', idRelatorio: 123, idConsulta: 134, dataCadastro: new Date},
    {descricao: 'testando12345', idRelatorio: 124, idConsulta: 135, dataCadastro: new Date},
  ];

  constructor() { }

  ngOnInit(): void {
  }

}
