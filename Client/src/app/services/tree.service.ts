import { Injectable } from '@angular/core';
import { Tree } from './tree';

@Injectable({
  providedIn: 'root'
})
export class TreeService {

  constructor() { }

  drawTree(baseLine, svg) {
    const t = new Tree(baseLine);
    t.regenerate(true, svg);
  }
}
