import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { provideHttpClient, withInterceptorsFromDi } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatButtonModule } from '@angular/material/button';
import { MatCardModule } from '@angular/material/card';
import { AppComponent } from './app.component';
import { HeaderComponent } from './components/header/header.component';
import { FooterComponent } from './components/footer/footer.component';
import { OrganizationsComponent } from './components/organizations/organizations.component';
import { ProductComponent } from './components/products/products.component';
import { ProfileComponent } from './components/profile/profile.component';
import { PublicationsComponent } from './components/publications/publications.component';
import { JwtModule } from '@auth0/angular-jwt';
import { LoginComponent } from './components/login/login.component';
import { provideAnimationsAsync } from '@angular/platform-browser/animations/async';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { ReactiveFormsModule } from '@angular/forms';
import { NotFoundComponent } from './components/not-found/not-found.component';
import { SinglePublicationComponent } from './components/single-publication/single-publication.component';
import { CommentsComponent } from './components/comments/comments.component';

import { SingleOrganizationComponent } from './components/single-organization/single-organization.component';

export function tokenGetter() {
  return localStorage.getItem('access_token');
}

@NgModule({ declarations: [
        AppComponent,
        HeaderComponent,
        FooterComponent,
        OrganizationsComponent,
        ProductComponent,
        ProfileComponent,
        PublicationsComponent,
        LoginComponent,
        NotFoundComponent,
        SinglePublicationComponent,
        CommentsComponent,
        SingleOrganizationComponent,
    ],
    bootstrap: [AppComponent], imports: [JwtModule.forRoot({
            config: {
                tokenGetter: tokenGetter,
                allowedDomains: ['localhost:8000'],
                disallowedRoutes: ['http://localhost:8000/api/token/'],
            },
        }),
        BrowserModule,
        ReactiveFormsModule,
        AppRoutingModule,
        MatToolbarModule,
        MatButtonModule,
        MatCardModule,
        MatFormFieldModule,
        MatInputModule], providers: [
        provideAnimationsAsync(),
        provideHttpClient(withInterceptorsFromDi())
    ] })
export class AppModule { }
