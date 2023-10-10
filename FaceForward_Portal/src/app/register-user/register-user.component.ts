import { Component } from '@angular/core';
import { UserService } from '../services/user.service';

@Component({
  selector: 'app-register-user',
  templateUrl: './register-user.component.html',
  styleUrls: ['./register-user.component.css']
})
export class RegisterUserComponent {

  constructor(private userService:UserService){  }

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

  async register()
  {
    try{
                      //to use await the function should be asyn (asynchronous)
      const response = await this.userService.registerUser(this.user).toPromise()
                                                                      //prmosises to get the data
                            //iss service se data bhejega backend mein api and result message aayega (successful/error)
      console.log(response) //print the response (console.log is print in javascript)
    }
    catch (error){
      console.log(error)
    }
  }
}
