#include <iostream>
#include <ios>
#include <cmath>
int main(int argc, char const *argv[])
{
    auto func = [](float X){ return 1/(1-pow(sin(X),2)); };
    auto func2 = [](float X) {return 1/(sqrt(1-pow(sin(X),2)));};
    int range[] = {1,2,3,4,5,6,7,8,9,90};
    auto flags = std::ios::showpos 
                | std::ios::scientific 
                | std::ios::uppercase
                ;
    std::cout.setf(flags);
    std::cout.precision(2);
    for (int i : range)
    {
        auto val = func(i);
        auto val2 = func2(i);
        if (std::isnan(val + val2)) return -1;
        std::cout << "Значення f(x) = " << val << '\n';
        std::cout << "Значення g(x) = " << val2 << '\n';
    }
    
    return 0;
}
