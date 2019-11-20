import { Component, OnInit } from '@angular/core';
import * as d3 from 'd3';
import { TreeService } from 'src/app/services/tree.service';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.scss']
})
export class MainComponent implements OnInit {

  constructor(private tree_service: TreeService) { }

  public x2: number;


  ngOnInit() {
    d3.select("svg")
    .append("circle")
    .attr("fill", "red")
    .attr("cx", "45")
    .attr("cy", "45")
    .attr("r", "10");

    d3.select("svg")
    .append("line")
    .attr("stroke-width", 0.7)
    .attr("stroke", "green")
    .attr("x1","-40")
    .attr("y1","90")
    .attr("x2",this.grass(140))
    .attr("y2","90");

    this.tree_service.drawTree(d3.select('svg'));
  }

  grass(x2){
    this.x2 = x2;

    return this.x2;
  }

}
