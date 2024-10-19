import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SinglePublicationComponent } from './single-publication.component';

describe('SinglePublicationComponent', () => {
  let component: SinglePublicationComponent;
  let fixture: ComponentFixture<SinglePublicationComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [SinglePublicationComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SinglePublicationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
