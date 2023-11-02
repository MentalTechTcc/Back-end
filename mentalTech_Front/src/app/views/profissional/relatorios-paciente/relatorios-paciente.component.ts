import { Component, OnInit } from '@angular/core';
import { RelatorioService } from 'src/app/services/relatorio.service';
import { Relatorio } from 'src/app/models/Relatorio.models';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-relatorios-paciente',
  templateUrl: './relatorios-paciente.component.html',
  styleUrls: ['./relatorios-paciente.component.css']
})
export class RelatoriosPacienteComponent implements OnInit {

  relatorios: Relatorio[] = [];

  constructor(
    private serviceRelatorio: RelatorioService,
    private route: ActivatedRoute
  ) { }

  ngOnInit(): void {
    this.route.paramMap.subscribe(params => {
      const idPessoa = params.get('idPessoa');
      const cpfProfissional = params.get('cpfProfissional');
      
      if (idPessoa && cpfProfissional) {
        this.serviceRelatorio.listarPorIdPessoa(Number(idPessoa), cpfProfissional).subscribe(
          (data: Relatorio[]) => {
            this.relatorios = data;
            console.log(data);
          },
          error => {
            console.error('Erro ao buscar relatórios:', error);
          }
        );
      }
    });
  }
}
