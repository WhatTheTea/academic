#include <iostream>
#include <cmath>

using namespace std;

void func(double x, double c)
{
    if(x > 1)
    {
        printf("Результат: %f\n", abs(x-c) + pow(x,6));
    }
    else if (x < 1)
    {
        printf("Результат: %f\n", pow(c*x+14.0, 1/3));
    }
}

int main()
{
    cout << "Введіть початок: ";
    double start = 0, end = 0;
    cin >> start;
    cout << "Введіть end: ";
    cin >> end;

    for(int i = start; i < end; i++)
    {
        func(i,end-i);
    }
    return 0;
}
