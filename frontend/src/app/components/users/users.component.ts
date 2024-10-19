import { Component, OnInit } from '@angular/core';
import { ApiService } from '../services/services/api.service';

@Component({
  selector: 'app-users',
  templateUrl: './users.component.html',
  styleUrls: ['./users.component.css']
})
export class UsersComponent implements OnInit {
  users: any[] = [];
  organizations: any[] = [];
  selectedView: 'users' | 'organizations' = 'users'; // Default view
  router: any;

  constructor(private apiService: ApiService) {}

  ngOnInit(): void {
    this.fetchUsers();
    this.fetchOrganizations();
  }

  fetchUsers(): void {
    this.apiService.getUsers().subscribe({
      next: (data: any[]) => {
        this.users = data;
      },
      error: (error) => {
        if (error.status === 401) {
          this.apiService.logout();
          this.router.navigate(['/login']);
        }
        console.error('Error fetching users:', error);
      }
    });
  }  

  fetchOrganizations(): void {
    this.apiService.getOrganizations().subscribe({
      next: (data: any[]) => {
        this.organizations = data;
      },
      error: (error) => {
        console.error('Error fetching organizations:', error);
      }
    });
  }  

  toggleView(view: 'users' | 'organizations'): void {
    this.selectedView = view;
  }
}
