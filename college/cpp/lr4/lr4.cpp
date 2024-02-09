#define FMT_HEADER_ONLY
#include "fmt/include/fmt/core.h"

#include <iostream>

float fuel_compute(int usage, int distance)
{
    return ((float)usage / 100.0f) * (float)distance;
}
void task1()
{
    auto fuel_usage = 7; // 7 / 100 km
    auto toA = 200, toB = 300, toC = 60, toD = 20;
    auto choice = '\0';
    bool validInput = true;
    float fuel = 0;
    fmt::print("Оберіть пункт призначення(А,B,C,D): ");
    std::cin >> choice;
    switch (choice)
    {
    case 'A':
        fuel = fuel_compute(fuel_usage, toA);
        break;
    case 'B':
        fuel = fuel_compute(fuel_usage, toB);
        break;
    case 'C':
        fuel = fuel_compute(fuel_usage, toC);
        break;
    case 'D':
        fuel = fuel_compute(fuel_usage, toD);
        break;

    default:
        fmt::println("Помилка");
        validInput = false;
        break;
    }
    if (validInput)
        fmt::println("Потрібна кількість палива: {:.2f}", fuel);
}
void task2()
{
    fmt::print("Введіть латинську літеру: ");
    auto symbol = '\0';
    std::cin >> symbol;
    switch (symbol)
    {
    case 'a':
    case 'e':
    case 'i':
    case 'o':
    case 'u':
        fmt::println("Літера голосна");
        break;
    default:
        fmt::println("Літера приголосна");
        break;
    }
}
void task3()
{
    fmt::print("Введіть номер аудиторії: ");
    auto room = 0;
    std::cin >> room;
    switch (room / 100)
    {
    case 1:
        fmt::println("Перший поверх");
        break;
    case 2:
        fmt::println("Другий поверх");
        break;
    case 3:
        fmt::println("Третій поверх");
        break;
    case 4:
        fmt::println("Четвертий поверх");
        break;
    
    default:
        fmt::println("Некоректний номер");
        break;
    }
}


int main(int argc, char const *argv[])
{
    bool running = true;
    while (running)
    {
        auto task = 0;
        fmt::print("Введіть номер задачі: ");
        std::cin >> task;
        switch (task)
        {
        case 1:
            task1();
            break;
        case 2:
            task2();
            break;
        case 3:
            task3();
            break;
        default:
            fmt::println("Некоректний ввід, вихід з програми");
            running = false;
            break;
        }
    }

    return 0;
}
