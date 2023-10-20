import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from 'src/environments/environment';

@Component({
  selector: 'app-especialistas',
  templateUrl: './especialistas.component.html',
  styleUrls: ['./especialistas.component.css']
})
export class EspecialistasComponent implements OnInit {
    especialistas: any[] = [];
  
    constructor(private http: HttpClient) {}
  
    ngOnInit(): void {
      // Fazer uma solicitação HTTP para buscar os dados dos especialistas
      this.http.get<any[]>(`${environment.baseUrl}/profissional`)
        .subscribe((data: any[]) => {
          this.especialistas = data;
        });
    }
  }


