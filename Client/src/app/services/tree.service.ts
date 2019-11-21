import { Injectable } from '@angular/core';
import { Tree } from './tree';
import { PercentPipe } from '@angular/common';

@Injectable({
  providedIn: 'root'
})
export class TreeService {

  constructor() { }

  drawTree(baseLine,percentage,levels,posX, svg) {
    const t = new Tree(baseLine,percentage,posX,levels);
    t.regenerate(true, svg);
  }
}
