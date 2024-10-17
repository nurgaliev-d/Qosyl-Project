import { Component, OnInit } from '@angular/core';
import { ApiService } from '../services/services/api.service';

@Component({
  selector: 'app-publications',
  templateUrl: './publications.component.html',
  styleUrls: ['./publications.component.css']
})
export class PublicationsComponent implements OnInit {
  router: any;
likePublication(arg0: any) {
throw new Error('Method not implemented.');
}
  publications: any[] = [];

  constructor(private apiService: ApiService) {}

  ngOnInit(): void {
    this.loadPublications();
  }

  loadPublications(): void {
    this.apiService.getPublications().subscribe({
        next: (data: any[]) => {
            this.publications = data;
        },
        error: (error) => {
            if (error.status === 401) {
                this.apiService.logout();
                this.router.navigate(['/login']);
            } else {
                console.error('Error fetching publications:', error);
            }
        }
    });
}
}
