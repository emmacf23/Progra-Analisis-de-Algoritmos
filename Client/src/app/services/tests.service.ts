import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Tree } from './tree';
import { TreeService } from './tree.service'
@Injectable({
  providedIn: 'root'
})
export class TestsService {


  trees: Tree[];
  order: [];
  serverData: JSON;
  bool: boolean = false;
  constructor(private http: HttpClient) {
  }

  readData(pTrees) {
    this.trees = [];
    var t = pTrees["test"]
    for (var i in t) {
      var leafLength = t[i]["leafLength"];
      var length = t[i]["length"];
      var levels = t[i]["levels"];
      var posX = t[i]["posX"];
      this.trees.push(new Tree(posX, this.getGrowPercentage(length, levels, leafLength), length, levels));
    }
  }

  sendRequest(onSuccess: (response: any) => void) {

    this.request()
      .subscribe(onSuccess);

  }

  sendRequestTree(onSuccess: (response: any) => void) {
    this.requestTree()
      .subscribe((response) => {
        this.serverData = response as JSON;
        this.readData(this.serverData["trees"]);
        onSuccess(this.trees);
      });
  }

  getGrowPercentage(pTreeLength, pTreeLevels, pLeafLength) {
    return (pLeafLength / pTreeLength) ** 1 / pTreeLevels;
  }

  request(): Observable<any> {
    return this.http.post<any>('/test/', {
      time: '60'
    }).pipe(
      // catchError(this.handleError('addHero', hero))
    );
  }

  requestTree(): Observable<any> {
    return this.http.get<any>('/run/').pipe(
      // catchError(this.handleError('addHero', hero))
    );
  }
}
