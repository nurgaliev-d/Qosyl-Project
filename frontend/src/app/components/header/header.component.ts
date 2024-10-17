import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { ApiService } from '../services/services/api.service';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent {
  constructor(private apiService: ApiService, private router: Router) {}

  logout(): void {
    localStorage.removeItem('access_token');
    this.router.navigate(['/login']);
  }

  navigateToSomePage(): void {
    this.router.navigate(['/publications']);
  }
}
