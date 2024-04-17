#include <iostream>
#include <cmath>

using namespace std;

double func(double x)
{
    double tg = log(x)/(sqrt(2*x)+(3.14/4));
    double cs = pow(x,2) + (2/3) * 3.14;
    return tan(tg) * cos(cs);
}

int main()
{
    cout << "Введіть х: ";
    double x = 0;
    cin >> x;
    printf("Результат: %f\n", func(x));
    return 0;
}
