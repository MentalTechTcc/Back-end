import { TestBed } from '@angular/core/testing';

import { AvaliacaoPacienteService } from './avaliacao-paciente.service';

describe('AvaliacaoPacienteService', () => {
  let service: AvaliacaoPacienteService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(AvaliacaoPacienteService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
