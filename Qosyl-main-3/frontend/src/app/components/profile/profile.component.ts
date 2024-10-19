import { Component, OnInit } from '@angular/core';
import { ApiService } from '../services/services/api.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit {
  userProfile: any = {};
  isCurrentUser: boolean = true;

  constructor(
    private apiService: ApiService,
    private router: Router // Import router for redirection
  ) {}

  ngOnInit(): void {
    this.loadCurrentUserProfile();
  }

  loadCurrentUserProfile(): void {
    this.apiService.getCurrentUserProfile().subscribe(
      data => {
        console.log(data);
        this.userProfile = data;
      },
      error => {
        console.error('Error fetching profile:', error);
      }
    );
}

  editProfile(): void {
    console.log('Edit profile clicked');
  }

  logout(): void {
    // Clear token or any authentication info
    localStorage.removeItem('token'); // If token is stored in localStorage

    // Redirect to login page
    this.router.navigate(['/login']);
  }
}
