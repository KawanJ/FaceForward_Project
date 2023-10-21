import { Component } from '@angular/core';
import { UserService } from '../services/user.service';

@Component({
  selector: 'app-immigration-checkin',
  templateUrl: './immigration-checkin.component.html',
  styleUrls: ['./immigration-checkin.component.css']
})
export class ImmigrationCheckinComponent {

  constructor(private userService:UserService) {}

  id = ""
  verified = null

  async verifyUser()
  {
    try{
      const res = await this.userService.verifyUser(this.id).toPromise()
      this.verified = res.status
      console.log(this.verified)
    }
    catch (error){
      console.log(error)
    }
  }

}
