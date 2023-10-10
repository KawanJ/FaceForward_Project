import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ImmigrationCheckinComponent } from './immigration-checkin.component';

describe('ImmigrationCheckinComponent', () => {
  let component: ImmigrationCheckinComponent;
  let fixture: ComponentFixture<ImmigrationCheckinComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ImmigrationCheckinComponent]
    });
    fixture = TestBed.createComponent(ImmigrationCheckinComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
