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
  buyProduct(productId: number): void {
    // Logic for buying the product
    // You can navigate to a checkout page or show a confirmation message
    console.log(`Product ${productId} purchased!`);
    // Example: Navigate to checkout (assuming you have a router set up)
    // this.router.navigate(['/checkout', productId]);
  }
}
