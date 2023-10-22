import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DicasPacienteComponent } from './dicas-paciente.component';

describe('DicasPacienteComponent', () => {
  let component: DicasPacienteComponent;
  let fixture: ComponentFixture<DicasPacienteComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DicasPacienteComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DicasPacienteComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
