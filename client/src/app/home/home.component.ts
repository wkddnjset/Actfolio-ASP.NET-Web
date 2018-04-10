import { Component, OnInit } from '@angular/core';
import { NgxCarousel } from 'ngx-carousel';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  constructor() { }

  	public carouselOne: NgxCarousel;

  	ngOnInit() {
		this.carouselOne = {
			grid: {xs: 1, sm: 1, md: 2, lg: 3, all: 0},
			slide: 1,
			speed: 1500,
			interval: 3000,
			point: {
				visible: true
			},
			load: 2,
			touch: true,
			loop: true,
			custom: 'banner'
		}
	}
}
