import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './component/login/login.component';
import { SecondComponent } from './component/second/second.component';
import { HomeComponent } from './component/home/home.component';
// import { AppComponent } from './app.component';
import { AdminComponent } from './component/admin/admin.component';
import { AuthGuard } from './services/auth.guard';
import { Role } from './shared/helpers';

const routes: Routes = [
  {
    path: 'second',
    component: SecondComponent,
    canActivate: [AuthGuard],
    data: {roles: [Role.Admin, Role.User]}
  },
  {
    path : 'login',
    component: LoginComponent
  },
  {
    path : '',
    component: HomeComponent
  },
  {
    path: 'admin',
    component: AdminComponent,
    canActivate: [AuthGuard],
    data: {roles: [Role.Admin]}
  },
  {
    path: '**',
    redirectTo: 'login' 
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})



export class AppRoutingModule { }
