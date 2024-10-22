import {Component, OnInit} from '@angular/core';
import {ApiService} from "../services/services/api.service";
import {ActivatedRoute} from "@angular/router";

@Component({
  selector: 'app-single-organization',
  templateUrl: './single-organization.component.html',
  styleUrl: './single-organization.component.css'
})
export class SingleOrganizationComponent implements OnInit{

  organization: any;
  id: any;


  constructor(private route: ActivatedRoute, private apiService: ApiService) {

  }

  ngOnInit(): void {
    this.loadOrganization();
  }


  loadOrganization(): void {
    this.route.paramMap.subscribe((params) => {
      const id = Number(params.get('id'));
      this.apiService.getOrganization(id).subscribe(
        (data) => {
          this.organization = data;
          console.log(this.organization);
        },
        (error) => {
          console.error('Error fetching organization', error);
        }
      );
    })
  }
}
