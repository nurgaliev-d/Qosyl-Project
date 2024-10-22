import { Component, OnInit } from '@angular/core';
import { ApiService } from '../services/services/api.service';
import {RouterLink} from "@angular/router";


@Component({
  selector: 'app-publications',
  templateUrl: './publications.component.html',
  styleUrls: ['./publications.component.css']
})
export class PublicationsComponent implements OnInit {

  publications: any[] = [];
  id: any;
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


  likPublication(id: number) {
    this.apiService.likePublication(id)
  }
}
