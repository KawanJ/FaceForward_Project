import { Component } from '@angular/core';
import { UserService } from '../services/user.service';

@Component({
  selector: 'app-immigration-records',
  templateUrl: './immigration-records.component.html',
  styleUrls: ['./immigration-records.component.css']
})
export class ImmigrationRecordsComponent {

  constructor(private userService:UserService){  }

  id = ""
  user = null

  async getUserData()
  {
    try{
      const res = await this.userService.getUser(this.id).toPromise()
      this.user = res["Travel_History"]
      console.log(this.user)
    }
    catch (error){
      console.log(error)
    }
  }
}
