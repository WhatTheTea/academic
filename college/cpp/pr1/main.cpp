#define FMT_HEADER_ONLY
#include "fmt/include/fmt/core.h"
#include <iostream>
#include <math.h>
int main(int argc, char const *argv[])
{
    fmt::println("Введіть x, d, f");
    float x,d,f,y;
    std::cin >> x >> d >> f;
    y = ((x*x)/(d-f)) + (d/f)/x;
    if (isinf(y)) {
        fmt::println("Ділення на нуль");
        return 1;
    }
    fmt::println("Відповідь: {:f}", y);
    return 0;
}
