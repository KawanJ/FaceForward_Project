import { Component } from '@angular/core';
import { UserService } from '../services/user.service';
import { ToastrService } from 'ngx-toastr';
import { HttpErrorResponse } from '@angular/common/http';

@Component({
  selector: 'app-immigration-records',
  templateUrl: './immigration-records.component.html',
  styleUrls: ['./immigration-records.component.css']
})
export class ImmigrationRecordsComponent {

  constructor(private toastr: ToastrService, private userService:UserService){}

  passportID = "";
  userRecords = null;
  showRecord: boolean = false;

  async getUserData() {
    try {
      const res = await this.userService.getUser(this.passportID).toPromise();
      if(res["Travel_History"].length == 0) {
        this.toastr.warning('Travel Records Empty');
      }
      this.userRecords = res["Travel_History"].reverse();
      this.showRecord = true;
      this.toastr.success('Data Fetched Successfully');
    }
    catch (error) {
      if(error instanceof HttpErrorResponse) {
        this.toastr.error('Please Try again', error.error.error);
      }
      console.log(error)
    }
  }

  goBack() {
    this.showRecord = false;
    this.passportID = "";
    this.userRecords = null;
  }
}
