import { Component, OnInit } from '@angular/core';
import { Relatorio } from 'src/app/models/Relatorio.models';
import {LoginUsuarioService} from 'src/app/services/login-usuario.service'
import {RelatorioService} from 'src/app/services/relatorio.service'


@Component({
  selector: 'app-educacional',
  templateUrl: './educacional.component.html',
  styleUrls: ['./educacional.component.css']
})
export class EducacionalComponent implements OnInit {

  relatorios: Relatorio[] = [];
  profissional:any=[];

  constructor(
    private serviceRelatorio: RelatorioService,
    private serviceProfissional: LoginUsuarioService,
    ) { }

  ngOnInit(): void {
    this.serviceProfissional.getPerfilProfissional().subscribe(
      (data: any) => {
        this.profissional = data;
        console.log(data)
        this.serviceRelatorio.listarPorCpfProfissional(this.profissional.cpf).subscribe(
          (data: Relatorio[]) => {
            this.relatorios = data;
            console.log(data)
          },
          error => {
            console.error('Erro ao buscar dicas:', error);
          }
        );
      },
      (error) => {
        console.log('error');
      }
    );

    

  }

}
