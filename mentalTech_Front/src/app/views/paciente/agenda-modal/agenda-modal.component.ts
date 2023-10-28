import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { Agenda } from 'src/app/models/Agenda.models';

@Component({
  selector: 'app-agenda-modal',
  templateUrl: './agenda-modal.component.html',
  styleUrls: ['./agenda-modal.component.css']
})
export class AgendaModalComponent implements OnInit {
  @Input() agendaDoProfissional: Agenda[]=[];
  @Output() fecharModalEvent = new EventEmitter<void>(); 

  constructor() { }

  ngOnInit(): void {
  }

  fecharModal() {
    this.fecharModalEvent.emit();
  }
  getModalidadeLabel(modalidade: number): string {
    return modalidade === 1 ? 'Online' : 'Presencial';
  }
}
