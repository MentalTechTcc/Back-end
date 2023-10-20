import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CadastroEspEndTemComponent } from './cadastro-esp-end-tem.component';

describe('CadastroEspEndTemComponent', () => {
  let component: CadastroEspEndTemComponent;
  let fixture: ComponentFixture<CadastroEspEndTemComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CadastroEspEndTemComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CadastroEspEndTemComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
