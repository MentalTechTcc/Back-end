import { TestBed } from '@angular/core/testing';

import { EspecialidadeServiceService } from './especialidade-service.service';

describe('EspecialidadeServiceService', () => {
  let service: EspecialidadeServiceService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(EspecialidadeServiceService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
