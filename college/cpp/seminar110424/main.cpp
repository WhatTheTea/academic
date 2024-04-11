#include <iostream>

int main()
{
    double R = 0, S_circle = 0, S_sphere = 0;
    double pi = 3.14159;
    std::cout << "Радіус: ";
    std::cin >> R;
    S_circle = pi * R * R;
    S_sphere = 4 * pi * R * R;
    printf("Площа круга: %.2f\nПлоща сфери: %.2f\n", S_circle, S_sphere);

    system("pause");
    return 0;
}
