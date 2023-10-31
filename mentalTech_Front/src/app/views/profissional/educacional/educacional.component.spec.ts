import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EducacionalComponent } from './educacional.component';

describe('EducacionalComponent', () => {
  let component: EducacionalComponent;
  let fixture: ComponentFixture<EducacionalComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ EducacionalComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(EducacionalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
