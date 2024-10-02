import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { OrganizationsComponent } from './components/organizations/organizations.component';
import { ProductComponent } from './components/products/products.component';
import { ProfileComponent } from './components/profile/profile.component';

const routes: Routes = [
  { path: 'organizations', component: OrganizationsComponent },
  { path: 'products', component: ProductComponent },
  { path: '', redirectTo: '/organizations', pathMatch: 'full' },
  { path: '**', redirectTo: '/organizations' },
  { path: 'profile', component: ProfileComponent },
  { path: 'profile/:user_id', component: ProfileComponent }, 
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
