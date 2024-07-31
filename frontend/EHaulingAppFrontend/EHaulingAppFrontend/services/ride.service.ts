import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class RideService {
  private baseUrl = 'http://localhost:5000/api/ride';

  constructor(private http: HttpClient) { }

  requestRide(data: any): Observable<any> {
    return this.http.post(`${this.baseUrl}/request`, data);
  }
}