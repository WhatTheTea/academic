#include <iostream>
#include <iomanip>
#include <math.h>

float func(float a, float b, float y)
{
    float top = (a / y) - y;
    float bottom_1 = y / 4;
    float bottom_2 = 1/(12-b);
    float bottom = (bottom_1 + bottom_2);
    if (isinf(top) || isinf(bottom_2) || bottom == 0)
    {
        std::cout << "y = " << y << " Division by zero error\n";
        return NAN;
    }
    return top / bottom;
}
int main(){
    std::cout << "Type: 1. Xstart, 2. Xend, 3. Xstep\n";
    float x_start, x_end, x_step;
    std::cin >> x_start >> x_end >> x_step;

    float a, b;
    std::cout << "Type constants: 1. a 2. b\n";
    std::cin >> a >> b; 

    for (float y = x_start; y <= x_end; y+=x_step)
    {
        float res = func(a, b, y);
        if (isnan(res)) continue;
        std::cout << std::setprecision(3) << std::showpos << "y = " << y << " F#26 = " << res << "\n"; 
    }
}
