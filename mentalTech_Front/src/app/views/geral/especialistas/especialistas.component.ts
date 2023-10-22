import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from 'src/environments/environment';
import { CadastroProfissionalService } from 'src/app/services/cadastro-profissional.service';
import { Profissional } from 'src/app/models/Profissional.models';

@Component({
  selector: 'app-especialistas',
  templateUrl: './especialistas.component.html',
  styleUrls: ['./especialistas.component.css']
})
export class EspecialistasComponent implements OnInit {
  especialistas: Profissional[] = [];

  constructor(private http: HttpClient, private service: CadastroProfissionalService) {}

  ngOnInit(): void {
    // Fazer uma solicitação HTTP para buscar os dados dos especialistas
    // this.http.get<any[]>(`${environment.baseUrl}/profissional`)
    // .subscribe((data: any[]) => {
    //   this.especialistas = data;
    // });

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
