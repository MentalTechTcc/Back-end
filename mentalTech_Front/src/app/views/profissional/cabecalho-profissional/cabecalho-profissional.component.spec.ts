import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CabecalhoProfissionalComponent } from './cabecalho-profissional.component';

describe('CabecalhoProfissionalComponent', () => {
  let component: CabecalhoProfissionalComponent;
  let fixture: ComponentFixture<CabecalhoProfissionalComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CabecalhoProfissionalComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CabecalhoProfissionalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
