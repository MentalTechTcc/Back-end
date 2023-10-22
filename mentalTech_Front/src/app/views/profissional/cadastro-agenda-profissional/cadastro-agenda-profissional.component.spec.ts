import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CadastroAgendaProfissionalComponent } from './cadastro-agenda-profissional.component';

describe('CadastroAgendaProfissionalComponent', () => {
  let component: CadastroAgendaProfissionalComponent;
  let fixture: ComponentFixture<CadastroAgendaProfissionalComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CadastroAgendaProfissionalComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CadastroAgendaProfissionalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
