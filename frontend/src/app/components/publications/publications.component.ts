import { Component, OnInit } from '@angular/core';
import { ApiService } from '../services/services/api.service';

@Component({
  selector: 'app-publications',
  templateUrl: './publications.component.html',
  styleUrls: ['./publications.component.css']
})
export class PublicationsComponent implements OnInit {
likePublication(arg0: any) {
throw new Error('Method not implemented.');
}
  publications: any[] = [];

  constructor(private apiService: ApiService) {}

  ngOnInit(): void {
    this.loadPublications();
  }

  loadPublications(): void {
    this.apiService.getPublications().subscribe(
      (data) => {
        this.publications = data;
        console.log(this.publications);  // Check if data is being logged here
      },
      (error) => {
        console.error('Error fetching publications', error);
      }
    );
  }
}
