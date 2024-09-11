import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { UserloginComponent } from './userlogin/userlogin.component';
import { UserhomeComponent } from './userhome/userhome.component';
import { WorkerloginComponent } from './workerlogin/workerlogin.component';
import { WorkerhomeComponent } from './workerhome/workerhome.component';
import { UsercreateComponent } from './usercreate/usercreate.component';
import { WorkercreateComponent } from './workercreate/workercreate.component';
import { NavbarComponent } from './navbar/navbar.component';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    UserloginComponent,
    UserhomeComponent,
    WorkerloginComponent,
    WorkerhomeComponent,
    UsercreateComponent,
    WorkercreateComponent,
    NavbarComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
