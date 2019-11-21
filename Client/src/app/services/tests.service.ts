import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Observable} from 'rxjs';
import {Tree} from './tree';

@Injectable({
  providedIn: 'root'
})
export class TestsService {


  trees: Tree[];
  serverData: JSON;
  bool:boolean = false;
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

  sendRequest() {

    this.request()
      .subscribe((response) => {
        this.serverData = response as JSON;        
        this.readData(this.serverData["trees"]);
        console.log("Server Data:",this.serverData);
        console.log("Arboles: ",this.trees);
        this.bool = true;
      });

  }

  getGrowPercentage(pTreeLength, pTreeLevels, pLeafLength) {
    return (pLeafLength / pTreeLength) ** 1 / pTreeLevels;
  }

  request(): Observable<any> {
    return this.http.post<any>('/run/', {
      time: '10'
    }).pipe(
      // catchError(this.handleError('addHero', hero))
    );
  }
}
