import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'; //library (class) for using http apis 



@Injectable({
  providedIn: 'root'
})
export class UserService {

  private registerUserAPI = "http://127.0.0.1:5000/add_user"
  private getUserAPI = "http://127.0.0.1:5000/travel_history?id="
  private getUnverifiedUserAPI = "http://127.0.0.1:5000/pending_requests"
  private verifyUserAPI = "http://127.0.0.1:5000/verify_user?id="
              
  constructor(private http:HttpClient) { } //importing HttpClient as http (instance of a class)

  registerUser(user:any, photo:File){
    const formData = new FormData();
    formData.append('data', JSON.stringify(user));
    formData.append('photo', photo);
    //ye http mein post karo koi bhi datatype (what url to connect to, giving requested data to API)
    return this.http.post<any>(this.registerUserAPI, formData);
  }

  getUser(id:string){
    return this.http.get<any>(this.getUserAPI + id);
  }

  getUnverifiedUser(){
    return this.http.get<any>(this.getUnverifiedUserAPI);
  }

  verifyUser(id:string){
    return this.http.get<any>(this.verifyUserAPI + id);
  }

}
