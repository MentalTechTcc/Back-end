import { TestBed } from '@angular/core/testing';

import { AtualizacaoDadosProfisionalService } from './atualizacao-dados-profisional.service';

describe('AtualizacaoDadosProfisionalService', () => {
  let service: AtualizacaoDadosProfisionalService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(AtualizacaoDadosProfisionalService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
