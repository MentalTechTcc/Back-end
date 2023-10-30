import { Router } from '@angular/router';
import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { CadastroAgendaProfissionalService } from 'src/app/services/cadastro-agenda-profissional.service';


@Component({
  selector: 'app-pagamento',
  templateUrl: './pagamento.component.html',
  styleUrls: ['./pagamento.component.css']
})
export class PagamentoComponent implements OnInit {


  linkPagamento: string = '';
  pix: string = '';
  constructor(private router: Router, private agendaService: CadastroAgendaProfissionalService) { }

  ngOnInit(): void {
    this.linkPagamento = this.agendaService.getLinkPagamento();
    this.pix = this.agendaService.getPix();
  }

  fechar() {
    this.router.navigate(['/listar-profissionais']);

  }
}
