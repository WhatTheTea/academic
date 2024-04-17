#include <cmath>
#include <iostream>

class Radius{
public:
    double value = 0;
    double CircleArea(){
        return pi * this->squared();
    }
    double SphereArea(){
        return 4 * pi * this->squared();
    }
private:
    double pi = 3.14159;
    double squared(){
        return std::pow(this->value, 2);
    }
};

int main()
{
    std::cout << "Радіус: ";
    Radius R;
    std::cin >> R.value;
    printf("Площа круга: %.2f\nПлоща сфери: %.2f\n", R.CircleArea(), R.SphereArea());

    system("pause");
    return 0;
}
