#include <fstream>
#include <iostream>
#include <sstream>
#include <string>


constexpr auto Y(double x) { return sin(5 * x) + cos(7 * x) + sin(11 * x); };

int main(int argc, const char **argv) 
{ 
    std::ofstream fout("result.txt");
    std::stringstream result;
    int start = 0, end = 0;
    std::string choice;
    std::cout << "Введіть початок діапазону або /exit: ";
    while (std::cin >> choice) {
        if (choice == "/exit") break;

    }
    return 0; 
}