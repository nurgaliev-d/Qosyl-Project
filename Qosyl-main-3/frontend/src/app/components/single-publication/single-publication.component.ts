import {Component, OnInit} from '@angular/core';
import {ApiService} from "../services/services/api.service";
import {Publication} from "../../publication";
import {Comment} from "../../comment";
import {ActivatedRoute} from "@angular/router";
import {observable} from "rxjs";


@Component({
  selector: 'app-single-publication',
  templateUrl: './single-publication.component.html',
  styleUrl: './single-publication.component.css'
})
export class SinglePublicationComponent implements OnInit {
  publication: any;
  comments: any[] = [];
  id: any;
  likePublication(arg0: any) {
    throw new Error('Method not implemented.');
  }

  constructor(private route: ActivatedRoute, private apiService: ApiService) {

  }


  ngOnInit(): void {
    this.loadPublication();
    this.loadComments()
  }

  loadComments(): void{
    this.route.paramMap.subscribe((params) => {
      const publication = Number(params.get('publication'));
      this.apiService.getComments(publication).subscribe(
        (data) => {
          this.comments = data;
          console.log(this.comments);
        },
        (error) => {
          console.error('Error fetching comments', error);
        }
      );
    })
  }
  // loadComments(): void {
  //   this.apiService.getComments().subscribe(
  //     (data) => {
  //       this.comments = data;
  //       console.log(this.comments);  // Check if data is being logged here
  //     },
  //     (error) => {
  //       console.error('Error fetching publications', error);
  //     }
  //   );
  // }


  loadPublication(): void {
    this.route.paramMap.subscribe((params) => {
      const id = Number(params.get('id'));
      this.apiService.getPublication(id).subscribe(
        (data) => {
          this.publication = data;
          console.log(this.publication);  // Check if data is being logged here
        },
        (error) => {
          console.error('Error fetching publications', error);
        }
      );
    })
  }
}
