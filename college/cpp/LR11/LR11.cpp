#include <iostream>
#include <math.h>

using std::cout, std::cin;

inline float G(float y, float f){
    return exp(2 * y) + sin(pow(f, 2));
}

int main() {
    float y = 0.0, f = 0.0;
    bool cont = true;
    while (cont)
    {
        cout << "Введіть значення y та f: ";
        cin >> y >> f;
        cout << G(y, f) << '\n';
        cout << "Продовжити?\n0. Ні\n1. Так\n";
        cin >> cont;
    }
}
