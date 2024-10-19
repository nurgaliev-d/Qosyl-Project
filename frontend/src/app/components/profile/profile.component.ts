import { Component, OnInit } from '@angular/core';
import { ApiService } from '../services/services/api.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit {
  userProfile: any;
  error: string | null = null;

  constructor(private apiService: ApiService, private router: Router) {}

  ngOnInit(): void {
    this.fetchUserProfile();
  }

  fetchUserProfile(): void {
    const token = this.apiService.getToken();
    console.log('Token:', token); // Log the token to see its value
    this.apiService.getUserProfile().subscribe({
        next: (data) => {
            this.userProfile = data;
        },
        error: (err) => {
            if (err.status === 401) {
                this.apiService.logout();
                this.router.navigate(['/login']);
            } else {
                this.error = 'Failed to load profile';
                console.error('Error fetching user profile:', err);
            }
        }
    });
  }
}
