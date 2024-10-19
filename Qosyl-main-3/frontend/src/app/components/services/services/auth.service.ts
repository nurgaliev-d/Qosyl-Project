import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';
import { Observable } from 'rxjs';

@Injectable({
    providedIn: 'root',
})
export class AuthService {
    private baseUrl = 'http://localhost:8000/api';

    constructor(private http: HttpClient, private router: Router) {}

    login(username: string, password: string): Observable<any> {
        return this.http.post<any>(`${this.baseUrl}/login/`, { username, password });
    }

    logout() {
        localStorage.removeItem('access_token');
        this.router.navigate(['/login']); // Redirect to login page
    }

    isAuthenticated() {
        return !!localStorage.getItem('access_token');
    }
}
