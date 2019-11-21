import {Component, OnInit, OnChanges} from '@angular/core';
import * as d3 from 'd3';
import { TreeService } from 'src/app/services/tree.service';
import { TestsService } from 'src/app/services/tests.service';
import { Tree } from 'src/app/services/tree';
import { timeout } from 'q';

@Component({
  selector: 'app-main',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.scss']
})
export class MainComponent implements OnInit {

  

  constructor(private tree_service: TreeService, private test_service: TestsService) { }

  public x2: number;
  public cantAnts: number;
  
  ngOnInit() {
    this.test_service.sendRequest();
    setTimeout( () => { 
    var trees = this.test_service.trees;  
      for (var i in trees){
        this.tree_service.drawTree(trees[i],d3.select('svg'));
      }
    console.log("Sali")
    this.cualquierNombre();
  }, 500 );
  }
  /*
  ngAfterContentInit(){
    var trees = this.test_service.trees;  
    console.log("Arboles ya cargados",this.test_service.trees)
      for (var i in trees){
        console.log("El i",trees[i])
        this.tree_service.drawTree(trees[i],d3.select('svg'));
      }
    console.log("Sali")
    this.cualquierNombre();
  }*/
/*
  cargarArboles() {    
    
    var trees = this.test_service.trees;
    console.log("Arboles:",trees);
    if (trees != []){
      console.log("Arboles ya cargados",trees)
      for (var i in trees){
        console.log("El i",trees[i])
        this.tree_service.drawTree(trees[i],d3.select('svg'));
      }
      
    }
    console.log("Sali")
    this.cualquierNombre();
  }*/


  grass(x2) {
    this.x2 = x2;

    return this.x2;
  }


  ant(cantAnts) {

    this.cantAnts = cantAnts;

    return this.cantAnts
  }
  
  cualquierNombre(){
    d3.select('svg')
      .append('line')
      .attr('stroke-width', 15)
      .attr('stroke', 'green')
      .attr('x1', '100')
      .attr('y1', '850')
      .attr('x2', this.grass(1500))
      .attr('y2', '850');

    d3.select('svg')
      .append('line')
      .attr('stroke-width', 15)
      .attr('stroke', 'green')
      .attr('x1', '100')
      .attr('y1', '950')
      .attr('x2', this.grass(1500))
      .attr('y2', '950');
      
    /// Anthill ///
    d3.select('svg')
      .append('path')
      .attr('d', 'M-115,850 C-120,870 -110,900 -160,950')
      .attr('fill', 'none')
      .attr('stroke-width', 8)
      .attr('stroke', 'black');

    d3.select('svg')
      .append('path')
      .attr('d', 'M15,850 C17,870 10,900 60,950')
      .attr('fill', 'none')
      .attr('stroke-width', 8)
      .attr('stroke', 'black');

    d3.select('svg')
      .append('path')
      .attr('d', 'M-92,890 C-93,900 -90,900 -130,950')
      .attr('fill', 'none')
      .attr('stroke-width', 2)
      .attr('stroke', 'black');

    d3.select('svg')
      .append('path')
      .attr('d', 'M-5,890 C-3,900 -10,900 40,950')
      .attr('fill', 'none')
      .attr('stroke-width', 2)
      .attr('stroke', 'black');

    d3.select('svg')
      .append('ellipse')
      .attr('fill', 'black')
      .attr('cx', '-50')
      .attr('cy', '850')
      .attr('rx', '70')
      .attr('ry', '25');


    for (let i = 0; i <= 30; i++) {
      d3.select('svg')
        .append('rect')
        .attr('fill', 'black')
        .attr('x', 0)
        .attr('y', 846)
        .attr('width', 8)
        .attr('height', 8);
    }

    
    var i = 200;
    d3.selectAll('rect').transition()
      .delay(function(d, i) {
        return 500 * i;
      })
      .on('start', function repeat() {

        i = i + 100;

        if (i > 1500){
          i = 300;
        }

        var j = i/1500
        d3.active(this)
        // 1 Transition //
          .duration(6000*j)
          .attr('x', i)
          .ease(d3.easeLinear)

          // 2 Transition //
          .transition()
          .duration(2000)
          .attr('y', 947)

          // 2 Transition //
          .transition()
          .duration(6000*j)
          .attr('x', 0)

          // 1 Transition //
          .transition()
          .duration(2000)
          .attr('x', 0)
          .attr('y', 846)
          .transition()
          //.on('start', repeat);

      });

  }
}
