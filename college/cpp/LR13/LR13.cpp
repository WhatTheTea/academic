#include <algorithm>
#include <functional>
#include <iostream>
#include <vector>
#define ROWS 4
#define COLS 5

using std::cout, std::cin, std::string, std::vector;

static void sort_matrix(vector<vector<int>> &matrix) {
  for (auto &&row : matrix) {
    std::sort(row.begin(), row.end(), std::greater<int>());
  }
}

static void print_matrix(const vector<vector<int>> &matrix) {
  for (auto &&row : matrix) {
    for (auto &&col : row) {
      cout << col << ' ';
    }
    cout << '\n';
  }
}

static auto transpose(const vector<vector<int>> &matrix) {
  vector<vector<int>> result(matrix[0].size(), vector<int>());
  for (int r = 0; r < matrix.size(); r++) {
    for (int c = 0; c < matrix[r].size(); c++) {
      result[c].push_back(matrix.at(r).at(c));
    }
  }
  return result;
}

int main() {
  vector<vector<int>> p{{1, 2, 3, 4, 5},
                        {10, 9, 8, 7, 6},
                        {5, 4, 3, 2, 1},
                        {6, 7, 8, 9, 10}};
  char choice = 0;
  while (choice != '0') {
    cout << "Меню: 1. Стовпці 2. Рядки 0. Вихід\n";
    cin >> choice;
    switch (choice) {
    case '1': {
      print_matrix(p);
      auto mat = transpose(p);
      cout << "\n";
      sort_matrix(mat);
      print_matrix(transpose(mat));
      break;
    }
    case '2': {
      auto mat(p);
      print_matrix(mat);
      cout << "\n";
      sort_matrix(mat);
      print_matrix(mat);
      break;
    }
    case '0':
      break;
    default:
      cout << "err";
      break;
    }
  }
}