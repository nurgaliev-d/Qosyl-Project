import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private baseUrl = 'http://localhost:8000/api';

  constructor(private http: HttpClient) {}

  getOrganizations(): Observable<any[]> {
    return this.http.get<any[]>(`${this.baseUrl}/organizations/`);
  }

  getProducts(): Observable<any[]> {
    return this.http.get<any[]>(`${this.baseUrl}/products/`);
  }

  getCurrentUserProfile(): Observable<any> {
    return this.http.get(`${this.baseUrl}profile/`);
  }
  getOtherUserProfile(userId: string): Observable<any> {
    return this.http.get(`${this.baseUrl}profile/${userId}/`);
  }
}
