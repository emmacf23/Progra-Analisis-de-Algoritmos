import { Component, OnInit } from '@angular/core';
import * as d3 from 'd3';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.scss']
})
export class MainComponent implements OnInit {

  constructor() { }

  public x2: number;
  public cantAnts: number;


  ngOnInit() {
<<<<<<< Updated upstream

    /// Grass //
    d3.select("svg")
    .append("line")
    .attr("stroke-width", 15)
    .attr("stroke", "green")
    .attr("x1","-150")
    .attr("y1","850")
    .attr("x2",this.grass(1300))
    .attr("y2","850");

    d3.select("svg")
    .append("line")
    .attr("stroke-width", 15)
    .attr("stroke", "green")
    .attr("x1","-150")
    .attr("y1","950")
    .attr("x2",this.grass(1300))
    .attr("y2","950");

    /// Anthill ///
    d3.select("svg")
    .append("path")
    .attr("d","M-365,850 C-370,870 -360,900 -410,950")
    .attr("fill","none")
    .attr("stroke-width",8)
    .attr("stroke","black");

    d3.select("svg")
    .append("path")
    .attr("d","M-235,850 C-233,870 -240,900 -190,950")
    .attr("fill","none")
    .attr("stroke-width",8)
    .attr("stroke","black");

    d3.select("svg")
    .append("path")
    .attr("d","M-342,890 C-343,900 -340,900 -380,950")
    .attr("fill","none")
    .attr("stroke-width",2)
    .attr("stroke","black");

    d3.select("svg")
    .append("path")
    .attr("d","M-255,890 C-253,900 -260,900 -210,950")
    .attr("fill","none")
    .attr("stroke-width",3)
    .attr("stroke","black");

    d3.select("svg")
    .append("ellipse")
    .attr("fill", "black")
    .attr("cx", "-300")
    .attr("cy", "850")
    .attr("rx", "70")
    .attr("ry", "25");


    for(let i = 0; i<= 30; i++)
      d3.select("svg")
        .append("rect")
        .attr("fill","black")
        .attr("x",-250)
        .attr("y",846)
        .attr("width",8)
        .attr("height",8)

    let distance = this.grass(1290)
    d3.selectAll("rect").transition()
    .delay(function(d,i){ return 500 * i})
      .on("start", function repeat(){

        d3.active(this)
        // 1 Transition //
        .duration(3000)
        .attr("x",distance)
        .ease(d3.easeLinear)

        // 2 Transition //
        .transition()
        .duration(2000)
        .attr("y",947)

        // 2 Transition //
        .transition()
        .duration(3000)
        .attr("x",-150)

        // 1 Transition //
        .transition()
        .duration(2000)
        .attr("x",-250)
        .attr("y",846)
        .transition()
        .on("start", repeat);

      });
      

  }

  // Funcion para ampliar el x2 de los caminos //
  grass(x2){

=======
    d3.select('svg')
    .append('circle')
    .attr('fill', 'red')
    .attr('cx', '45')
    .attr('cy', '45')
    .attr('r', '10');

    d3.select('svg')
    .append('line')
    .attr('stroke-width', 0.7)
    .attr('stroke', 'green')
    .attr('x1', '-40')
    .attr('y1', '90')
    .attr('x2', this.grass(140))
    .attr('y2', '90');

  }

  grass(x2) {
>>>>>>> Stashed changes
    this.x2 = x2;

    return this.x2;
  }


  ant(cantAnts){

    this.cantAnts = cantAnts;

    return this.cantAnts
  }
}
