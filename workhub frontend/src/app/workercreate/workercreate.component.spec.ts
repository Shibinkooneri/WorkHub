import { ComponentFixture, TestBed } from '@angular/core/testing';

import { WorkercreateComponent } from './workercreate.component';

describe('WorkercreateComponent', () => {
  let component: WorkercreateComponent;
  let fixture: ComponentFixture<WorkercreateComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ WorkercreateComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(WorkercreateComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
