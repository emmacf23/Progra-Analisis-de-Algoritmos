import { Injectable } from '@angular/core';
import { Tree } from './tree';
import { PercentPipe } from '@angular/common';

@Injectable({
  providedIn: 'root'
})
export class TreeService {

  constructor() { }

  drawTree(tree, svg) {
    const t = tree;
    t.regenerate(true, svg);
  }
}
