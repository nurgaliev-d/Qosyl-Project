import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { ApiService } from '../services/services/api.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  loginForm: FormGroup;
  errorMessage: string | null = null;
  isLoading: boolean = false;

  constructor(
    private fb: FormBuilder,
    private apiService: ApiService,
    private router: Router
  ) {
    this.loginForm = this.fb.group({
      username: ['', Validators.required],
      password: ['', Validators.required]
    });
  }

  ngOnInit(): void {
    if (this.apiService.isAuthenticated()) {
      this.router.navigate(['/users']);
    }
  }

  onSubmit(): void {
    if (this.loginForm.valid) {
      const { username, password } = this.loginForm.value;
      this.isLoading = true;

      this.apiService.login(username, password).subscribe({
        next: (response) => {
          console.log('Login successful:', response);
          this.apiService.setToken(response.access_token);
          this.router.navigate(['/publications']);
        },
        error: (err) => {
          console.error('Login failed:', err);
          this.errorMessage = 'Invalid username or password. Please try again.';
        },
        complete: () => {
          this.isLoading = false; // Reset loading state
        }
      });
    }
  }
}
