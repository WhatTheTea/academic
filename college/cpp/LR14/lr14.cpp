#include <cmath>
#include <functional>
#include <iostream>
#include <ostream>
#include <string>
#include <vector>

using std::cout, std::cin, std::string, std::vector;
template<typename T>
static void map(vector<vector<T>> &matrix,
                std::function<void(T *, int, int)> fun) {
  for (int i = 0; i < matrix.size(); i++) {
    for (int j = 0; j < matrix.size(); j++) {
      fun(&matrix[i][j], i, j);
    }
  }
}

int main() {
  char choice = 0;
  while (true) {
    cout << "n - число. e - вихід\n";
    cin >> choice;
    if (choice == 'e') break;
    vector<vector<double>> p(choice - '0', vector<double>(choice - '0', 0.0));
    map<double>(p, [](double *v, int i, int j) { *v = sin(i + j); });
    int pos = 0, neg = 0;
    map<double>(p, [&pos, &neg](double *v, int i, int j) { *v > 0 ? pos++ : neg++;});
    cout <<"Додатніх: "<< pos << " Від'ємних: " << neg << '\n';
  }
}