#include <cstring>
#include <functional>
#include <iostream>

constexpr int R = 3;
constexpr int C = 5;
constexpr int matrix[R][C] = {
    {6, 10, 2, 4, 2}, {5, 7, 13, 3, 1}, {5, 10, 1, 4, 2}};

template <int rows, int cols>
void map_matrix(int (&m)[rows][cols], std::function<void(int &)> f) {
  for (int(&i)[cols] : m) {
    for (int &j : i) {
      f(j);
    }
  }
}

int main(int argc, const char **argv) {
  // init
  int m[R][C] = {};
  float count = 0;
  float sum = 0;
  // funcs
  auto counter = [&count](int &i) { count++; };
  auto summer = [&sum](int &i) { sum += i; };
  float mean = 0;
  auto addsubber = [&mean](int &i) { i = (i >= mean ? 1 : -1); };
  auto outer = [](int &i) { std::cout << i << " "; };
  memcpy(m, matrix, R * C * sizeof(int));

  map_matrix(m, counter); // рахуємо кількість елементів у всій таблиці
  map_matrix(m, summer);
  mean = sum / count;
  map_matrix(m, addsubber);
  map_matrix(m, outer);
  return 0;
}