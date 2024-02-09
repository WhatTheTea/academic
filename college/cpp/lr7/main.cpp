#include <iostream>
#include <string>

int main(int argc, char const *argv[])
{
    float N = 3, V = 5, Z = 30, R=0;
    int days = 0;
    std::cout << "Введіть рештки матеріалу: ";
    std::cin >> R;
    do
    {
        R += N-V;
        days++;
    } while (R > Z);
    std::cout << "Матеріалу вистачить на " << days << " днів\n"; 
}
