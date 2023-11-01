import { Component, OnInit, EventEmitter, Output, Input } from '@angular/core';
import { Relatorio } from 'src/app/models/Relatorio.models';

@Component({
  selector: 'app-educacional-modal',
  templateUrl: './educacional-modal.component.html',
  styleUrls: ['./educacional-modal.component.css']
})
export class EducacionalModalComponent implements OnInit {
  @Output() fecharModalEvent = new EventEmitter<void>();
  @Input() relatorio: Relatorio | null = null;


  constructor() {}

  ngOnInit(): void {}

  fecharModal() {
    this.fecharModalEvent.emit();
  }
}
