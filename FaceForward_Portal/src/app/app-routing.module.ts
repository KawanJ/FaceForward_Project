import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { TempComponentComponent } from './temp-component/temp-component.component';

const routes: Routes = [
  { path: 'temp', component: TempComponentComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
