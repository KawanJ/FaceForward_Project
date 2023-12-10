import { Component, OnInit } from '@angular/core';
import { UserService } from '../services/user.service';
import { ToastrService } from 'ngx-toastr';
import { HttpErrorResponse } from '@angular/common/http';

@Component({
  selector: 'app-register-requests',
  templateUrl: './register-requests.component.html',
  styleUrls: ['./register-requests.component.css']
})
export class RegisterRequestsComponent implements OnInit{

  constructor(private toastr: ToastrService, private userService:UserService){}

  users: any = []
  requestEmpty: boolean = false

  async ngOnInit() {
    const res = await this.userService.getUnverifiedUser().toPromise()
    this.users = res.users
    if(this.users.length == 0) {
      this.requestEmpty = true
    }
    console.log(this.users)
  }

  async acceptRequest(index:number) {
    try {
      const res = await this.userService.acceptRegisterRequest(this.users[index].Passport_No.toString()).toPromise();
      console.log(res)
      this.users.splice(index, 1)
      this.toastr.success('Request Accepted Successfully');
      if(this.users.length == 0) {
        this.requestEmpty = true
      }
    }
    catch (error) {
      if(error instanceof HttpErrorResponse) {
        this.toastr.error('Please Try again', error.error.error);
      }
      console.log(error)
    }
  }

  async rejectRequest(index: number) {
    try {
      const res = await this.userService.rejecttRegisterRequest(this.users[index].Passport_No).toPromise();
      console.log(res)
      this.users.splice(index, 1)
      this.toastr.success('Request Rejected Successfully');
      if(this.users.length == 0) {
        this.requestEmpty = true
      }
    }
    catch (error) {
      if(error instanceof HttpErrorResponse) {
        this.toastr.error('Please Try again', error.error.error);
      }
      console.log(error)
    }
  }
}