#include <iostream>
#include <vector>

using std::cout, std::cin;

int min(int a, int b, int c, int d, int e) {
	int min = INT_MAX;
	std::vector<int> nums = { a,b,c,d,e };
	for (int i = 0; i < nums.size(); i++)
	{
		if (nums.at(i) > min) continue;
		min = nums.at(i);
	}
	return min;
}

void first() {
	int a = 0, b = 0, c = 0, d = 0, e = 0;
	cout << "Введіть 5 чисел: ";
	cin >> a >> b >> c >> d >> e;
	cout << "Мінімальне: " << min(a, b, c, d, e) << std::endl;
}

void second() {
	auto sq = [](int a, int b, int c) {return 2 * (a * b + b * c + a * c); };
	auto vol = [](int a, int b, int c) {return a * b * c; };

	int a = 0, b = 0, c = 0;
	cout << "Введіть 3 сторони паралелепіпеда: ";
	cin >> a >> b >> c;
	cout << "Площа поверхні: " << sq(a, b, c) << '\n';
	cout << "Об'єм: " << vol(a, b, c) << std::endl;
}

int main()
{
	int choice = 0;
	cout << "Введіть номер задачі (1,2): ";
	cin >> choice;
	switch (choice)
	{
	case 1:
		first();
		break;
	case 2:
		second();
		break;
	default:
		break;
	}
}

