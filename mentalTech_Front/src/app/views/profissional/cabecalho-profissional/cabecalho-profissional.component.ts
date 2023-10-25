import { Router } from '@angular/router';
import { Component, OnInit } from '@angular/core';
import { LoginUsuarioService } from 'src/app/services/login-usuario.service';

@Component({
  selector: 'app-cabecalho-profissional',
  templateUrl: './cabecalho-profissional.component.html',
  styleUrls: ['./cabecalho-profissional.component.css']
})
export class CabecalhoProfissionalComponent implements OnInit {

  constructor(private router: Router, private service: LoginUsuarioService) { }

  ngOnInit(): void {
  }
  sair(){
    this.service.logoutProfissional().subscribe(
      (response) => {

        this.router.navigate(['/home']);
        console.log('certooooooooooo')
      },
      (error) => {
        console.error(error);
      }
    );

  }

}
