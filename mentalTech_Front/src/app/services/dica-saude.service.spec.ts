import { TestBed } from '@angular/core/testing';

import { DicaSaudeService } from './dica-saude.service';

describe('DicaSaudeService', () => {
  let service: DicaSaudeService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(DicaSaudeService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
