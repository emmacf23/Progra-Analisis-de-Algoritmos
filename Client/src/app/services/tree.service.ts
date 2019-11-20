import { Injectable } from '@angular/core';
import { Tree } from './tree';

@Injectable({
  providedIn: 'root'
})
export class TreeService {

  constructor() { }

  drawTree(svg) {
    const t = new Tree();
    t.regenerate(true, svg);
  }
}
