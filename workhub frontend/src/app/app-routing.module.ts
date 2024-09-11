import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { UserloginComponent } from './userlogin/userlogin.component';
import { UserhomeComponent } from './userhome/userhome.component';
import { WorkerloginComponent } from './workerlogin/workerlogin.component';
import { WorkerhomeComponent } from './workerhome/workerhome.component';
import { UsercreateComponent } from './usercreate/usercreate.component';
import { WorkercreateComponent } from './workercreate/workercreate.component';

const routes: Routes = [
  {path:'',component:HomeComponent},
  {path:'ulogin',component:UserloginComponent},
  {path:'uhome',component:UserhomeComponent},
  {path:'wlogin',component:WorkerloginComponent},
  {path:'whome',component:WorkerhomeComponent},
  {path:'usignup',component:UsercreateComponent},
  {path:'wsignup',component:WorkercreateComponent}

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
