import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MinhasConsultasPacienteComponent } from './minhas-consultas-paciente.component';

describe('MinhasConsultasPacienteComponent', () => {
  let component: MinhasConsultasPacienteComponent;
  let fixture: ComponentFixture<MinhasConsultasPacienteComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ MinhasConsultasPacienteComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(MinhasConsultasPacienteComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
