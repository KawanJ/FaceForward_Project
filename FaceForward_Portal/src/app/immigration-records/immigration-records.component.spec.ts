import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ImmigrationRecordsComponent } from './immigration-records.component';

describe('ImmigrationRecordsComponent', () => {
  let component: ImmigrationRecordsComponent;
  let fixture: ComponentFixture<ImmigrationRecordsComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ImmigrationRecordsComponent]
    });
    fixture = TestBed.createComponent(ImmigrationRecordsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
