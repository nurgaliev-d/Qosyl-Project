import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ApiService } from '../services/services/api.service';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit {
  userProfile: any = {};
  isCurrentUser: boolean = false;

  constructor(
    private apiService: ApiService,
    private route: ActivatedRoute
  ) {}

  ngOnInit(): void {
    const userId = this.route.snapshot.paramMap.get('user_id');
    if (userId) {
      this.isCurrentUser = false;
      this.loadOtherUserProfile(userId);
    } else {
      this.isCurrentUser = true;
      this.loadCurrentUserProfile();
    }
  }

  loadCurrentUserProfile(): void {
    this.apiService.getCurrentUserProfile().subscribe(
      data => {
        this.userProfile = data;
      },
      error => {
        console.error('Error fetching profile:', error);
      }
    );
  }

  loadOtherUserProfile(userId: string): void {
    this.apiService.getOtherUserProfile(userId).subscribe(
      data => {
        this.userProfile = data;
      },
      error => {
        console.error('Error fetching other user profile:', error);
      }
    );
  }
}
