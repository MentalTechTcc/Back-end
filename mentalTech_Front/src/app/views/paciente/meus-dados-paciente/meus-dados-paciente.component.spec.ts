import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MeusDadosPacienteComponent } from './meus-dados-paciente.component';

describe('MeusDadosPacienteComponent', () => {
  let component: MeusDadosPacienteComponent;
  let fixture: ComponentFixture<MeusDadosPacienteComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ MeusDadosPacienteComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(MeusDadosPacienteComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
