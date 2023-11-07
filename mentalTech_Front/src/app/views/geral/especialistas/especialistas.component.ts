import { Component, OnInit } from '@angular/core';
import { CadastroProfissionalService } from 'src/app/services/cadastro-profissional.service';
import { Profissional } from 'src/app/models/Profissional.models';
import { Especialidade } from 'src/app/models/Especialidade.models';
import { Tematica } from 'src/app/models/Tematica.models';
import { EspecialidadeServiceService } from 'src/app/services/especialidade-service.service';
import { TematicaServiceService } from 'src/app/services/tematica-service.service';

@Component({
  selector: 'app-especialistas',
  templateUrl: './especialistas.component.html',
  styleUrls: ['./especialistas.component.css']
})
export class EspecialistasComponent implements OnInit {
  especialistas: Profissional[] = [];
  especialidadesPorProfissional: { [cpfProfissional: string]: string[] } = {}; //objeto
  tematicasPorProfissional: { [cpfProfissional: string]: string[] } = {};  //objeto

  constructor(
    private service: CadastroProfissionalService,
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
