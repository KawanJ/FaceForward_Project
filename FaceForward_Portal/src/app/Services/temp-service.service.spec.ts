import { TestBed } from '@angular/core/testing';

import { TempServiceService } from './temp-service.service';

describe('TempServiceService', () => {
  let service: TempServiceService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(TempServiceService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
