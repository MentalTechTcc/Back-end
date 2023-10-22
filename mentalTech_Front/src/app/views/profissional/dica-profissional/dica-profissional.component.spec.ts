import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DicaProfissionalComponent } from './dica-profissional.component';

describe('DicaProfissionalComponent', () => {
  let component: DicaProfissionalComponent;
  let fixture: ComponentFixture<DicaProfissionalComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ DicaProfissionalComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(DicaProfissionalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
