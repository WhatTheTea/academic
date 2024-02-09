#include <iostream>

bool sum(int a, int b, int *res)
{
    *res = a + b;
    return true;
}

int main(int argc, char const *argv[])
{
    bool status = false;
    int res = 0;
    status = sum(5,5,&res);
    std::cout << "Успішно? " << status <<" "<< res << '\n';
    return 0;
}
