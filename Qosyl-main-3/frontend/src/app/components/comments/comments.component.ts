import { Component,OnInit } from '@angular/core';
import {ActivatedRoute} from "@angular/router";
import {ApiService} from "../services/services/api.service";

@Component({
  selector: 'app-comments',
  templateUrl: './comments.component.html',
  styleUrl: './comments.component.css'
})
export class CommentsComponent implements OnInit{
  comments:any[] = []

  constructor(private route: ActivatedRoute, private apiService: ApiService) {

  }
  ngOnInit(): void {
    this.loadComments()
  }
  loadComments(): void{
    this.route.paramMap.subscribe((params) => {
      const publication = Number(params.get('id'));
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
}
