import { Component } from '@angular/core';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';
import { MatListModule } from '@angular/material/list';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';

@Component({
  standalone: true,
  selector: 'app-search',
  templateUrl: './search.component.html',
  styleUrls: ['./search.component.scss'],
  imports: [
    CommonModule,
    FormsModule,
    MatFormFieldModule,
    MatInputModule,
    MatButtonModule,
    MatListModule
  ],
})
export class SearchComponent {
  searchTerm: string = '';
  regulations: string[] = [
    'Coal mining regulations in Minnesota',
    'Water conservation rules in Arizona',
    'Renewable energy incentives in Texas',
    'Wildlife protection laws in Alaska',
    'Urban transportation upgrades in New York'
  ];
  filteredRegulations: string[] = [];

  search() {
    const term = this.searchTerm.toLowerCase();
    this.filteredRegulations = this.regulations.filter(regulation =>
      regulation.toLowerCase().includes(term)
    );
  }
}