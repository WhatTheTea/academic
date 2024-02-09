#include <functional>
#include <iostream>
#include <ostream>
constexpr int N = 3;
template <int rows, int cols>
void map_matrix(int (&m)[rows][cols], std::function<void(int &)> f) {
  for (int(&i)[cols] : m) {
    for (int &j : i) {
      f(j);
    }
  }
}
int main(int argc, const char **argv) {
  int matrix[N][N] = {
      {1, 2, 3},
      {4, 1, 2},
      {2, 8, 1},
  };
  int count = 0, number = 0;
  auto counter = [&count, &number](int &i) {
    if (i == number)
      count++;
  };

  std::cout << "Введіть число: ";
  std::cin >> number;
  map_matrix(matrix, counter);
  std::cout << "Кількість входжень числа " << number << " в матрицю: " << count
            << std::endl;
  return 0;
}