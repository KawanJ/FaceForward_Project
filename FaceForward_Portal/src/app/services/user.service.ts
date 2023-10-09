import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'; //library (class) for using http apis 



@Injectable({
  providedIn: 'root'
})
export class UserService {

  private registerAPI = "http://127.0.0.1:5000/add_user"
              //importing HttpClient as http (instance of a class)
  constructor(private http:HttpClient) { }
                  //any data type
  registerUser(user:any){
    //ye http mein post karo koi bhi datatype (what url to connect to, giving requested data to API)
    return this.http.post<any>(this.registerAPI, user);
  }

}
