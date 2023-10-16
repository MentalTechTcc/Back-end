import { TestBed } from '@angular/core/testing';

import { CadastroPacienteService } from './cadastro-paciente.service';

describe('CadastroPacienteService', () => {
  let service: CadastroPacienteService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(CadastroPacienteService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
