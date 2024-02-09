#include <iostream>
#include <vector>

int main(int argc, char const *argv[])
{
    std::vector<int> numbers;
    std::string input;
    int num = 0, result = 0;
    while (std::cin >> input)
    {
        if (input == "x") break;
        num = std::stoi(input);
        numbers.push_back(num);
    }
    switch (numbers.size())
    {
    case 0:
        std::cerr << "empty vector" << '\n';
        break;
    case 1:
        std::cout << numbers.at(0) << '\n';
        break;
    default:
        for(int i = 1, j = 0; i < numbers.size(); i++, j++)
        {
            result += numbers.at(i) * numbers.at(j);
        }
        break;
    }

    std::cout << "result: " << result << "\n"; 
    return 0;
}
