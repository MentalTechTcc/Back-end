import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RelatoriosPacienteComponent } from './relatorios-paciente.component';

describe('RelatoriosPacienteComponent', () => {
  let component: RelatoriosPacienteComponent;
  let fixture: ComponentFixture<RelatoriosPacienteComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ RelatoriosPacienteComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(RelatoriosPacienteComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
