#include <iostream>
#include <vector>

#define count(a) (sizeof(a) / sizeof(*a))

int main(int argc, char const *argv[])
{
    int numbers[100];
    std::string input;
    int num = 0, result = 0;
    while (std::cin >> input)
    {
        if (input == "x")
            break;
        num = std::stoi(input);
        numbers[count(numbers)] = num;
    }
    switch (count(numbers))
    {
    case 0:
        std::cerr << "empty vector" << '\n';
        break;
    case 1:
        std::cout << numbers[0] << '\n';
        break;
    default:
        for (int i = 1, j = 0; i < count(numbers); i++, j++)
        {
            result += numbers[i] * numbers[j];
        }
        break;
    }

    std::cout << "result: " << result << "\n";
    return 0;
}
