//Extra Libraries Used
import { NgModule } from '@angular/core'; //Default Library
import { BrowserModule } from '@angular/platform-browser'; //Default Library
import { HttpClientModule } from '@angular/common/http'; //Library for calling API
import { FormsModule } from '@angular/forms'; //Library for using forms in HTML

//Components Below
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { RegisterUserComponent } from './register-user/register-user.component';
import { ImmigrationCheckinComponent } from './immigration-checkin/immigration-checkin.component';
import { ImmigrationRecordsComponent } from './immigration-records/immigration-records.component'; //Default Component

@NgModule({
  declarations: [
    AppComponent,
    RegisterUserComponent,
    ImmigrationCheckinComponent,
    ImmigrationRecordsComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
