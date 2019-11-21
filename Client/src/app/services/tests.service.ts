import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import {Tree} from './tree'
@Injectable({
  providedIn: 'root'
})
export class TestsService {

  tree: Object;

  trees: Tree[];
  serverData: JSON;
  constructor(private http: HttpClient) { }

  sendRequest() {

    this.request()
      .subscribe((response) => {
        this.serverData = response as JSON
        this.readData(response.trees);
        console.log(this.serverData);
        console.log(this.trees);

      });
      
  }
  getGrowPercentage(pTreeLength, pTreeLevels, pLeafLength){
    return (pLeafLength / pTreeLength) ** 1 / pTreeLevels;
  }
  readData(pTrees){
    this.trees = []
    for (var i in pTrees){
      var leafLength = pTrees[i].leafLength
      var length = pTrees[i].length
      var levels = pTrees[i].levels
      var posX = pTrees[i].posX
      this.trees.push(new Tree(length,this.getGrowPercentage(length,levels,leafLength),posX,levels))
    }
  }
  request(): Observable<any> {
    return this.http.post<any>("/run/", {
        // name: "Comase esta"
        time: "10"
        // email: "b",
        // password: "c"
    }).pipe(
      // catchError(this.handleError('addHero', hero))
    );
  }
}
