import { Component } from '@angular/core';
import { TempServiceService } from '../Services/temp-service.service';

@Component({
  selector: 'app-temp-component',
  templateUrl: './temp-component.component.html',
  styleUrls: ['./temp-component.component.css']
})
export class TempComponentComponent {
  inputString: string = '';

  constructor(private tempService: TempServiceService) {}

  async addString() {
    try {
      await this.tempService.addData(this.inputString).toPromise();
      console.log('String added successfully');
    } catch (error) {
      console.error('Error adding string:', error);
    }
  }

  async showResult() {
    try {
      let res = await this.tempService.viewData().toPromise();
      console.log(res);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  }
}
