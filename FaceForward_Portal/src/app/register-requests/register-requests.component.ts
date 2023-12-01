import { Component, OnInit } from '@angular/core';
import { UserService } from '../services/user.service';

@Component({
  selector: 'app-register-requests',
  templateUrl: './register-requests.component.html',
  styleUrls: ['./register-requests.component.css']
})
export class RegisterRequestsComponent implements OnInit{
  constructor(private userService:UserService){}

  users : any = []

  async ngOnInit() {
    const res = await this.userService.getUnverifiedUser().toPromise()
    this.users = res.users
    console.log(this.users)
  }
}
