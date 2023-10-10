import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { RegisterUserComponent } from './register-user/register-user.component';
import { ImmigrationCheckinComponent } from './immigration-checkin/immigration-checkin.component';
import { ImmigrationRecordsComponent } from './immigration-records/immigration-records.component';

const routes: Routes = [
  {
    path: 'register_user',  //the path name like https://reg
    component: RegisterUserComponent,   //component(page) name 
    title: 'Register User'   //at the top of the tab
  },
  {
    path: 'immigration_checkin',
    component: ImmigrationCheckinComponent,
    title: 'Immigration Check-In'
  },
  {
    path: 'immigration_records',
    component: ImmigrationRecordsComponent,
    title: 'Immigration Records'
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
