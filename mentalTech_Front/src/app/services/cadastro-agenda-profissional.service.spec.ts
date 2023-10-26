import { TestBed } from '@angular/core/testing';

import { CadastroAgendaProfissionalService } from './cadastro-agenda-profissional.service';

describe('CadastroAgendaProfissionalService', () => {
  let service: CadastroAgendaProfissionalService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(CadastroAgendaProfissionalService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
