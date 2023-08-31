import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class TempServiceService {
  private apiUrl = 'http://127.0.0.1:5000';

  constructor(private http: HttpClient) {}

  addData(inputString: string) {
    const requestData = {
      "passID": inputString
    };
  
    return this.http.post(this.apiUrl + '/add_user', requestData);
  }

  viewData() {
    return this.http.get(this.apiUrl + '/view_users');
  }
}
