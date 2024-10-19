import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private baseUrl = 'http://localhost:8000/api';

  constructor(private http: HttpClient) {}

  getUsers(): Observable<any[]> {
    const token = this.getToken();
    const headers = token ? new HttpHeaders().set('Authorization', `Bearer ${token}`) : new HttpHeaders();
  
    return this.http.get<any[]>(`${this.baseUrl}/users/`, { headers });
  }  

  getOrganizations(): Observable<any[]> {
    const token = this.getToken();
    const headers = token ? new HttpHeaders().set('Authorization', `Bearer ${token}`) : new HttpHeaders();
  
    return this.http.get<any[]>(`${this.baseUrl}/organizations/`, { headers });
  }  

  getProducts(): Observable<any[]> {
    return this.http.get<any[]>(`${this.baseUrl}/products/`);
  }

  getUserProfile(): Observable<any> {
    const token = this.getToken();
    const headers = token ? new HttpHeaders().set('Authorization', `Bearer ${token}`) : new HttpHeaders();

    return this.http.get<any>(`${this.baseUrl}/profile/`, { headers });
}


  getOtherUserProfile(userId: string): Observable<any> {
    return this.http.get(`${this.baseUrl}/profile/${userId}/`);
  }

  getPublications(): Observable<any[]> {
    const token = this.getToken();
    const headers = token ? new HttpHeaders().set('Authorization', `Bearer ${token}`) : new HttpHeaders();
  
    return this.http.get<any[]>(`${this.baseUrl}/publications/`, { headers });
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
  

  updateUserProfile(data: FormData): Observable<any> {
    return this.http.post<any>(`${this.baseUrl}/profile/`, data);
  }  
  
  logout(): void {
    localStorage.removeItem('access_token');
  }  

  setToken(token: string): void {
    localStorage.setItem('access_token', token);
  }
  
  getToken(): string | null {
    return localStorage.getItem('access_token');
} 
  
  isAuthenticated(): boolean {
    return !!this.getToken();
  }
  
}