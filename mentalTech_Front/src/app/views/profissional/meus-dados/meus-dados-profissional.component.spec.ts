import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MeusDadosProfissionalComponent } from './meus-dados.component-profissional';

describe('MeusDadosProfissionalComponent', () => {
  let component: MeusDadosProfissionalComponent;
  let fixture: ComponentFixture<MeusDadosProfissionalComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ MeusDadosProfissionalComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(MeusDadosProfissionalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
