import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-entrar',
  templateUrl: './entrar.component.html',
  styleUrls: ['./entrar.component.css']
})
export class EntrarComponent{

  selectedOption: string = 'paciente'; // Inicializa com 'paciente'

  selectOption(option: string): void {
    this.selectedOption = option;
  }

}
