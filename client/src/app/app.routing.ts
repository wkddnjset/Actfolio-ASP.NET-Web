import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { HomeComponent } from './home/home.component';
import { DetailComponent } from './detail/detail.component';

const appRoutes: Routes = [
	{
		path:"",
		component:HomeComponent,
	},
	{
		path:"detail/:slug",
		component:DetailComponent,
	}
]

@NgModule({
	imports: [
		RouterModule.forRoot(
			appRoutes
		)
	],
	exports : [
		RouterModule
	]
})

export class AppRoutingModule{}