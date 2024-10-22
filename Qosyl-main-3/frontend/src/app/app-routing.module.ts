import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { OrganizationsComponent } from './components/organizations/organizations.component';
import { ProductComponent } from './components/products/products.component';
import { ProfileComponent } from './components/profile/profile.component';
import { PublicationsComponent } from './components/publications/publications.component';
import { LoginComponent } from './components/login/login.component';
import { NotFoundComponent } from './components/not-found/not-found.component';
import {SinglePublicationComponent} from "./components/single-publication/single-publication.component";
import {CommentsComponent} from "./components/comments/comments.component";
import {SingleOrganizationComponent} from "./components/single-organization/single-organization.component";

const routes: Routes = [
  { path: 'login', component: LoginComponent },
  { path: 'organizations', component: OrganizationsComponent },
  { path: 'products', component: ProductComponent },
  { path: 'profile', component: ProfileComponent },
  { path: 'profile/:user_id', component: ProfileComponent },
  { path: 'publications', component: PublicationsComponent },
  { path: 'publications/:id', component: SinglePublicationComponent},
  { path: 'organizations/:id', component: SingleOrganizationComponent},
  { path: 'comments/:publication',component: CommentsComponent},
  { path: '', redirectTo: '/publications', pathMatch: 'full' },
  { path: '**', component: NotFoundComponent }
];


@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
