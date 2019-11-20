import { Component, OnInit } from '@angular/core';
import * as d3 from 'd3';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.scss']
})
export class MainComponent implements OnInit {

  constructor() { }

  ngOnInit() {
    d3.select("svg")
    .append("circle")
    .attr("fill", "red")
    .attr("cx", "45")
    .attr("cy", "45")
    .attr("r", "10");
  }

}
