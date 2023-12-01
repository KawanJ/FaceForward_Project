import { Component,ViewEncapsulation  } from '@angular/core';
import { UserService } from '../services/user.service';
import { ToastrService } from 'ngx-toastr';
import { HttpErrorResponse } from '@angular/common/http';

@Component({
  encapsulation: ViewEncapsulation.None,
  selector: 'app-immigration-checkin',
  templateUrl: './immigration-checkin.component.html',
  styleUrls: ['./immigration-checkin.component.css']
})
export class ImmigrationCheckinComponent {

  constructor(private toastr: ToastrService, private userService:UserService) {}

  id: string = ""; 
  isVerifying: boolean = false;
  verified: boolean | null = null;
  showAlert: boolean = false;
  alertColor: string = "transparent";

  async verifyUser() {
    this.isVerifying = true;
    try {
      this.isVerifying = true;

      const res = await this.userService.verifyUser(this.id).toPromise();
      this.verified = res.status;
  
      // Set alert color based on verification status
      this.alertColor = this.verified ? 'green' : '#f28080';
  
      // Show the alert for 5 seconds
      this.showAlert = true;
      setTimeout(() => {
        this.showAlert = false;
        this.alertColor = "transparent"; // Reset alert color after fade-out
      }, 5000);

      //Reseting variables
      this.id = "";
    } 
    catch (error) {
      if(error instanceof HttpErrorResponse) {
        this.toastr.error('Please Try again', error.error.error);
      }
      console.log(error)
    }
    this.isVerifying = false;
  }
}
