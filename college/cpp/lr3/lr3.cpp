#include <iostream>

int main()
{
    char sentence[100];
    std::cout << "Enter a sentence (format: word1;word2;word3;...;wordN): ";
    std::cin >> sentence;
    int count = 0; // Підрахунок випадків 'b' між ';'
    bool is_first = false;
    for (int i = 0; sentence[i] != '\0'; i++) // Перебір по реченню
    {
        if (sentence[i] == ';' && sentence[i+1] == 'b') // Перевірка на ';' & 'b'
            count++;
    }

    std::cout << count << std::endl;
}