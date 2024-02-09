#include <iostream>
#include <math.h>

int main(int argc, char const *argv[])
{
    auto func1 = [](float x)
    { return x != 0 ? cos(x-1)/x : NAN; };
    int rng;
    std::cin >> rng;
    for (int i = -rng; i <= rng; i++)
    {
        float res = func1(i);
        if (isnan(res)) continue;
        std::cout << res << '\n';
    }
    return 0;
}
