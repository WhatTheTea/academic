#include "librarycli.h"
#include "range.h"
#include <iostream>

LibraryCLI::LibraryCLI() {}


void ById()
{
    std::cout << "Введіть діапазон ідентифікаційних номерів: \nВід До: ";
    Range range;
    std::cin >> range.start >> range.end;
    auto book = bookstore.SearchByIdRange(range);
    std::cout << book.toString() << '\n';
}

void ByCopies()
{
    std::cout << "Введіть діапазон кількості примірників: \nВід До: ";
    Range range;
    std::cin >> range.start >> range.end;
    auto book = bookstore.SearchByCopiesRange(range);
    std::cout << book.toString() << '\n';
}

void ByName()
{
    std::cout << "Введіть ім'я книги:";
    string name;
    std::cin >> name;
    auto book = bookstore.SearchByName(name);
    std::cout << book.toString() << '\n';
}

void AddBook()
{
    auto new_book = null<Book>;
    std::cout << "Введіть назву книги: ";
    std::cin >> new_book.title;
    std::cout << "Введіть номер книги: ";
    std::cin >> new_book.id;
    std::cout << "Введіть кількість примірників : ";
    std::cin >> new_book.copies;
    bookstore.Add(new_book);
    std::cout << "Книгу додано!\n";
}

void RemoveBook()
{
    std::cout << "Введіть номер книги:";
    int id = 0;
    std::cin >> id;
    bookstore.Remove(id);
    std::cout << "Книгу видалено!\n";
}

void mainloop()
{
    string input;
    int choice;
    while (true) {
        std::cout << "Меню:\n\t1. Шукати за номером \n\t2. Шукати за кількістю примірників"
             << "\n\t3. Пошук за іменем\n\t4. Додати книжку\n\t5. Видалити книжку\n";
        std::cin >> input;
        if (input == "/exit") break;

        switch (std::stoi(input)) {
        case Menu::ByIdRange:
            ById();
            break;
        case Menu::ByCopiesRange:
            ByCopies();
            break;
        case Menu::ByName:
            ByName();
            break;
        case Menu::AddBook:
            AddBook();
            break;
        case Menu::RemoveBook:
            RemoveBook();
            break;
        }
    }
}
