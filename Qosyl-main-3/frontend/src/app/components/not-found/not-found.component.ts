import { Component } from '@angular/core';

@Component({
  selector: 'app-not-found',
  template: `<h2>Page not found</h2><p>The page you're looking for doesn't exist.</p>`,
  styles: ['h2 { color: red; }']
})
export class NotFoundComponent {}
