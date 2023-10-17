import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SouProfissionalComponent } from './sou-profissional.component';

describe('SouProfissionalComponent', () => {
  let component: SouProfissionalComponent;
  let fixture: ComponentFixture<SouProfissionalComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SouProfissionalComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SouProfissionalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
