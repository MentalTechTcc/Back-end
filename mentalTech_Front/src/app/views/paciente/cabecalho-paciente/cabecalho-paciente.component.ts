import { Router } from '@angular/router';
import { LoginUsuarioService } from './../../../services/login-usuario.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-cabecalho-paciente',
  templateUrl: './cabecalho-paciente.component.html',
  styleUrls: ['./cabecalho-paciente.component.css']
})
export class CabecalhoPacienteComponent implements OnInit {

  constructor(private router: Router,private service: LoginUsuarioService) { }

  ngOnInit(): void {
  }

  sair(){
    this.service.logoutPaciente().subscribe(
      (response) => {

        this.router.navigate(['/home']);
      },
      (error) => {
        console.error(error);
      }
    );

  }

}
