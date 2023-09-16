//Extra Libraries Used
import { NgModule } from '@angular/core'; //Default Library
import { BrowserModule } from '@angular/platform-browser'; //Default Library
import { HttpClientModule } from '@angular/common/http'; //Library for calling API
import { FormsModule } from '@angular/forms'; //Library for using forms in HTML

//Components Below
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component'; //Default Component

@NgModule({
  declarations: [
    AppComponent
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
