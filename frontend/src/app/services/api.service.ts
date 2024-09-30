import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private baseUrl = 'http://127.0.0.1:8000'; // URL of your Django API

  constructor(private http: HttpClient) { }

  getOrganizations(): Observable<any> {
    return this.http.get(`${this.baseUrl}/organizations/`);  // Base URL points to Django API
  }
  

  // Fetch publications
  getPublications(): Observable<any> {
    return this.http.get(`${this.baseUrl}/publications/`);
  }

  // Fetch products
  getProducts(): Observable<any> {
    return this.http.get(`${this.baseUrl}/products/`);
  }

  // Fetch user profile data
  getUserProfile(userId: number): Observable<any> {
    return this.http.get(`${this.baseUrl}/userprofile/${userId}/`);
  }
}
