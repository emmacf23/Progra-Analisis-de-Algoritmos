import { Component, OnInit, OnChanges } from '@angular/core';
import * as d3 from 'd3';
import { TreeService } from 'src/app/services/tree.service';
import { TestsService } from 'src/app/services/tests.service';
import { Tree } from 'src/app/services/tree';
import { timeout } from 'q';
import { TouchSequence } from 'selenium-webdriver';

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
    this.test_service.sendRequestTree((trees) => {
      console.log("ServerData", trees);
      for (var i in trees) {
        this.tree_service.drawTree(trees[i], d3.select('svg'));
      }
      console.log("Sali")
      this.test_service.sendRequest((response) => {
        this.drawWeb(response, trees);
      });
    });
  }
  grass(x2) {
    this.x2 = x2;

    return this.x2;
  }


  ant(cantAnts) {

    this.cantAnts = cantAnts;

    return this.cantAnts
  }

  drawWeb(response, trees) {
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


    let order: Array<any> = [];
    let treeArray: Array<Number> = [];


    for (var orderIndex in response) {
      order.push(response[orderIndex]);
    }


    for (var treeIndex in trees) {
      treeArray.push(trees[treeIndex]);
    }

    for (let ant = 0; ant <= order[0].length; ant++) {
      d3.select('svg')
        .append('rect')
        .attr('fill', 'black')
        .attr('x', 0)
        .attr('y', 846)
        .attr('width', 8)
        .attr('height', 8);
    }


    let arbol = -1
    d3.selectAll('rect').transition()
      .delay(function (d, i) {
        return 500 * i;
      })
      .on('start', function repeat() {
        arbol = arbol + 1;

        let arbolAVisitar = treeArray[order[0][arbol] - 1]["posX"];
        let arbolHeight = treeArray[order[0][arbol] - 1]["seed"]["l"];
        let arbolLastHeight = treeArray[order[0][arbol] - 1]["seed"]["l"];
        let arbolLevels = treeArray[order[0][arbol] - 1]["seed"]["l"];
        let arbolPercentage = treeArray[order[0][arbol] - 1]["percentage"];


        for (let level = 1; level < arbolLevels; level++) {
          arbolLastHeight = arbolLastHeight * arbolPercentage;
          arbolHeight += arbolLastHeight;
        }

        arbolHeight = Math.round(arbolHeight);

        let speedVariable = arbolAVisitar / 1500
        arbolHeight = arbolHeight / 1500
        d3.active(this)
          // 1 Transition //
          .duration(10000 * speedVariable)
          .attr('x', arbolAVisitar)
          .ease(d3.easeLinear)

          // 2 Transition //
          .transition()
          .duration(10000 * arbolHeight)
          .attr('y', 947)

          // 2 Transition //
          .transition()
          .duration(10000 * speedVariable)
          .attr('x', 0)

          // 1 Transition //
          .transition()
          .duration(10000 * arbolHeight)
          .attr('x', 0)
          .attr('y', 846)
          .transition()
        //.on('start', repeat);

      });
  }
}
