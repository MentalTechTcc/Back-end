import { TestBed } from '@angular/core/testing';

import { CadastroProfissionalService } from './cadastro-profissional.service';

describe('CadastroProfissionalService', () => {
  let service: CadastroProfissionalService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(CadastroProfissionalService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
