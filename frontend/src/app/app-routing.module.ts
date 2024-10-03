import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { OrganizationsComponent } from './components/organizations/organizations.component';
import { ProductComponent } from './components/products/products.component';
import { ProfileComponent } from './components/profile/profile.component';
import { PublicationsComponent } from './components/publications/publications.component';
import { LoginComponent } from './components/login/login.component';
import { NotFoundComponent } from './components/not-found/not-found.component';

const routes: Routes = [
  { path: 'login', component: LoginComponent },
  { path: 'organizations', component: OrganizationsComponent },
  { path: 'products', component: ProductComponent },
  { path: 'profile', component: ProfileComponent },
  { path: 'profile/:user_id', component: ProfileComponent }, 
  { path: 'publications', component: PublicationsComponent },
  { path: '', redirectTo: '/publications', pathMatch: 'full' },
  { path: '**', component: NotFoundComponent }
];


@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
