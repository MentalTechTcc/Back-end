import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EducacionalModalComponent } from './educacional-modal.component';

describe('EducacionalModalComponent', () => {
  let component: EducacionalModalComponent;
  let fixture: ComponentFixture<EducacionalModalComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ EducacionalModalComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(EducacionalModalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
