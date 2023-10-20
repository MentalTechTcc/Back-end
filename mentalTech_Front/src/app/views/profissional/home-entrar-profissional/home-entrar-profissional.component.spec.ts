import { ComponentFixture, TestBed } from '@angular/core/testing';

import { HomeEntrarProfissionalComponent } from './home-entrar-profissional.component';

describe('HomeEntrarProfissionalComponent', () => {
  let component: HomeEntrarProfissionalComponent;
  let fixture: ComponentFixture<HomeEntrarProfissionalComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ HomeEntrarProfissionalComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(HomeEntrarProfissionalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
