#include <iostream>
//#define FIRST
#define SECOND
using std::cout, std::cin;
#ifdef FIRST

int decs(int a) {
	if (a < 10 || a > 99) return -1;
	return a / 10;
}

int main()
{
	int a = 0;
	cin >> a;
	cout << "Кількість десятків: " << decs(a);
}
#endif // FIRST

#ifdef SECOND
int sumoftree(int a) {
	if (a < 100 || a > 999) return -1;
	return (a / 100) + ((a / 10) % 10) + (a % 10);
}

int main() {
	int a = 0;
	cin >> a;
	cout << "Сума трьох: " << sumoftree(a);
}
#endif // SECOND

