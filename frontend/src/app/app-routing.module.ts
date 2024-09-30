import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { OrganizationsComponent } from './organizations/organizations.component';
import { ProductsComponent } from './products/products.component';

const routes: Routes = [
  { path: 'organizations', component: OrganizationsComponent },
  { path: 'products', component: ProductsComponent },
  { path: '', redirectTo: '/organizations', pathMatch: 'full' } // Default route
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
