//Extra Libraries Used
import { NgModule } from '@angular/core'; //Default Library
import { BrowserModule } from '@angular/platform-browser'; //Default Library
import { HttpClientModule } from '@angular/common/http'; //Library for calling API
import { FormsModule } from '@angular/forms'; //Library for using forms in HTML
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { ToastrModule } from 'ngx-toastr';

//Components Below
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { RegisterUserComponent } from './register-user/register-user.component';
import { ImmigrationCheckinComponent } from './immigration-checkin/immigration-checkin.component';
import { ImmigrationRecordsComponent } from './immigration-records/immigration-records.component';
import { RegisterRequestsComponent } from './register-requests/register-requests.component'; //Default Component


@NgModule({
  declarations: [
    AppComponent,
    RegisterUserComponent,
    ImmigrationCheckinComponent,
    ImmigrationRecordsComponent,
    RegisterRequestsComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    BrowserAnimationsModule,
    ToastrModule.forRoot(),
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
