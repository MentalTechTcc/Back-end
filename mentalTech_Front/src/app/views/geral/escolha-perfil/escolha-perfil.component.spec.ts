import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EscolhaPerfilComponent } from './escolha-perfil.component';

describe('EscolhaPerfilComponent', () => {
  let component: EscolhaPerfilComponent;
  let fixture: ComponentFixture<EscolhaPerfilComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ EscolhaPerfilComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(EscolhaPerfilComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
