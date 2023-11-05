import { TestBed } from '@angular/core/testing';

import { AvaliacaoProfissionalService } from './avaliacao-profissional.service';

describe('AvaliacaoProfissionalService', () => {
  let service: AvaliacaoProfissionalService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(AvaliacaoProfissionalService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
