// LR13.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#define ROWS 4
#define COLS 5

using std::cout, std::cin, std::string;

static void cols_ascending()
{

}
static void rows_descending()
{

}
template <size_t rows, size_t cols>
static void populate_matrix(int(&arr)[rows][cols])
{
	cout << "Введіть матрицю " << rows << " x " << cols << '\n';
	for (int i = 0; i < rows; i++)
	{
		for (int j = 0; j < cols; j++)
		{
			cin >> arr[i][j];
		}
	}
}
template <size_t rows, size_t cols>
static void print_matrix(const int(&arr)[rows][cols])
{
	for (int i = 0; i < rows; i++)
	{
		for (int j = 0; j < cols; j++)
		{
			cout << arr[i][j] << '\t';
		}
		cout << '\n';
	}
}

int main()
{
	int p[ROWS][COLS]{};
	char choice = 0;
	while (choice != 'E')
	{
		cout << "Оберіть сортування: 1. Стовпці за зростанням 2. Рядки за спаданням E. Вихід\n";
		cin >> choice;
		switch (choice)
		{
		case '1':
			populate_matrix<ROWS, COLS>(p);
			print_matrix<ROWS, COLS>(p);
			break;
		case '2':
			break;
		case 'E':
			break;
		default:
			cout << "err";
			break;
		}
	}
}