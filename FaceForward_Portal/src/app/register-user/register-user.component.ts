import { Component } from '@angular/core';
import { UserService } from '../services/user.service';
import { ToastrService } from 'ngx-toastr';
import { HttpErrorResponse } from '@angular/common/http';

@Component({
  selector: 'app-register-user',
  templateUrl: './register-user.component.html',
  styleUrls: ['./register-user.component.css']
})
export class RegisterUserComponent {

  constructor(private toastr: ToastrService, private userService:UserService){  }

  user = {
    Passport_No: null,
    Type: null,
    Country_Code: null,
    Given_Name: null,
    Surname: null,
    Sex: null,
    Nationality: null,
    Date_of_Birth: null,
    Place_of_Birth: null,
    Date_of_Issue: null,
    Date_of_Expiration: null,
    Issuing_Authority: null
  };

  image: File = {} as File

  onFileSelected(event: any): void {
    this.image = event.target.files[0];
  }

  async register()
  {
    try{
                      //to use await the function should be asyn (asynchronous)
      const response = await this.userService.registerUser(this.user, this.image).toPromise()
                                                                      //prmosises to get the data
                            //iss service se data bhejega backend mein api and result message aayega (successful/error)
      console.log(response)
      this.toastr.success('Registration Successful');
      
      this.user.Passport_No=null;
      this.user.Type=null;
      this.user.Country_Code=null;
      this.user.Given_Name=null;
      this.user.Surname=null;
      this.user.Sex=null;
      this.user.Nationality=null;
      this.user.Date_of_Birth=null;
      this.user.Place_of_Birth=null;
      this.user.Date_of_Issue=null;
      this.user.Date_of_Expiration=null;
      this.user.Issuing_Authority=null;
      //print the response (console.log is print in javascript)
    }
    catch (error){
      if(error instanceof HttpErrorResponse) {
        this.toastr.error('Please Try again', error.error.error);
      }
      console.log(error)
    }
  }
}
