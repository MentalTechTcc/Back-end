import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CabecalhoPacienteComponent } from './cabecalho-paciente.component';

describe('CabecalhoPacienteComponent', () => {
  let component: CabecalhoPacienteComponent;
  let fixture: ComponentFixture<CabecalhoPacienteComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CabecalhoPacienteComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CabecalhoPacienteComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
