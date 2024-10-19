import { Component, OnInit } from '@angular/core';
import { ApiService } from '../services/services/api.service';

@Component({
  selector: 'app-organizations',
  templateUrl: './organizations.component.html',
  styleUrls: ['./organizations.component.css'],
})
export class OrganizationsComponent implements OnInit {
  organizations: any[] = [];

  constructor(private apiService: ApiService) {}

  ngOnInit(): void {
    this.loadOrganizations();
  }

  loadOrganizations(): void {
    this.apiService.getOrganizations().subscribe(
      (data) => {
        this.organizations = data; // Set the fetched data to the organizations property
      },
      (error) => {
        console.error('Error fetching organizations:', error); // Log any errors
      }
    );
  }
}
