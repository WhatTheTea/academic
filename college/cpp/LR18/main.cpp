#include <iostream>
#include "test.h"

int main()
{
    std::cout << "Hello World!" << std::endl;
    auto t = test();
    t.check();
    return 0;
}
