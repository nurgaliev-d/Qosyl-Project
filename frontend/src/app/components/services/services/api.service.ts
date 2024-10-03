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
    return this.http.get(`${this.baseUrl}/profile/`);
}

  getOtherUserProfile(userId: string): Observable<any> {
    return this.http.get(`${this.baseUrl}/profile/${userId}/`);
  }

  getPublications(): Observable<any[]> {
    return this.http.get<any[]>(`${this.baseUrl}/publications/`);
  }  

  getPublication(id: number): Observable<any> {
    return this.http.get<any>(`${this.baseUrl}/publications/${id}/`);
  }

  createPublication(publication: any): Observable<any> {
    return this.http.post<any>(`${this.baseUrl}/publications/create/`, publication);
  }

  updatePublication(id: number, publication: any): Observable<any> {
    return this.http.put<any>(`${this.baseUrl}/publications/${id}/update/`, publication);
  }

  deletePublication(id: number): Observable<any> {
    return this.http.delete<any>(`${this.baseUrl}/publications/${id}/delete/`);
  }

  likePublication(id: number): Observable<any> {
    return this.http.post<any>(`${this.baseUrl}/publications/${id}/like/`, {});
  }

  login(username: string, password: string): Observable<any> {
    return this.http.post<any>(`${this.baseUrl}/token/`, { username, password });
  }
  
  setToken(token: string): void {
    localStorage.setItem('access_token', token);
  }
  
  getToken(): string | null {
    return localStorage.getItem('access_token');
  }
  
  logout(): void {
    localStorage.removeItem('access_token');
  }  
}