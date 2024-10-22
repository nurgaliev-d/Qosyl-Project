import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SingleOrganizationComponent } from './single-organization.component';
import {CommentsComponent} from "../comments/comments.component";

describe('SingleOrganizationComponent', () => {
  let component: SingleOrganizationComponent;
  let fixture: ComponentFixture<SingleOrganizationComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [SingleOrganizationComponent, CommentsComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SingleOrganizationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });
  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
