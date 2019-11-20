import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class TestsService {

  constructor(private http: HttpClient) { }

  sendRequest() {

    this.request()
      .subscribe((response) => {
        console.log(response);
      });
  }

  request(): Observable<any> {
    return this.http.post<any>("/run", {
        name: "Comase esta"
        // email: "b",
        // password: "c"
    }).pipe(
      // catchError(this.handleError('addHero', hero))
    );
  }


}
