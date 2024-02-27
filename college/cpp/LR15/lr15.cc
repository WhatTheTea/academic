#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <cmath>
#include <vector>

constexpr auto FUNC(double x) { return sin(5 * x) + cos(7 * x) + sin(11 * x); };

template<typename T>
struct FuncResult{ T X; T Y; };

std::vector<FuncResult<double>> doCalc(int start, int end)
{
    std::vector<FuncResult<double>> res;
    for (int x = start; x <= end; x++) res.push_back({(double)x,FUNC(x)});
    return res;
}

std::string toText(const std::vector<FuncResult<double>> &src)
{
    std::stringstream result;
    for (auto &&res : src) {
        result << "X: " 
        << res.X << "\t Y: "
        << res.Y << '\n';
    }
    return result.str();
}

int main(int argc, const char **argv) 
{ 
    std::ofstream fout("result.txt");
    int start = 0, end = 0;
    std::string choice;
    std::cout << "Введіть початок діапазону або /exit: ";
    while (std::cin >> choice) {
        if (choice == "/exit") break;
        start = std::stoi(choice);
        std::cout << "Введіть кінець діапазону: ";
        std::cin >> end;
        auto calc = doCalc(start, end);
        auto text = toText(calc);
        std::cout << text;
        fout << text;
        fout.flush();
    }
    fout.close();
    return 0; 
}