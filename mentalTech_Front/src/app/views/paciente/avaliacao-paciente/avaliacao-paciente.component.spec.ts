import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AvaliacaoPacienteComponent } from './avaliacao-paciente.component';

describe('AvaliacaoPacienteComponent', () => {
  let component: AvaliacaoPacienteComponent;
  let fixture: ComponentFixture<AvaliacaoPacienteComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AvaliacaoPacienteComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AvaliacaoPacienteComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
