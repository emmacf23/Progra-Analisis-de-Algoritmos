import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class TestsService {

  serverData: JSON;
  constructor(private http: HttpClient) { }

  sendRequest() {

    this.request()
      .subscribe((response) => {
        this.serverData = response as JSON
        console.log(this.serverData);
      });
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
