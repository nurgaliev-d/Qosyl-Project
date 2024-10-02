import { Component, OnInit } from '@angular/core';
import { ApiService } from '../services/services/api.service';

@Component({
  selector: 'app-product',
  templateUrl: './products.component.html',
  styleUrls: ['./products.component.css']
})
export class ProductComponent implements OnInit {
  products: any[] = [];
  baseUrl: string = 'http://localhost:8000';

  constructor(private apiService: ApiService) {}

  ngOnInit(): void {
    this.loadProducts();
  }

  loadProducts(): void {
    this.apiService.getProducts().subscribe(data => {
      this.products = data.map(product => ({
        ...product,
        image: `${this.baseUrl}${product.image}` // Prepend base URL
      }));
    });
  }
}
