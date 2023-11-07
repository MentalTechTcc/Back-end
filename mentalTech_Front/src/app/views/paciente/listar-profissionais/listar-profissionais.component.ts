import { Component, OnInit } from '@angular/core';
import { Profissional } from 'src/app/models/Profissional.models';
import { CadastroProfissionalService } from 'src/app/services/cadastro-profissional.service';
import { CadastroAgendaProfissionalService } from 'src/app/services/cadastro-agenda-profissional.service';
import { EspecialidadeServiceService } from 'src/app/services/especialidade-service.service';
import { TematicaServiceService } from 'src/app/services/tematica-service.service';
import { Agenda, AgendaRequestId } from 'src/app/models/Agenda.models';
import { Especialidade } from 'src/app/models/Especialidade.models';
import { Tematica } from 'src/app/models/Tematica.models';

@Component({
  selector: 'app-listar-profissionais',
  templateUrl: './listar-profissionais.component.html',
  styleUrls: ['./listar-profissionais.component.css']
})
export class ListarProfissionaisComponent implements OnInit {

  especialistas: Profissional[] = [];
  agendaDoProfissional: AgendaRequestId[]=[];
  especialidadesPorProfissional: { [cpfProfissional: string]: string[] } = {}; //objeto
  tematicasPorProfissional: { [cpfProfissional: string]: string[] } = {};  //objeto
  isModalOpen = false;

  constructor(
    private service: CadastroProfissionalService,
    private agendaService: CadastroAgendaProfissionalService,
    private especialidadeService: EspecialidadeServiceService,
    private tematicasService: TematicaServiceService
  ) {}

  ngOnInit(): void {
    this.service.listar().subscribe(
      (data: Profissional[]) => {
        this.especialistas = data;
        this.obterEspecialidadesPorProfissional();
        this.obterTematicasPorProfissional();
      },
      (error) => {
        console.error('Erro ao buscar especialistas:', error);
      }
    );
  }

  exibirAgenda(cpfProfissional: string): void {
    this.agendaService.listarPorCpf(cpfProfissional).subscribe(
      (data: AgendaRequestId[]) => {
        this.agendaDoProfissional = data.filter(agenda => !agenda.ocupado);
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

  obterEspecialidadesPorProfissional(): void {
    this.especialistas.forEach((especialista) => {
      this.especialidadeService.listarEspecialidadesProfissional(especialista.cpf).subscribe(
        (especialidades: Especialidade[]) => {
          this.especialidadesPorProfissional[especialista.cpf] = especialidades.map(especialidade => especialidade.descricaoEspecialidade);
        },
        (error) => {
          console.error('Erro ao buscar especialidades do profissional:', error);
        }
      );
    });
  }
  
  obterTematicasPorProfissional(): void {
    this.especialistas.forEach((especialista) => {
      this.tematicasService.listarTematicasProfissional(especialista.cpf).subscribe(
        (tematicas: Tematica[]) => {
          this.tematicasPorProfissional[especialista.cpf] = tematicas.map(tematica => tematica.nomeTematica);
        },
        (error) => {
          console.error('Erro ao buscar tematicas do profissional:', error);
        }
      );
    });
  }

}
