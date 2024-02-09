#include <iostream>
#include <math.h>

int main(int argc, char const *argv[])
{
    auto func1 = [](float x, float b)
    { return b != -1000 ? (x + 1) / (1000 + b) : NAN; };
    auto func2 = [](float x)
    { return (100 * x) + 5; };
    int rng, b_factor;
    std::cin >> rng >> b_factor;
    for (int i = -rng; i <= rng; i++)
    {
        float res;
        if (i <= 0)
        {
            res = func1(i, i & (rand() % b_factor));
            if (isnan(res)) continue;
        }
        else res = func2(i);
        
        std::cout << res << '\n';
    }
    return 0;
}
