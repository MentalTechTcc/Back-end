import { Component, OnInit } from '@angular/core';
import { Profissional } from 'src/app/models/Profissional.models';
import { CadastroProfissionalService } from 'src/app/services/cadastro-profissional.service';
import { CadastroAgendaProfissionalService } from 'src/app/services/cadastro-agenda-profissional.service';
import { Agenda } from 'src/app/models/Agenda.models';

@Component({
  selector: 'app-listar-profissionais',
  templateUrl: './listar-profissionais.component.html',
  styleUrls: ['./listar-profissionais.component.css']
})
export class ListarProfissionaisComponent implements OnInit {

  especialistas: Profissional[] = [];
  agendaDoProfissional: Agenda[]=[];
  isModalOpen = false;

  constructor(
    private service: CadastroProfissionalService,
    private agendaService: CadastroAgendaProfissionalService
  ) {}

  ngOnInit(): void {
    this.service.listar().subscribe(
      (data: Profissional[]) => {
        this.especialistas = data;
      },
      (error) => {
        console.error('Erro ao buscar especialistas:', error);
      }
    );
  }

  exibirAgenda(cpfProfissional: string): void {
    this.agendaService.listarPorCpf(cpfProfissional).subscribe(
      (data: Agenda[]) => {
        this.agendaDoProfissional = data;
        this.isModalOpen = true;
        console.log(this.isModalOpen);
      },
      (error) => {
        console.error('Erro ao buscar a agenda do profissional:', error);
      }
    );
  }

  fecharModal() {
    this.isModalOpen = false;
  }
}
