#include <iostream>
#include <cmath>

using namespace std;

double func(double x, double y)
{
    double cos1 = pow(y,3) + sqrt(4*x*sin(x));
    double div = exp(2*x) / sqrt(3*x);
    return cos(cos1) + div;
}

int main()
{
    cout << "Введіть х: ";
    double x = 0, y = 0;
    cin >> x;
    cout << "Введіть y: ";
    cin >> y;
    cout << "Результат: " << func(x,y) << '\n';
    return 0;
}
