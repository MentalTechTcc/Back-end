import { TestBed } from '@angular/core/testing';

import { TematicaServiceService } from './tematica-service.service';

describe('TematicaServiceService', () => {
  let service: TematicaServiceService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(TematicaServiceService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
