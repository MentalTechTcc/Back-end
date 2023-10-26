import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MinhaAgendaProfissionalComponent } from './minha-agenda-profissional.component';

describe('MinhaAgendaProfissionalComponent', () => {
  let component: MinhaAgendaProfissionalComponent;
  let fixture: ComponentFixture<MinhaAgendaProfissionalComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ MinhaAgendaProfissionalComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(MinhaAgendaProfissionalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
